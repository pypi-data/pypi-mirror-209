class Credential:
    """The base class of a Scandal credential."""

    def get_token(self):
        raise NotImplementedError()


class TokenCredential(Credential):
    def __init__(self, token: str):
        self._token = token

    def get_token(self):
        return self._token


class DeviceCredential(Credential):
    """A credential that triggers a Fulcrum OAuth2 Device Authorization flow."""

    def get_token(self):
        pass


class ClientCredential(Credential):
    """A credential that performs an OAuth2 client credentials flow."""
