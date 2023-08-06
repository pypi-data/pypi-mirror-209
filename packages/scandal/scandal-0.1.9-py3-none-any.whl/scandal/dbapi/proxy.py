import wrapt

from scandal import dbapi


def instance_method(func):
    """Delegates an instance method to a function."""

    def _func(self, *args, **kwargs):
        return func(*args, **kwargs)

    return _func


class ScandalDbApiProxy(wrapt.ObjectProxy):
    connect = instance_method(dbapi.connect)
