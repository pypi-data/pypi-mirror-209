from typing import Optional
import requests
import typer

from launch import constants
from launch.auth import cache
from launch.pipelines import pipeline_helper
from launch.utils import get_account_id, print_response

app = typer.Typer()

EXPAND_HELP = (
    'Show all resources below pipelines (jobs)'
)


@app.command(help='List pipelines for a project')
def list(
    project_id: str = typer.Option(
        ..., help='The project ID to list pipelines for.'),
    expand: bool = typer.Option(False, '--expand', '-e', help=EXPAND_HELP),
    running: bool = constants.EXPAND_RUNNING_OPTION,
    launchflow_server_address: str = constants.
    LAUNCHFLOW_SERVER_ADDRESS_OPTION,
):
    creds = cache.get_user_creds(launchflow_server_address)
    response = pipeline_helper.list_pipelines(
        project_id=project_id,
        launchflow_server_address=launchflow_server_address,
        creds=creds,
        running=running,
        expand=expand)

    print_response('Pipelines', response)


@app.command(help='Create a project in an account')
def create(
    display_name: str = typer.Option(..., help='Display name of the project'),
    project_id: str = typer.Option(
        ..., help='The project ID to create the pipeline in.'),
    account_id: Optional[int] = constants.ACCOUNT_OPTION,
    launchflow_server_address: str = constants.
    LAUNCHFLOW_SERVER_ADDRESS_OPTION,
):
    creds = cache.get_user_creds(launchflow_server_address)
    account_id = get_account_id(account_id)
    response = requests.post(
        f'{launchflow_server_address}/projects/create',
        json={
            'account_id': account_id,
            'project_id': project_id,
            'display_name': display_name
        },
        headers={'Authorization': f'Bearer {creds.id_token}'})
    if response.status_code != 200:
        print(f'Failed to create project: {response.content.decode()}')
        return

    print_response('Pipeline', response)


if __name__ == "__main__":
    app()
