import asyncio
import os
import signal
import socket
import subprocess
from sys import platform
from typing import List, Optional
import atexit

import requests
from pkg_resources import resource_filename
from ray.job_submission import JobSubmissionClient

from launch.prometheus import queries

RAY_CLUSTER_ADDRESS = 'http://127.0.0.1:8265'


def _port_is_open(port: str, host: str = 'http://localhost', timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
    except Exception:
        return False
    else:
        sock.close()
        return True


def local_runtime_is_initialized():
    for port in ['8265', '9090']:
        if not _port_is_open(port):
            return False
    return True


def initialize_local_runtime_environment_and_block():
    # TODO: should include other distributions.
    if platform == "linux" or platform == "linux2":
        executable = 'linux/prometheus'
    elif platform == "darwin":
        executable = 'mac/prometheus'
    else:
        raise ValueError(
            f'launch CLI is not supported for platform: {platform}')
    prom_dir = resource_filename('launch', 'prometheus')

    prom_process = subprocess.Popen(
        f'./{executable} --config.file=/tmp/ray/session_latest/metrics/prometheus/prometheus.yml',  # noqa
        cwd=f'{prom_dir}/.',
        shell=True)
    ray_process = subprocess.Popen('ray start --head --block', shell=True)

    atexit.register(prom_process.terminate)
    atexit.register(ray_process.terminate)
    ray_process.wait()
    print('Environment shutdown.')


def initialize_local_runtime_environment():
    subprocess.run('ray start --head', shell=True)
    # TODO: should include other distributions.
    if platform == "linux" or platform == "linux2":
        executable = 'linux/prometheus'
    elif platform == "darwin":
        executable = 'mac/prometheus'
    else:
        raise ValueError(
            f'launch CLI is not supported for platform: {platform}')
    prom_dir = resource_filename('launch', 'prometheus')
    # TODO: Add better process management for prometheus and ray.
    _ = subprocess.Popen(
        f'./{executable} --config.file=/tmp/ray/session_latest/metrics/prometheus/prometheus.yml',  # noqa
        cwd=f'{prom_dir}/.',
        shell=True)


def shutdown_local_runtime_environment():
    subprocess.run('ray stop', shell=True)
    subprocess.run('fuser -k 9090/tcp', shell=True)


def submit_job_to_ray_cluster(
    entrypoint: str,
    working_dir: Optional[str] = None,
    requirements_file: Optional[str] = None,
    cluster_address: str = RAY_CLUSTER_ADDRESS,
) -> str:
    client = JobSubmissionClient(cluster_address)

    runtime_env = {}
    if working_dir is not None:
        runtime_env['working_dir'] = working_dir
    if requirements_file is not None:
        runtime_env['pip'] = requirements_file

    job_id = client.submit_job(entrypoint=entrypoint, runtime_env=runtime_env)
    return job_id


async def stream_job_logs_async(job_id: str,
                                cluster_address: str = RAY_CLUSTER_ADDRESS):
    client = JobSubmissionClient(cluster_address)
    print('streaming logs...')
    async for lines in client.tail_job_logs(job_id):
        print(lines, end="")


def stream_job_logs(job_id: str, cluster_address: str = RAY_CLUSTER_ADDRESS):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(stream_job_logs_async(job_id, cluster_address))
    loop.close()


def get_job_info(ray_client: JobSubmissionClient, job_id: str):
    ray_info = ray_client.get_job_info(job_id)
    job_info = {
        'id': ray_info.submission_id,
        'runtime': 'LOCAL',
        'job_status': ray_info.status,
        'latest_metrics': {
            'throughput': '0',
            'processor_latency': '0',
            'num_replicas': '0',
        }
    }
    if ray_info.status in ['RUNNING', 'PENDING']:
        job_info['latest_metrics'] = {
            'throughput': queries.throughput(ray_info.job_id),
            'processor_latency': queries.processor_latency(ray_info.job_id),
            'num_replicas': queries.num_replicas(ray_info.job_id),
        }
    return job_info


def ping_job_info(
    job_ids: List[str],
    extension_server_address: Optional[str] = None,
    cluster_address: str = RAY_CLUSTER_ADDRESS,
):
    try:
        client = JobSubmissionClient(cluster_address)
    except Exception:
        print('ray cluster is not running.')
        return
    print(f'pinging job status for {len(job_ids)} jobs...')
    for job_id in job_ids:
        job_info = get_job_info(client, job_id)
        print(job_info)
        if extension_server_address is not None:
            requests.post(extension_server_address, json=job_info)


async def stream_job_info_async(
    job_id: str,
    extension_server_address: Optional[str] = None,
    cluster_address: str = RAY_CLUSTER_ADDRESS,
):
    client = JobSubmissionClient(cluster_address)
    print('streaming job status...')
    while True:
        job_info = get_job_info(client, job_id)
        if extension_server_address is not None:
            requests.post(extension_server_address, json=job_info)
        if job_info['job_status'] in ['FAILED', 'STOPPED', 'SUCCEEDED']:
            break
        await asyncio.sleep(3)


def stream_job_info(
    job_id: str,
    extension_server_address: Optional[str] = None,
    cluster_address: str = RAY_CLUSTER_ADDRESS,
):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(
        stream_job_info_async(job_id, extension_server_address,
                              cluster_address))
    loop.close()


def stop_job(job_id: str, cluster_address: str = RAY_CLUSTER_ADDRESS):
    client = JobSubmissionClient(cluster_address)
    return client.stop_job(job_id)


def drain_job(job_id: str, cluster_address: str = RAY_CLUSTER_ADDRESS):
    client = JobSubmissionClient(cluster_address)
    job_info = client.get_job_info(job_id)
    pid = job_info.driver_info.pid
    os.kill(int(pid), signal.SIGINT)
    return True
