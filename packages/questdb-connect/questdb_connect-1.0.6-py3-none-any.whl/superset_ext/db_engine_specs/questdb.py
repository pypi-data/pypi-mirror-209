#
#     ___                  _   ____  ____
#    / _ \ _   _  ___  ___| |_|  _ \| __ )
#   | | | | | | |/ _ \/ __| __| | | |  _ \
#   | |_| | |_| |  __/\__ \ |_| |_| | |_) |
#    \__\_\\__,_|\___||___/\__|____/|____/
#
#  Copyright (c) 2014-2019 Appsicle
#  Copyright (c) 2019-2023 QuestDB
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import re
from datetime import datetime
from typing import Any, Dict, List, Optional

from flask_babel import gettext as __
from marshmallow import Schema, fields
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.sql import text
from sqlalchemy.types import TypeEngine
from superset.db_engine_specs.base import (
    BaseEngineSpec,
    BasicParametersMixin,
    BasicParametersType,
)
from superset.utils import core as utils
from superset.utils.core import GenericDataType

from questdb_connect import remove_public_schema
from questdb_connect import types as questdb_types
from questdb_connect.dialect import connection_uri
from questdb_connect.function_names import FUNCTION_NAMES

# Apache Superset requires a Python DB-API database driver, and a SQLAlchemy dialect
# https://superset.apache.org/docs/databases/installing-database-drivers
# https://preset.io/blog/building-database-connector/
# https://preset.io/blog/improving-apache-superset-integration-database-sqlalchemy/


class QDBParametersSchema(Schema):
    username = fields.String(allow_none=True, description=__("user"))
    password = fields.String(allow_none=True, description=__("password"))
    host = fields.String(required=True, description=__("host"))
    port = fields.Integer(allow_none=True, description=__("port"))
    database = fields.String(allow_none=True, description=__("database"))


class QDBEngineSpec(BaseEngineSpec, BasicParametersMixin):
    engine = "questdb"
    engine_name = "QuestDB Connect"
    default_driver = "psycopg2"
    encryption_parameters = {"sslmode": "prefer"}
    sqlalchemy_uri_placeholder = "questdb://user:password@host:port/database"
    parameters_schema = QDBParametersSchema()
    time_groupby_inline = False
    allows_hidden_cc_in_orderby = True
    time_secondary_columns = True
    try_remove_schema_from_table_name = True
    max_column_name_length = 120
    supports_dynamic_schema = False
    top_keywords = {}
    # https://en.wikipedia.org/wiki/ISO_8601#Durations
    # https://questdb.io/docs/reference/function/date-time/#date_trunc
    _time_grain_expressions = {
        None: "{col}",
        "PT1S": "date_trunc('second', {col})",
        "PT1M": "date_trunc('minute', {col})",
        "PT1H": "date_trunc('hour', {col})",
        "P1D": "date_trunc('day', {col})",
        "P1W": "date_trunc('week', {col})",
        "P1M": "date_trunc('month', {col})",
        "P1Y": "date_trunc('year', {col})",
        "P3M": "date_trunc('quarter', {col})",
    }
    column_type_mappings = (
        (
            re.compile("^LONG256", re.IGNORECASE),
            questdb_types.Long256,
            GenericDataType.STRING,
        ),
        (
            re.compile("^BOOLEAN", re.IGNORECASE),
            questdb_types.Boolean,
            GenericDataType.BOOLEAN,
        ),
        (
            re.compile("^BYTE", re.IGNORECASE),
            questdb_types.Byte,
            GenericDataType.NUMERIC,
        ),
        (
            re.compile("^SHORT", re.IGNORECASE),
            questdb_types.Short,
            GenericDataType.NUMERIC,
        ),
        (re.compile("^INT", re.IGNORECASE), questdb_types.Int, GenericDataType.NUMERIC),
        (
            re.compile("^LONG", re.IGNORECASE),
            questdb_types.Long,
            GenericDataType.NUMERIC,
        ),
        (
            re.compile("^FLOAT", re.IGNORECASE),
            questdb_types.Float,
            GenericDataType.NUMERIC,
        ),
        (
            re.compile("^DOUBLE'", re.IGNORECASE),
            questdb_types.Double,
            GenericDataType.NUMERIC,
        ),
        (
            re.compile("^SYMBOL", re.IGNORECASE),
            questdb_types.Symbol,
            GenericDataType.STRING,
        ),
        (
            re.compile("^STRING", re.IGNORECASE),
            questdb_types.String,
            GenericDataType.STRING,
        ),
        (
            re.compile("^UUID", re.IGNORECASE),
            questdb_types.UUID,
            GenericDataType.STRING,
        ),
        (
            re.compile("^CHAR", re.IGNORECASE),
            questdb_types.Char,
            GenericDataType.STRING,
        ),
        (
            re.compile("^TIMESTAMP", re.IGNORECASE),
            questdb_types.Timestamp,
            GenericDataType.TEMPORAL,
        ),
        (
            re.compile("^DATE", re.IGNORECASE),
            questdb_types.Date,
            GenericDataType.TEMPORAL,
        ),
        (
            re.compile(r"^GEOHASH\(\d+[b|c]\)", re.IGNORECASE),
            questdb_types.GeohashLong,
            GenericDataType.STRING,
        ),
    )

    @classmethod
    def build_sqlalchemy_uri(
        cls,
        parameters: BasicParametersType,
        encrypted_extra: Optional[Dict[str, str]] = None,
    ) -> str:
        return connection_uri(
            parameters.get("host"),
            parameters.get("port"),
            parameters.get("username"),
            parameters.get("password"),
            parameters.get("database"),
        )

    @classmethod
    def get_default_schema_for_query(cls, database, query) -> Optional[str]:
        return "public"

    @classmethod
    def get_text_clause(cls, clause):
        """SQLAlchemy wrapper to ensure text clauses are escaped properly
        :param clause: string clause with potentially unescaped characters
        :return: text clause with escaped characters
        """
        if cls.allows_escaped_colons:
            clause = clause.replace(":", "\\:")
        return text(remove_public_schema(clause))

    @classmethod
    def epoch_to_dttm(cls) -> str:
        """SQL expression that converts epoch (seconds) to datetime that can be used
        in a query. The reference column should be denoted as `{col}` in the return
        expression, e.g. "FROM_UNIXTIME({col})"
        :return: SQL Expression
        """
        return "{col} * 1000000"

    @classmethod
    def convert_dttm(
        cls, target_type: str, dttm: datetime, *_args, **_kwargs
    ) -> Optional[str]:
        """Convert a Python `datetime` object to a SQL expression.
        :param target_type: The target type of expression
        :param dttm: The datetime object
        :return: The SQL expression
        """
        type_u = target_type.upper()
        if type_u == "DATE":
            return f"TO_DATE('{dttm.date().isoformat()}', 'YYYY-MM-DD')"
        if type_u in ("DATETIME", "TIMESTAMP"):
            dttm_formatted = dttm.isoformat(sep="T", timespec="microseconds")
            return f"TO_TIMESTAMP('{dttm_formatted}', 'yyyy-MM-ddTHH:mm:ss.SSSUUUZ')"
        return None

    @classmethod
    def get_datatype(cls, type_code: Any) -> Optional[str]:
        """Change column type code from cursor description to string representation.
        :param type_code: Type code from cursor description
        :return: String representation of type code
        """
        if type_code and isinstance(type_code, str):
            return type_code.upper()
        return str(type_code)

    @classmethod
    def get_column_spec(
        cls,
        native_type: Optional[str],
        db_extra: Optional[Dict[str, Any]] = None,
        source: utils.ColumnTypeSource = utils.ColumnTypeSource.GET_TABLE,
    ) -> Optional[utils.ColumnSpec]:
        """Get generic type related specs regarding a native column type.
        :param native_type: Native database type
        :param db_extra: The database extra object
        :param source: Type coming from the database table or cursor description
        :return: ColumnSpec object
        """
        sqla_type = questdb_types.resolve_type_from_name(native_type)
        if not sqla_type:
            return BaseEngineSpec.get_column_spec(native_type, db_extra, source)
        name_u = sqla_type.__visit_name__
        generic_type = None
        if name_u == "BOOLEAN":
            generic_type = GenericDataType.BOOLEAN
        elif name_u in ("BYTE", "SHORT", "INT", "LONG", "FLOAT", "DOUBLE"):
            generic_type = GenericDataType.NUMERIC
        elif name_u in ("SYMBOL", "STRING", "CHAR", "LONG256", "UUID"):
            generic_type = GenericDataType.STRING
        elif name_u in ("DATE", "TIMESTAMP"):
            generic_type = GenericDataType.TEMPORAL
        elif "GEOHASH" in name_u and "(" in name_u and ")" in name_u:
            generic_type = GenericDataType.STRING
        return utils.ColumnSpec(
            sqla_type, generic_type, generic_type == GenericDataType.TEMPORAL
        )

    @classmethod
    def get_sqla_column_type(
        cls,
        native_type: Optional[str],
        db_extra: Optional[Dict[str, Any]] = None,
        source: utils.ColumnTypeSource = utils.ColumnTypeSource.GET_TABLE,
    ) -> Optional[TypeEngine]:
        """Converts native database type to sqlalchemy column type.
        :param native_type: Native database type
        :param db_extra: The database extra object
        :param source: Type coming from the database table or cursor description
        :return: ColumnSpec object
        """
        return questdb_types.resolve_type_from_name(native_type).impl

    @classmethod
    def column_datatype_to_string(
        cls,
        sqla_column_type: TypeEngine,
        dialect: Dialect,
    ) -> str:
        """Convert sqlalchemy column type to string representation.
        By default, removes collation and character encoding info to avoid
        unnecessarily long datatypes.
        :param sqla_column_type: SqlAlchemy column type
        :param dialect: Sqlalchemy dialect
        :return: Compiled column type
        """
        return sqla_column_type.copy().compile(dialect=dialect)

    @classmethod
    def select_star(
        cls,
        database,
        table_name: str,
        engine,
        schema: Optional[str] = None,
        limit: int = 100,
        show_cols: bool = False,
        indent: bool = True,
        latest_partition: bool = True,
        cols: Optional[List[Dict[str, Any]]] = None,
    ) -> str:
        """Generate a "SELECT * from table_name" query with appropriate limit.
        :param database: Database instance
        :param table_name: Table name, unquoted
        :param engine: SqlAlchemy Engine instance
        :param schema: Schema, unquoted
        :param limit: limit to impose on query
        :param show_cols: Show columns in query; otherwise use "*"
        :param indent: Add indentation to query
        :param latest_partition: Only query the latest partition
        :param cols: Columns to include in query
        :return: SQL query
        """
        return super().select_star(
            database,
            table_name,
            engine,
            None,
            limit,
            show_cols,
            indent,
            latest_partition,
            cols,
        )

    @classmethod
    def get_function_names(cls, database) -> List[str]:
        """Get a list of function names that are able to be called on the database.
        Used for SQL Lab autocomplete.
        :param database: The database to get functions for
        :return: A list of function names usable in the database
        """
        return FUNCTION_NAMES

    @classmethod
    def get_allow_cost_estimate(cls, extra: Dict[str, Any]) -> bool:
        return False

    @classmethod
    def get_view_names(cls, database, inspector, schema: Optional[str]):
        return []
