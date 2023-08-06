import time
import webbrowser

import jwt
import keyring
import requests

from scandal._config import get_archimedes_url, get_client_id

CLIENT_IDS = {"scandal-py": "a358618b-92ea-411f-b8f1-99be0f557da0"}

SERVICE = "scandal-py"
GRANT_TYPE = "urn:ietf:params:oauth:grant-type:device_code"

# Refresh token 5 minutes before it expires
EXPIRY_WINDOW = 5 * 60


def auth_user():
    # _try_delete_password(SERVICE, "access_token")
    # _try_delete_password(SERVICE, "refresh_token")
    client_id = get_client_id(SERVICE)

    access_token = keyring.get_password(SERVICE, "access_token")
    refresh_token = keyring.get_password(SERVICE, "refresh_token")

    if access_token:
        access_token_decoded = jwt.decode(
            access_token, options={"verify_signature": False}
        )

        if access_token_decoded.get("exp") > (time.time() - EXPIRY_WINDOW):
            return access_token

        if refresh_token:
            refresh_resp = requests.post(
                f"{get_archimedes_url()}/oauth/token",
                data={
                    "client_id": client_id,
                    "grant_type": GRANT_TYPE,
                    "refresh_token": refresh_token,
                },
            )
            if not refresh_resp.ok:
                print("Failed to refresh Scandal token.")
                keyring.delete_password(SERVICE, "access_token")
                keyring.delete_password(SERVICE, "refresh_token")
                return auth_user()

    resp = requests.post(
        f"{get_archimedes_url()}/oauth/device",
        data={
            "client_id": client_id,
            # TODO(ngates): should this be scandal instead?
            "audience": "https://scandal.fulcrum.so",
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
            f"{get_archimedes_url()}/oauth/token",
            data={
                "client_id": client_id,
                "grant_type": GRANT_TYPE,
                "device_code": code_resp["device_code"],
            },
        )

        if token_resp.ok:
            token_resp = token_resp.json()
            access_token = token_resp["access_token"]
            refresh_token = token_resp.get("refresh_token", "refresh")

            keyring.set_password(SERVICE, "access_token", access_token)
            keyring.set_password(SERVICE, "refresh_token", refresh_token)

            return access_token

        if token_resp.json()["error"] != "authorization_pending":
            token_resp.raise_for_status()

    raise Exception("Timed out waiting for authorization. Please try again")


def _try_delete_password(service: str, username: str):
    try:
        keyring.delete_password(service, username)
    except Exception:
        pass
