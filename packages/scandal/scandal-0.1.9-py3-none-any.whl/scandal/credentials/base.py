class Credential:
    """The base class of a Scandal credential."""

    def get_token(self):
        raise NotImplementedError()
