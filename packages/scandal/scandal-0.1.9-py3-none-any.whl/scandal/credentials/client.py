import requests

from scandal.credentials.base import Credential
from scandal.credentials.oauth import wellknown

_token_endpoint = wellknown()["token_endpoint"]


class ClientCredential(Credential):
    """A credential that performs an OAuth2 client credentials flow."""

    def __init__(self, client_id: str, client_secret: str):
        self._id = client_id
        self._secret = client_secret

    def get_token(self):
        resp = requests.post(_token_endpoint, auth=(self._id, self._secret))
        if not resp.ok:
            raise Exception(
                f"Client credentials flow failed {resp.status_code}: {resp.text}"
            )
        return resp["access_token"]
