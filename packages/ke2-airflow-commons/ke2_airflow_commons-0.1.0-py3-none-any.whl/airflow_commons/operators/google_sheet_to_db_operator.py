import json
import os
from types import MappingProxyType
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
from airflow.hooks.base import BaseHook
from airflow.models import BaseOperator
from airflow.utils.context import Context
from clickhouse_sqlalchemy import Table, engines, types
from google.oauth2 import service_account
from googleapiclient.discovery import Resource, build
from sqlalchemy import Column, MetaData

from airflow_commons.hooks.clickhouse_hook import ClickHouseHook

DATATYPES = MappingProxyType({
    np.dtype('datetime64[ns]'): types.DateTime64,
    object: types.String,
    str: types.String,
    np.dtype('object_'): types.String,
    np.dtype('int64'): types.Int64,
    int: types.Int64,
    np.dtype('float64'): types.Float64,
    float: types.Float64,
})


class GSheetToClickhouseOperator(BaseOperator):
    """
    Operator that read Google Sheet and insert it into Clickhouse table.

    Create two tables: main table that will be truncated before insert and history table,
        that cpntains two columns: dt and data with json
    """

    TABLE_PATH = '/clickhouse/tables/{{shard}}/marts/{table}'
    S3FS_PATH = '/opt/airflow/s3fs/{{ dag.dag_id }}/{{ run_id }}'

    template_fields = ('sheet', 'table_name', 'headers', 'S3FS_PATH')
    template_ext = ()
    ui_color = '#188038'

    def __init__(
        self,
        *,
        spreadsheet_id: str,
        hook: ClickHouseHook,
        table_name: str,
        sheet: Optional[str] = None,
        recreate: Optional[bool] = None,
        headers: Optional[int] = None,
        google_auth_conn_id: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create operator.

        Args:
            spreadsheet_id: id of Google spreadsheet - it is in url
            hook: hook for connecting to Clickhouse
            table_name: name of clickhouse table
            sheet: name of sheet
            recreate: if true, operator will drop table and create again
            headers: number of row, that contains headers, default 1
            google_auth_conn_id: connection of Google cloud that contains keyfile json
            **kwargs: additional keyword arguments for parent constructor of BaseOperator
        """
        super().__init__(**kwargs)
        self.spreadsheet_id = spreadsheet_id
        self.hook = hook
        self.table_name = table_name
        self.sheet = sheet or 'Лист1'
        self.recreate = recreate or False
        self.headers = headers or 1
        self.google_auth_conn_id = google_auth_conn_id or 'google_sheets_service_account'
        self.history_table_name = '{table_name}_history'.format(table_name=self.table_name)

    @classmethod
    def get_service_sacc(cls, credentials_json: Dict[str, str]) -> Resource:
        """
        Method for getting service account from google api to get spreadsheet.

        Args:
            credentials_json: dict with service_account credentials

        Returns:
            A Resource object with methods for interacting with the service.
        """
        scopes = ['https://www.googleapis.com/auth/spreadsheets']

        creds = service_account.Credentials.from_service_account_info(credentials_json, scopes=scopes)
        return build('sheets', 'v4', credentials=creds)

    def convert_types(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Method for detecting actual types of columns and trying to convert pandas Series to them.

        Methods pd.to_datetime and pd.to_numeric are using.

        Args:
            df: pandas Dataframe

        Returns:
            pandas Dataframe with new types of columns
        """
        self.log.info('start to casting datetime columns')
        for column in df.columns:
            if df[column].dtype == object:
                try:
                    df[column] = pd.to_datetime(df[column])
                except ValueError:
                    self.log.info('cant cast to datetime, skip column')
                    try:
                        df[column] = pd.to_numeric(df[column])
                    except ValueError:
                        self.log.info('cant cast to numeric, skip column')

        return df

    @classmethod
    def ge_ch_type_from_pandas(cls, series: pd.Series) -> types.common.ClickHouseTypeEngine:
        """
        Method for choose type from sqlalchemy engine types.

        Basically, need for detect Date columns.

        Args:
            series: Series of pandas dataframe

        Returns:
            ClickhouseTypeEngine that class of all clickhouse types
        """
        is_np_datetime = series.dtype == np.dtype('datetime64[ns]')

        if is_np_datetime and (series.dt.floor('d') == series).all():
            return types.Date
        return DATATYPES[series.dtype]

    def execute(self, context: Context) -> str:
        """
        Airflow method for running.

        Args:
            context: context of task

        Returns:
            written dataframe in json format of raw with message about unavailability to write it
        """
        credentials_extra = json.loads(BaseHook.get_connection(self.google_auth_conn_id).get_extra())
        credentials = json.loads(credentials_extra.get('extra__google_cloud_platform__keyfile_dict'))
        service_acc = self.get_service_sacc(credentials)
        self.log.info('Got service account')

        self.log.info('trying to get data from spreadsheet')
        # It is set dynamically during service creation.
        spreadsheets_values = service_acc.spreadsheets().values()
        spreadsheet_content = spreadsheets_values.get(
            spreadsheetId=self.spreadsheet_id,
            range=self.sheet,
            valueRenderOption='UNFORMATTED_VALUE',
            dateTimeRenderOption='FORMATTED_STRING',
        )
        spreadsheet_json = spreadsheet_content.execute()
        self.log.info('got data from google spreadsheet')
        df = pd.DataFrame(
            spreadsheet_json['values'][1:],
            columns=spreadsheet_json['values'][self.headers - 1],
        )
        df = self.convert_types(df)
        self.log.info(df.info())

        if not df.empty:
            if not os.path.isdir(self.S3FS_PATH):
                os.makedirs(self.S3FS_PATH)

            table_target_file_path = '{file_path}.csv'.format(
                file_path=os.path.join(self.S3FS_PATH, self.table_name),
            )

            df.to_csv(table_target_file_path)
            self.log.info(
                'File {path} successfully loaded to s3'.format(
                    path=table_target_file_path,
                ),
            )

            history_table_target_file_path = '{file_path}.csv'.format(
                file_path=os.path.join(self.S3FS_PATH, self.history_table_name),
            )

            df.to_csv(history_table_target_file_path)
            self.log.info(
                'File {path} successfully loaded to s3'.format(
                    path=history_table_target_file_path,
                ),
            )

            db_engine = self.hook.get_alchemy_engine()
            db_metadata = MetaData(bind=db_engine)

            columns = [
                Column(
                    'dt',
                    types.DateTime64,
                    server_default=context['execution_date'].to_datetime_string(),
                ),
            ]
            for column in df.columns:
                columns.append(
                    Column(
                        column,
                        self.ge_ch_type_from_pandas(df[column]),
                    ),
                )

            table = Table(
                self.table_name,
                db_metadata,
                *columns,
                engines.ReplicatedMergeTree(
                    table_path=self.TABLE_PATH.format(table=self.table_name),
                    replica_name='{replica}',
                    partition_by=columns[0],
                    order_by=(columns[0],),
                ),
                clickhouse_cluster='{cluster}',
            )

            history_table = Table(
                self.history_table_name,
                db_metadata,
                Column(
                    'dt',
                    types.DateTime64,
                    server_default=context['execution_date'].to_datetime_string(),
                ),
                Column('data', types.String),
                engines.ReplicatedMergeTree(
                    table_path=self.TABLE_PATH.format(table=self.history_table_name),
                    replica_name='{replica}',
                    partition_by=columns[0],
                    order_by=(columns[0],),
                ),
                clickhouse_cluster='{cluster}',
            )

            history_table.create(checkfirst=True)
            self.log.info(
                'Table {history_table_name} successfully created'.format(
                    history_table_name=self.history_table_name,
                ),
            )

            if self.recreate:
                self.log.info('Start recreating table')
                self.hook.run(
                    "DROP TABLE IF EXISTS {table_name} ON CLUSTER '{{cluster}}'".format(
                        table_name=self.table_name,
                    ),
                )
                self.log.info(
                    'Table {table_name} successfully dropped'.format(
                        table_name=self.table_name,
                    ),
                )

                table.create()

                self.log.info(
                    'Table {table_name} was successfully created'.format(
                        table_name=self.table_name,
                    ),
                )
            else:
                table.create(checkfirst=True)
                self.log.info('Start to truncate target table in Clickhouse')
                self.hook.run(
                    "TRUNCATE TABLE IF EXISTS {table_name} ON CLUSTER '{{cluster}}'".format(
                        table_name=self.table_name,
                    ),
                )
                self.log.info(
                    'Table {table_name} successfully truncated'.format(
                        table_name=self.table_name,
                    ),
                )

            # first we need to insert data to main table with current data in dpreadsheet
            self.log.info('Start loading dataframe into Clickhouse')
            rows_inserted = self.hook.insert_dataframe(
                query='INSERT INTO {table_name} ({inserted_values}) VALUES'.format(
                    table_name=self.table_name,
                    inserted_values=','.join(map(str, df.columns)),
                ),
                dataframe=df,
            )
            self.log.info(
                '{rows_inserted} rows inserted into table {table_name}'.format(
                    rows_inserted=rows_inserted,
                    table_name=self.table_name,
                ),
            )

            # then we insert data in history table to know change of data, if we need (json in one column)
            self.log.info('Start loading history into Clickhouse')
            rows_inserted_history = self.hook.insert_dataframe(
                query='INSERT INTO {history_table_name} (dt, data) VALUES'.format(
                    history_table_name=self.history_table_name,
                ),
                dataframe=pd.DataFrame(
                    data={
                        'dt': [
                            context['execution_date'].to_datetime_string(),
                        ],
                        'data': [
                            df.to_json(),
                        ],
                    },
                ),
            )
            self.log.info(
                '{rows_inserted_history} rows inserted into table {history_table_name}'.format(
                    rows_inserted_history=rows_inserted_history,
                    history_table_name=self.history_table_name,
                ),
            )

            return df.to_json()

        self.log.info('There is no data, stop executing')
        return 'No data, no clickhouse table'
