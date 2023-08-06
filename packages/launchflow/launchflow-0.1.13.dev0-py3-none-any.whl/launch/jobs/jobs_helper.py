from typing import Any, Dict

import requests
import typer


def list_jobs(
    pipeline_id: str,
    launchflow_server_address: str,
    creds,
    running: bool,
) -> Dict[str, Any]:
    response = requests.post(
        f'{launchflow_server_address}/jobs/list',
        json={
            'pipeline_id': pipeline_id,
            'running': running
        },
        headers={'Authorization': f'Bearer {creds.id_token}'})
    if response.status_code != 200:
        typer.echo(f'Failed to list jobs: {response.content.decode()}')
        raise typer.Exit(1)
    return response.json()
