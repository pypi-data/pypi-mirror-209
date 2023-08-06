import asyncio
import json
import os
import ray
import sys
from typing import Optional

import requests
import typer
import urwid
import websockets

from launch.auth import cache
from launch.jobs import console_ui
from launch.session_state import LastJobInfo, LaunchFlowSession

RAY_CLUSTER_ADDRESS = 'http://127.0.0.1:8265'


def zipdir(path, ziph, requirements_path: str):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            full_file_path = os.path.join(root, file)
            if full_file_path == requirements_path:
                # No need to add requirements file we will do this below.
                continue
            ziph.write(
                full_file_path,
                os.path.relpath(full_file_path, os.path.join(path, '.')))


def send_deploy_request(
    server_address: str,
    zip_file: Optional[str],
    entry_point: str,
    account_id: Optional[int],
    project_id: Optional[int],
    pipeline_id: Optional[int],
    has_requirements: bool,
    bearer_token: str,
) -> str:
    version = sys.version_info
    python_version = f'{version.major}.{version.minor}'

    if zip_file is not None:
        files = {
            'zip_file': ('working_dir.zip', open(zip_file,
                                                 'rb'), 'application/zip')
        }
    else:
        files = None
    data = {
        'account_id': account_id,
        'project_id': project_id,
        'pipeline_id': pipeline_id,
        'entry_point': entry_point,
        'python_version': python_version,
        'ray_version': ray.__version__,
    }
    if has_requirements:
        data['requirements_file_relative_path'] = './requirements.txt'
    response = requests.post(
        f'{server_address}/jobs/create',
        headers={'Authorization': f'Bearer {bearer_token}'},
        files=files,
        data=data)
    state = LaunchFlowSession.load()
    if response.status_code != 200:
        json_content = json.loads(response.content.decode())
        state.last_job_info = LastJobInfo(
            job_id=None, job_create_http_status=response.status_code)
        state.write()
        raise ValueError(f'Remote run failed: {json_content["detail"]}.')
    output = response.json()
    job_id = output['id']
    print('Remote run launched succesfully. To track progress run:')
    print()
    print('    To attach to job run: ')
    print(f'        launch jobs attach {job_id}')
    print('    To drain job run:')
    print(f'        launch jobs drain {job_id}')
    print('    To stop job run:')
    print(f'        launch jobs stop {job_id}')
    state.last_job_info = LastJobInfo(
        job_id=output['id'], job_create_http_status=response.status_code)
    state.write()
    return output['id']


async def stream_job_info(
    job_id: str,
    launchflow_server_address: str,
    bearer_token: Optional[str],
    extension_server_address: str,
):
    if bearer_token is None:
        creds = cache.get_user_creds(launchflow_server_address)
        bearer_token = creds.id_token

    ws_endpoint = launchflow_server_address.replace('http://',
                                                    'ws://').replace(
                                                        'https://', 'wss://')
    if ws_endpoint.endswith('/'):
        ws_endpoint = ws_endpoint[:-1]
    try:
        async for ws in websockets.connect(
                f'{ws_endpoint}/jobs/info?job_id={job_id}',
                open_timeout=1,
                extra_headers={'Authorization': f'Bearer {bearer_token}'}):
            while True:
                data = await ws.recv()
                job_info = json.loads(data)
                job_info['runtime'] = 'REMOTE'
                requests.post(extension_server_address, json=job_info)
    except Exception as e:
        typer.echo(str(e))
        raise typer.Exit(1)


async def stream_job_logs(
    job_id: str,
    launchflow_server_address: str,
    bearer_token: Optional[str],
    extension_server_address: str,
):
    if bearer_token is None:
        creds = cache.get_user_creds(launchflow_server_address)
        bearer_token = creds.id_token

    ws_endpoint = launchflow_server_address.replace('http://',
                                                    'ws://').replace(
                                                        'https://', 'wss://')
    if ws_endpoint.endswith('/'):
        ws_endpoint = ws_endpoint[:-1]
    try:
        async for ws in websockets.connect(
                f'{ws_endpoint}/jobs/tail_logs?job_id={job_id}',
                open_timeout=1,
                extra_headers={'Authorization': f'Bearer {bearer_token}'}):
            while True:
                data = await ws.recv()
                print(data)
                # requests.post(extension_server_address, json=data)
    except Exception as e:
        typer.echo(str(e))
        raise typer.Exit(1)


def _stop_job(job_id: str,
              server_address: str,
              bearer_token: Optional[str] = None):
    if not bearer_token:
        creds = cache.get_user_creds(server_address)
        bearer_token = creds.id_token
    response = requests.post(
        f'{server_address}/jobs/stop',
        headers={'Authorization': f'Bearer {bearer_token}'},
        json={'job_id': job_id})
    return response


def stop_job_cli(job_id: str,
                 server_address: str,
                 bearer_token: Optional[str] = None):
    response = _stop_job(job_id, server_address, bearer_token)
    if response.status_code != 200:
        print(f'Failed to stop job error: {response.content.decode()}')
        return
    print('Job is now stopping.')


def stop_job_urwid(job_id: str, server_address: str, button):
    response = _stop_job(job_id, server_address)
    if response.status_code != 200:
        try:
            json_error = response.json()
            console_ui.error_widget.set_text(json_error['detail'])
        except json.JSONDecodeError:
            console_ui.error_widget.set_text(
                f'Stop failed: {response.content}')


def _drain_job(job_id: str,
               server_address: str,
               bearer_token: Optional[str] = None):
    if not bearer_token:
        creds = cache.get_user_creds(server_address)
        bearer_token = creds.id_token
    response = requests.post(
        f'{server_address}/jobs/drain',
        headers={'Authorization': f'Bearer {bearer_token}'},
        json={'job_id': job_id})
    return response


def drain_job_cli(job_id: str,
                  server_address: str,
                  bearer_token: Optional[str] = None):
    response = _drain_job(job_id, server_address, bearer_token)
    if response.status_code != 200:
        print(f'Failed to drain job error: {response.content.decode()}')
        return
    print('Job is now draining.')


def drain_job_urwid(job_id: str, server_address: str, button):
    response = _drain_job(job_id, server_address)
    if response.status_code != 200:
        try:
            json_error = response.json()
            console_ui.error_widget.set_text(json_error['detail'])
        except json.JSONDecodeError:
            console_ui.error_widget.set_text(
                f'Drain failed: {response.content}')


async def run_console_ui(job_id: int, server_address: str):
    aloop = asyncio.get_event_loop()
    import nest_asyncio
    nest_asyncio.apply(aloop)
    ev_loop = urwid.AsyncioEventLoop(loop=aloop)
    loop = urwid.MainLoop(console_ui.get_main_frame(job_id),
                          palette=console_ui.PALETTE,
                          event_loop=ev_loop)

    update_job_fd = loop.watch_pipe(console_ui.update_job_info)
    aloop.create_task(
        console_ui.get_job_info(update_job_fd, job_id, server_address))
    aloop.create_task(console_ui.get_logs(job_id, server_address))

    urwid.connect_signal(obj=console_ui.drain_button,
                         name='click',
                         callback=drain_job_urwid,
                         user_args=[job_id, server_address])
    urwid.connect_signal(obj=console_ui.stop_button,
                         name='click',
                         callback=stop_job_urwid,
                         user_args=[job_id, server_address])

    loop.run()


def get_logs(job_id: str, server_address: str):
    creds = cache.get_user_creds(server_address)
    response = requests.post(
        f'{server_address}/jobs/get_logs',
        headers={'Authorization': f'Bearer {creds.id_token}'},
        json={'job_id': job_id})
    if response.status_code != 200:
        typer.echo(f'Failed to get logs: {response.content.decode()}')
        raise typer.Exit(1)
    log_lines = response.json()
    print('\n'.join(log_lines))
