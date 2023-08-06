import functools
from typing import Optional

import requests

from scandal._config import get_archimedes_url


@functools.cache
def wellknown(issuer: Optional[str] = None):
    if not issuer:
        issuer = get_archimedes_url()
    if not issuer.endswith("/"):
        issuer = issuer + "/"
    return requests.get(f"{issuer}.well-known/openid-configuration").json()


def check_token(token: str) -> bool:
    """Check the validity of a token.

    We could do this locally for JWTs, but for opaque tokens we need to hit the server.
    For now, we will just always hit the userinfo endpoint.
    """
    return requests.get(
        wellknown()["userinfo_endpoint"], headers={"Authorization": f"Bearer {token}"}
    ).ok
