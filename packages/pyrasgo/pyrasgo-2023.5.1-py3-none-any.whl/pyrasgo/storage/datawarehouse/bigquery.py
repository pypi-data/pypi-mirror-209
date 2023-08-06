"""
BigQuery DataWarehouse Class
"""
from typing import Dict, List, Optional, Tuple

try:
    from typing import Literal  # Only available on 3.8+ directly
except ImportError:
    from typing_extensions import Literal

import pandas as pd

from pyrasgo.api.session import Session
from pyrasgo import errors
from pyrasgo.imports import bq, gcp_exc, gcp_flow, gcp_svc
from pyrasgo.schemas.enums import DataWarehouseType
from pyrasgo.storage.dataframe import utils as dfutils
from pyrasgo.storage.datawarehouse import utils as dwutils
from pyrasgo.utils import naming


class BigQueryDataWarehouse(Session):
    """
    BigQuery DataWarehouse Class
    """

    def __init__(self):
        if bq is None:
            raise errors.PackageDependencyWarning(
                "Missing a required python package to run BigQuery. "
                "Please download the BigQuery package by running: "
                "pip install pyrasgo[bigquery]"
            )
        _creds = self._dc
        if not _creds:
            raise errors.DWCredentialsWarning("Your user is missing credentials, please contact Rasgo.")
        if self._profile.get("isSso", False):
            raise errors.DWCredentialsWarning("PyRasgo does not support SSO connections.")
        self._connection: bq.Client = None
        self._credentials: bq.Credentials = None
        self._key = _creds.get("json_key")
        self.default_database = _creds.get("project")
        self.default_schema = _creds.get("dataset")

    @property
    def connection(self) -> 'bq.Client':
        """
        Returns a connection to the BQ Client
        """
        if self._connection:
            return self._connection
        if not self._credentials:
            self.set_credentials()
        return bq.Client(credentials=self._credentials, project=self.default_database)

    @property
    def dw_type(self) -> str:
        """
        Return the type of data warehouse we're building
        """
        return DataWarehouseType.BIGQUERY.value

    def set_credentials(self):
        """
        Sets the credentials for this BQ Class instance
        """
        # Try to auth as a user first, then try as a service account if that fails
        try:
            self._credentials = self._get_appflow_credentials()
        # If this is a service account, BQ will raise:
        # ValueError: Client secrets must be for a web or installed app.
        except ValueError:
            self._credentials = self._get_service_account_credentials()

    def _get_service_account_credentials(self):
        """
        Google stuff
        """
        return gcp_svc.Credentials.from_service_account_info(
            self._key,
            scopes=[
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/drive",
            ],
        )

    def _get_appflow_credentials(self):
        """
        Google stuff
        """
        appflow = gcp_flow.InstalledAppFlow.from_client_config(
            self._key,
            scopes=[
                "https://www.googleapis.com/auth/bigquery",
                "https://www.googleapis.com/auth/drive",
            ],
        )
        appflow.run_local_server()
        # appflow.run_console()
        return appflow.credentials

    def _job_config(self):
        """
        Returns a basic job config to run queries in default project & dataset
        """
        return bq.QueryJobConfig(default_dataset=f"{self.default_database}.{self.default_schema}")

    def execute_query(
        self,
        query: str,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> List[Tuple]:
        """
        Execute a query against this DataWarehouse and return results as a list.

        Args:
            query: SQL string to be executed

        Returns:
            List of Tuples
        """
        return list(self.connection.query(query, job_config=self._job_config()).result())

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
        if dwutils.is_select_statement(fqtn_or_sql):
            query_job = self.connection.query(
                query=fqtn_or_sql,
                job_config=bq.QueryJobConfig(dry_run=True),
            )
            schema = query_job._properties['statistics']['query']['schema']['fields']
            return {schema_field['name']: schema_field['type'] for schema_field in schema}
        # Otherwise assume fqtn:
        table = self.connection.get_table(fqtn_or_sql)
        schema = table.schema
        return {schema_field.name: schema_field.field_type for schema_field in schema}

    def query_into_dict(
        self,
        query: str,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> List[Dict]:
        """
        Execute a query against this DataWarehouse and return results as a dictionary.

        Args:
            query: SQL string to be executed

        Returns:
            List of Dicts
        """
        return list(self.connection.query(query, job_config=self._job_config()).result())

    def query_into_dataframe(
        self,
        query: str,
        **kwargs,  # Added to accept & ignore args from other dws
    ) -> pd.DataFrame:
        """
        Execute a query against this DataWarehouse and return results as a pandas DataFrame.

        Args:
            query: SQL select statement to be executed

        Returns:
            pandas DataFrame
        """
        return self.connection.query(query, job_config=self._job_config()).result().to_dataframe()

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
        table = self.connection.get_table(fqtn)
        return [(x.name, x.field_type) for x in table.schema]

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
        fqtn = table_metadata.get('fqtn')
        if fqtn:
            fqtn = naming.quote_fqtn(fqtn, dw_type=self.dw_type)
        if not fqtn:
            fqtn = naming.make_fqtn(
                database=table_metadata.get('database'),
                schema=table_metadata.get('schema'),
                table=table_metadata.get('table'),
            )

        # Create Initial select statement
        columns = ', '.join(columns) if columns else '*'
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
    ) -> None:
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
        # Upload the df into it
        dfutils.cleanse_sql_dataframe(df)
        write_disposition = "WRITE_EMPTY"
        if method == "append":
            write_disposition = "WRITE_APPEND"
        if method == "overwrite":
            write_disposition = "WRITE_TRUNCATE"
        job_config = bq.LoadJobConfig(write_disposition=write_disposition)
        self.connection.load_table_from_dataframe(df, table_name, job_config=job_config).result()
