from typing import Any, Dict

import requests
import typer

from launch.pipelines import pipeline_helper


def list_projects(
    account_id: str,
    launchflow_server_address: str,
    expand: bool,
    running: bool,
    creds,
) -> Dict[str, Any]:
    response = requests.post(
        f'{launchflow_server_address}/projects/list',
        json={'account_id': account_id},
        headers={'Authorization': f'Bearer {creds.id_token}'})
    if response.status_code != 200:
        typer.echo(f'Failed to list projects: {response.content.decode()}')
        raise typer.Exit(1)

    response_json = response.json()
    if expand:
        expanded_response = []
        projects = response_json['projects']
        for project in projects:
            pipelines = pipeline_helper.list_pipelines(
                project_id=project['id'],
                launchflow_server_address=launchflow_server_address,
                expand=True,
                running=running,
                creds=creds)
            project['pipelines'] = pipelines['pipelines']
            expanded_response.append(project)
        response_json = {'projects': expanded_response}
    return response_json
