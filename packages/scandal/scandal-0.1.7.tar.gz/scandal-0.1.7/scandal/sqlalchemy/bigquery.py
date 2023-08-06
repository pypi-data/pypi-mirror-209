import pyarrow
import sqlalchemy
from sqlalchemy.engine import URL
from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy_bigquery import BigQueryDialect

from scandal.dbapi.proxy import ScandalDbApiProxy


class BigQueryScandal(BigQueryDialect):
    def create_connect_args(self, url: URL):
        """The Scandal URI format is <dialect>+scandal://<org>/<project>."""
        org = url.host
        project = url.database
        return [], {"org": org, "project": project}

    @classmethod
    def dbapi(cls):
        return ScandalDbApiProxy(BigQueryDialect.dbapi())

    def has_table(self, connection, table_name, schema=None):
        return super(DefaultDialect, self).has_table(connection, table_name, schema)

    def get_columns(self, connection, table_name, schema=None, **kw):
        catalog = connection.connection.fulcrum_project
        schema: pyarrow.Schema = connection.connection.adbc_get_table_schema(
            table_name,
            catalog_filter=catalog,
            db_schema_filter=schema,
        )

        columns = []
        for column in schema:
            column: pyarrow.Field
            columns.append(
                {
                    "name": column.name,
                    "nullable": column.nullable,
                    "type": _get_sqla_column_type(column),
                }
            )

        return columns

    def get_table_comment(self, connection, table_name, schema=None, **kw):
        return super(DefaultDialect, self).get_table_comment(
            connection, table_name, schema=schema, **kw
        )

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        # We have no support for foreign keys
        return []

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        # We have no support for primary keys.
        return {"constrained_columns": []}

    def get_indexes(self, connection, table_name, schema=None, **kw):
        # TODO(ngates): support indexes
        return []

    def get_schema_names(self, connection, **kw):
        """Always use the ADBC metadata API to return schema names."""
        # FIXME(ngates): make use of the info_cache kwargs.
        info = (
            connection.connection.adbc_get_objects(depth="db_schemas")
            .read_all()
            .to_pylist()
        )
        schemas = []
        for catalog in info:
            for db_schema in catalog["catalog_db_schemas"]:
                schemas.append(db_schema["db_schema_name"])
        return schemas

    def get_table_names(self, connection, schema=None, **kw):
        """Always use the ADBC metadata API to return schema names."""
        catalog = connection.connection.fulcrum_project
        info = (
            connection.connection.adbc_get_objects(
                depth="tables",
                catalog_filter=catalog,
                db_schema_filter=schema,
                table_types_filter=["TABLE"],
            )
            .read_all()
            .to_pylist()
        )

        tables = []
        for catalog in info:
            for db_schema in catalog["catalog_db_schemas"]:
                if schema and db_schema["db_schema_name"] != schema:
                    continue
                for db_table in db_schema["db_schema_tables"]:
                    if db_table["table_type"] != "TABLE":
                        continue
                    tables.append(db_table["table_name"])

        return tables

    def get_view_names(self, connection, schema=None, **kw):
        catalog = connection.connection.fulcrum_project
        info = (
            connection.connection.adbc_get_objects(
                depth="tables",
                catalog_filter=catalog,
                db_schema_filter=schema,
                table_types_filter=["VIEW"],
            )
            .read_all()
            .to_pylist()
        )

        views = []
        for catalog in info:
            for db_schema in catalog["catalog_db_schemas"]:
                if schema and db_schema["db_schema_name"] != schema:
                    continue
                for db_table in db_schema["db_schema_tables"]:
                    if db_table["table_type"] != "VIEW":
                        continue
                    views.append(db_table["table_name"])

        return views

    def get_view_definition(self, connection, view_name, schema=None, **kw):
        return super(DefaultDialect, self).get_view_definition(
            connection, view_name, schema, **kw
        )


def _get_sqla_column_type(field: pyarrow.Field):
    _type_map = {
        'date32[day]': sqlalchemy.types.Date,
        "float": sqlalchemy.types.Float,
        "double": sqlalchemy.types.Float,  # Double exists in SQLAlchemy 2.0
        "int32": sqlalchemy.types.Integer,
        "int64": sqlalchemy.types.Integer,
        "string": sqlalchemy.types.String,
        # ... and so on
    }

    try:
        coltype = _type_map[str(field.type)]
    except KeyError:
        sqlalchemy.util.warn(
            "Did not recognize type '%s' of column '%s'" % (field.type, field.name)
        )
        coltype = sqlalchemy.types.NullType
    else:
        # if field.type.endswith("NUMERIC"):
        #     coltype = coltype(precision=field.precision, scale=field.scale)
        # elif field.field_type == "STRING" or field.field_type == "BYTES":
        #     coltype = coltype(field.max_length)
        # elif field.field_type == "RECORD" or field.field_type == "STRUCT":
        #     # FIXME(ngates): probably create our own struct type? Like BigQuery does.
        #     coltype = STRUCT(
        #         *(
        #             (subfield.name, _get_sqla_column_type(subfield))
        #             for subfield in field.fields
        #         )
        #     )
        # else:
        #     coltype = coltype()
        coltype = coltype()

    return coltype
