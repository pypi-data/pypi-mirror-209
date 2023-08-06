"""
Snowflake DataWarehouse Class
"""
from typing import Dict, List, Optional, Tuple

try:
    from typing import Literal  # Only available on 3.8+ directly
except ImportError:
    from typing_extensions import Literal

import pandas as pd

from pyrasgo.api.session import Session
from pyrasgo.storage.dataframe import utils as dfutils
from pyrasgo import errors
from pyrasgo.imports import sf_connector, write_pandas
from pyrasgo.schemas.enums import DataWarehouseType
from pyrasgo.storage.datawarehouse import utils


def unobscure(obscured: bytes) -> bytes:
    import zlib
    from base64 import urlsafe_b64decode

    return zlib.decompress(urlsafe_b64decode(obscured)).decode()


class SnowflakeDataWarehouse(Session):
    """
    Snowflake DataWarehouse Class
    """

    def __init__(self):
        if not sf_connector:
            raise errors.PackageDependencyWarning(
                "Missing a required python package to run Snowflake. "
                "Please download the Snowflake package by running: "
                "pip install pyrasgo[snowflake]"
            )

        _creds = self._dc
        if not _creds:
            raise errors.DWCredentialsWarning("Your user is missing credentials, please contact Rasgo.")
        if self._profile.get("isSso", False):
            raise errors.DWCredentialsWarning("PyRasgo does not support SSO connections.")
        self._connection: sf_connector.SnowflakeConnection = None
        self._credentials: dict = {
            "user": _creds.get("user"),
            "password": unobscure(_creds.get("password")),
            "role": _creds.get("role"),
            "account": _creds.get("account"),
            "database": _creds.get("database"),
            "schema": _creds.get("schema"),
            "warehouse": _creds.get("warehouse"),
            "application": "rasgo",
            "session_parameters": {
                "QUERY_TAG": "rasgo_python_sdk",
                "TIMESTAMP_NTZ_OUTPUT_FORMAT": "YYYY-MM-DD HH24:MI:SS.FF3",
                "TIMESTAMP_OUTPUT_FORMAT": "YYYY-MM-DD HH24:MI:SS.FF3 TZHTZM",
            },
        }
        self.default_database = _creds.get("database")
        self.default_schema = _creds.get("schema")

    @property
    def connection(self) -> 'sf_connector.SnowflakeConnection':
        """
        Returns a connection to Snowflake
        """
        if not self._connection:
            self._connection = sf_connector.connect(**self._credentials)
        return self._connection

    @property
    def dw_type(self) -> str:
        """
        Return the type of data warehouse we're building
        """
        return DataWarehouseType.SNOWFLAKE.value

    def execute_query(
        self,
        query: str,
        params: Optional[dict] = None,
        **kwargs,  # Added to accept & ignore args from other dws
    ):
        """
        Execute a query against this DataWarehouse and return results as a list.

        Args:
            query: SQL string to be executed

        Returns:
            List of Tuples
        """
        return self.connection.cursor().execute(query, params)

    def get_schema(
        self,
        fqtn_or_sql: str,
    ) -> Dict[str, str]:
        """
        Return the schema of a table, view, or select statement

        Params:
        `fqtn_or_sql`: str:
            Either a Fully-qualified table name (database.schema.table)
            or a SQL select statement that will create a view.
        """
        # Check for SQL
        if utils.is_select_statement(fqtn_or_sql):
            query_response = self.connection.cursor().describe(fqtn_or_sql)
            return {row[0]: utils.convert_to_type(row[1], row[4], row[5]) for row in query_response}
        # Otherwise assume fqtn:
        query_response = self.query_into_dict(f"DESC TABLE {fqtn_or_sql}")
        return {row['name']: row['type'] for row in query_response}

    def query_into_dict(
        self,
        query: str,
        params: Optional[dict] = None,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> pd.DataFrame:
        """
        Execute a query against this DataWarehouse and return results as a dictionary.

        Args:
            query: SQL string to be executed

        Returns:
            List of Dicts
        """
        return self.connection.cursor(sf_connector.DictCursor).execute(query, params).fetchall()

    def query_into_dataframe(
        self,
        query: str,
        params: Optional[dict] = None,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> pd.DataFrame:
        """
        Execute a query against this DataWarehouse and return results as a pandas DataFrame.

        Args:
            query: SQL select statement to be executed

        Returns:
            pandas DataFrame
        """
        cur = self.connection.cursor()
        cur.execute(query, params)
        return cur.fetch_pandas_all()

    def list_table_columns(
        self,
        fqtn: str,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> List[Tuple[str, str]]:
        """
        Return a list of columns in a table or view

        Args:
            fqtn: Fully-qualified table name (database.schema.table)

        Returns:
            List of Tuples
        """
        desc_sql = f"DESC TABLE {fqtn}"
        query_response = self.query_into_dict(desc_sql)
        return [(x["name"], x["type"]) for x in query_response]

    def make_select_statement(
        self,
        table_metadata: Dict[str, str],
        filters: Optional[List[str]] = None,
        order_by: Optional[List[str]] = None,
        columns: Optional[List[str]] = None,
        limit: Optional[int] = None,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> str:
        """
        Constructs & returns a SQL select statement

        Args:
            table_metadata: Dict must include fqtn, or database + schema + table
            filters: List of SQL WHERE filters strings to filter on in query
            order_by: List of columns to order by in query
            columns: List of columns to return in the query
            limit: Limit the number of rows returned in the query

        Returns:
            string
        """
        # Get table fqtn
        fqtn = table_metadata.get("fqtn")
        if not fqtn:
            fqtn = "{database}.{schema}.{table}".format(**table_metadata)

        # Create Initial select statement
        columns = ", ".join(columns) if columns else "*"
        query = f"SELECT {columns} FROM {fqtn}"

        # Add filters, orders, and limit if supplied
        if filters:
            query = f"{query} WHERE {' AND '.join(filters)}"
        if order_by:
            query = f"{query} ORDER BY {', '.join(order_by)}"
        if isinstance(limit, int):
            query = f"{query} LIMIT {limit}"
        return query.strip()

    def write_dataframe_to_table(
        self,
        df: pd.DataFrame,
        table_name: str,
        method: Literal["append", "overwrite", "fail"] = "fail",
        **kwargs,  # Added to accept & ignore args from other dws
    ):
        """
        Uploads a pandas DataFrame into this DataWarehouse as a table

        Args:
            df: pandas DataFrame to upload
            table_name: name for the target table in the DataWarehouse
            method: Literal:
                append = if table_name already exists, append to it
                overwrite = if table_name already exists, overwrite it
                fail = if table_name already exists, fail

        Returns:
            None
        """
        # Create the table
        dfutils.cleanse_sql_dataframe(df)
        make_table_query = dfutils.generate_ddl(df=df, table_name=table_name, method=method)
        self.execute_query(make_table_query)
        # Upload the df into it
        write_pandas(
            conn=self.connection,
            df=df,
            table_name=table_name,
            quote_identifiers=False,
        )
