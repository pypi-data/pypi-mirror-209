from typing import Optional

from adbc_driver_flightsql import dbapi as adbc_dbapi

from scandal._config import get_scandal_host
from scandal.credentials import Credential


def connect(
    org: Optional[str] = None,
    project: Optional[str] = None,
    auth_token: Optional[str] = None,
    credential: Optional[Credential] = None,
    scandal_host: str = get_scandal_host(),
    **kwargs,
):
    """Connect to Scandal.

    By default,
        - For interactive users we log in using an OAuth2 device code flow to the user's default organization.
        - For non-interactive users, we pick up creds from a credentials chain.
    """
    if not auth_token:
        if not credential:
            raise Exception("Expected auth_token or credential")
        auth_token = credential.get_token()

    # For now, we send the token as the Basic Auth password. This is because the response headers
    # aren't respected when using Bearer auth: https://github.com/apache/arrow-adbc/issues/584
    db_kwargs = {"username": "scandal", "password": auth_token}

    if project:
        # Connect directly to a project
        db_kwargs[_custom_header("x-fulcrum-project")] = project
    if org:
        db_kwargs[_custom_header("x-fulcrum-org")] = org

    connection = adbc_dbapi.connect(f"grpc+tcp://{scandal_host}", db_kwargs)

    connection.fulcrum_organization = org
    connection.fulcrum_project = project

    return connection


def _custom_header(name: str):
    # Construct the name of a custom header to pass to the Flight SQL server
    return f"adbc.flight.sql.rpc.call_header.{name}"
