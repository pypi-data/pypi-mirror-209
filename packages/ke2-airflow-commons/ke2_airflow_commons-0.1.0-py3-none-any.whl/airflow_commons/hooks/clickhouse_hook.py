from typing import Any, Dict, Generator, Iterable, List, Optional, Tuple, Union

import pandas as pd
from airflow.hooks.base import BaseHook
from clickhouse_driver import Client
from sqlalchemy import create_engine

_HIDDEN_FIELD_TYPE = List[str]
_RELABELING_TYPE = Dict[str, str]


class ClickHouseHook(BaseHook):
    """Hook for clickhouse database."""

    conn_name_attr = 'clickhouse_conn_id'
    default_conn_name = 'clickhouse_default'
    conn_type = 'clickhouse'
    hook_name = 'ClickHouse'

    def __init__(
        self,
        clickhouse_conn_id: str = default_conn_name,
        database: Optional[str] = None,
        settings: Optional[Dict] = None,
        use_numpy: bool = True,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create hook.

        Args:
            clickhouse_conn_id: Airflow connection id
            database: if database not specified, then hook will use schema from connection
            settings: settings for clickhouse Client, can be none
            use_numpy: setting for using numpy_arrays, default true
            *args: additional arguments for parent constructor of BaseHook
            **kwargs: additional keyword arguments for parent constructor of BaseHook
        """
        super().__init__(*args, **kwargs)
        self.clickhouse_conn_id = clickhouse_conn_id
        self.database = database
        self.settings = settings
        if self.settings:
            self.settings.update(use_numpy=use_numpy)
        else:
            self.settings = {'use_numpy': use_numpy}
        self.conn: Optional[Client] = None

    # Violation disabled because of public API of airflow
    def get_conn(self) -> Client:  # noqa: WPS615
        """
        Airflow method for getting connection from platform.

        Returns:
             New Clickhouse connection
        """
        database = self.get_connection(getattr(self, self.conn_name_attr))

        self.conn = Client(
            host=database.host,
            user=database.login,
            password=database.password,
            database=self.database or database.schema,
            port=database.port,
            settings=self.settings,
        )
        return self.conn

    def get_alchemy_engine(self):
        """
        Method for getting sqlalchemy engine from hook.

        Returns:
             New SQLAlchemy Clickhouse engine
        """
        conn = self.get_connection(getattr(self, self.conn_name_attr))
        conn.port = 8123
        uri = conn.get_uri()

        self.log.info(uri)

        return create_engine(uri)

    # TODO move to api-db 2.0 and add fetchall method in get_records
    # TODO: How is responsible to finish this TODO?
    def get_records(self, sql, parameters=None):
        raise NotImplementedError()

    # TODO move to api-db 2.0 and add fetch_one method in get_records
    # TODO: How is responsible to finish this TODO?
    def get_first(self, sql, parameters=None):
        raise NotImplementedError()

    def get_pandas_df(
        self,
        sql: str,
        params: Union[None, Dict, List, Tuple, Generator] = None,
        query_id: Optional[str] = None,
        external_tables: Optional[List[Dict]] = None,
    ) -> pd.DataFrame:
        """
        Executes the sql and returns a pandas dataframe.

        Args:
            sql: the sql statement to be executed (str) or a list of sql statements to execute
            params: The parameters to render the SQL query with
            query_id: the query identifier. It will be generated in case of absence. String but real type is uuid
            external_tables: external tables6 that can be used in query

        Returns:
            Pandas Dataframe after executing sql in ClickHouse
        """
        with self.get_conn() as conn:
            sql_result = conn.query_dataframe(
                sql,
                params=params,
                query_id=query_id,
                external_tables=external_tables,
            )

        return sql_result

    def run(
        self,
        sql: str,
        params: Union[None, Dict, List, Tuple, Generator] = None,
        query_id: Optional[str] = None,
        external_tables: Optional[List[Dict]] = None,
    ) -> Any:
        """
        Runs a command or a list of commands.

        Pass a list of sql statements to the sql parameter to get them to execute sequentially

        Args:
            sql: the sql statement to be executed (str) or a list of sql statements to execute
            params: The parameters to render the SQL query with
            query_id: the query identifier. It will be generated in case of absence. String but real type is uuid
            external_tables: external tables6 that can be used in query

        Returns:
            List of tuples or list of np.arrays after executing sql in ClickHouse
        """
        with self.get_conn() as conn:
            sql_result = conn.execute(
                sql,
                params=params,
                query_id=query_id,
                external_tables=external_tables,
            )

        return sql_result

    # TODO add generating insert query to specified table
    # TODO: How is responsible to finish this TODO?
    def insert_rows(
        self,
        table: str,
        rows: Iterable[Tuple],
        target_fields: Optional[Iterable[str]] = None,
    ) -> Any:
        raise NotImplementedError()

    def insert_dataframe(
        self,
        query: str,
        dataframe: pd.DataFrame,
        external_tables: Optional[List[Dict]] = None,
        query_id: Optional[str] = None,
    ) -> Any:
        with self.get_conn() as conn:
            sql_result = conn.insert_dataframe(
                query=query,
                dataframe=dataframe,
                external_tables=external_tables,
                query_id=query_id,
            )

        return sql_result

    @classmethod
    def get_ui_field_behaviour(cls) -> Dict[str, Union[_HIDDEN_FIELD_TYPE, _RELABELING_TYPE]]:
        """
        Airflow method for overriding connection UI.

        Returns:
            Dictionary with custom behaviour for Connection in UI
        """
        return {
            'hidden_fields': ['extra'],
            'relabeling': {'schema': 'Database'},
        }
