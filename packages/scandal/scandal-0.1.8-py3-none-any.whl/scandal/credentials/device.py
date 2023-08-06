import time
import webbrowser

import keyring
import requests

from scandal.credentials.base import Credential
from scandal.credentials.oauth import check_token, wellknown

_device_endpoint = wellknown()["device_authorization_endpoint"]
_token_endpoint = wellknown()["token_endpoint"]
# Usually, device flows should use the token_endpoint. But our flow is hosted on a different server for now.
_device_token_endpoint = wellknown().get("device_token_endpoint", _token_endpoint)


class DeviceCredential(Credential):
    """A credential that triggers a Fulcrum OAuth2 Device Authorization flow."""

    def __init__(self, client_id: str):
        self._client_id = client_id
        self._client_name = f"scandal_{client_id}"

    def get_token(self):
        access_token = keyring.get_password(self._client_name, "access_token")
        refresh_token = keyring.get_password(self._client_name, "refresh_token")

        if access_token:
            if check_token(access_token):
                return access_token

        if refresh_token:
            refresh_resp = requests.post(
                _token_endpoint,
                data={
                    "client_id": self._client_id,
                    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                    "refresh_token": refresh_token,
                },
            )
            if not refresh_resp.ok:
                print("Failed to refresh Scandal token.")
                keyring.delete_password(self._client_name, "access_token")
                keyring.delete_password(self._client_name, "refresh_token")
                return self.get_token()

        resp = requests.post(
            _device_endpoint,
            data={
                "client_id": self._client_id,
                "scope": "offline_access",
            },
        )
        if not resp.ok:
            raise Exception(f"{resp.status_code}: {resp.text}")
        code_resp = resp.json()

        expiry = time.time() + code_resp["expires_in"]

        print("Enter the following code at this URL: " + code_resp["verification_uri"])
        print(code_resp["user_code"])
        webbrowser.open(code_resp["verification_uri_complete"])

        while time.time() < expiry:
            time.sleep(code_resp["interval"])
            token_resp = requests.post(
                _device_token_endpoint,
                data={
                    "client_id": self._client_id,
                    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                    "device_code": code_resp["device_code"],
                },
            )

            if token_resp.ok:
                token_resp = token_resp.json()
                access_token = token_resp["access_token"]
                keyring.set_password(self._client_name, "access_token", access_token)

                refresh_token = token_resp.get("refresh_token", "refresh")
                if refresh_token:
                    keyring.set_password(
                        self._client_name, "refresh_token", refresh_token
                    )

                return access_token

            if token_resp.json()["error"] != "authorization_pending":
                token_resp.raise_for_status()

        raise Exception("Timed out waiting for authorization. Please try again")


def _try_delete_password(service: str, username: str):
    try:
        keyring.delete_password(service, username)
    except Exception:
        pass
