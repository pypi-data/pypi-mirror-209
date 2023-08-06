import json
import os.path

CLIENT_IDS = {
    "scandal-py": os.environ.get(
        "SCANDAL_CLIENT_ID", "a358618b-92ea-411f-b8f1-99be0f557da0"
    )
}

CREDS_FILE = os.path.expanduser("~/.config/fulcrum/local.creds.json")
_IS_LOCAL_DEV = os.path.exists(CREDS_FILE)


def get_client_id(service: str = "scandal-py"):
    """For local development, we read the client-id out of a file on disk. Otherwise, it's hard-coded."""
    if _IS_LOCAL_DEV:
        with open(CREDS_FILE) as f:
            creds = json.load(f)
            return creds["clientCreds"][service]["clientId"]
    return CLIENT_IDS[service]


def get_scandal_host():
    if _IS_LOCAL_DEV:
        return "localhost:8443"
    return os.environ.get("SCANDAL_HOST", "crowbar.fly.dev:443")


def get_archimedes_url() -> str:
    if _IS_LOCAL_DEV:
        return "http://localhost:3000"
    return os.environ.get("ARCHIMEDES_URL", "https://archimedes-dev.fly.dev")
