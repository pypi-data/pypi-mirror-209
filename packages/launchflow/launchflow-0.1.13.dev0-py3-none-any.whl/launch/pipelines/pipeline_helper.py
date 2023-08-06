from typing import Any, Dict

import requests
import typer

from launch.jobs import jobs_helper


def list_pipelines(
    project_id: str,
    launchflow_server_address: str,
    expand: bool,
    running: bool,
    creds,
) -> Dict[str, Any]:
    response = requests.post(
        f'{launchflow_server_address}/pipelines/list',
        json={'project_id': project_id},
        headers={'Authorization': f'Bearer {creds.id_token}'})
    if response.status_code != 200:
        typer.echo(f'Failed to list pipelines: {response.content.decode()}')
        raise typer.Exit(1)

    response_json = response.json()
    if expand:
        expanded_response = []
        pipelines = response_json['pipelines']
        for pipeline in pipelines:
            jobs = jobs_helper.list_jobs(
                pipeline_id=pipeline['id'],
                running=running,
                launchflow_server_address=launchflow_server_address,
                creds=creds)
            pipeline['jobs'] = jobs['jobs']
            expanded_response.append(pipeline)
        response_json = {'pipelines': expanded_response}
    return response_json
