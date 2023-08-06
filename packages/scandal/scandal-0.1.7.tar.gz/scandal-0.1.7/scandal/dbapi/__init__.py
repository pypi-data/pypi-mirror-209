"""Scandal implementation of the Database API Specification v2.0.

.. _Python Database API Specification v2.0 (DB-API):
   https://www.python.org/dev/peps/pep-0249/
"""

# Use the ADBC DBAPI module, except for some Scandal overrides.


from adbc_driver_flightsql import dbapi as adbc_dbapi

from scandal.dbapi.connection import connect

apilevel = "2.0"

__all__ = adbc_dbapi.__all__ + ["connect" ""]
