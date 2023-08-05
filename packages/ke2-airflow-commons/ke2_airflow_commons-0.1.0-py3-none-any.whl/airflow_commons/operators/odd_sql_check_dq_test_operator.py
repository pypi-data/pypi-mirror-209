import traceback
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Iterable, List, Optional, Union

import pandas as pd
from airflow.models import BaseOperator, Variable
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.context import Context as AirflowContext
from odd_models.models import (
    DataEntity,
    DataEntityType,
    DataQualityTest,
    DataQualityTestExpectation,
    DataQualityTestRun,
    LinkedUrl,
    QualityRunStatus,
)

from airflow_commons.hooks.clickhouse_hook import ClickHouseHook
from airflow_commons.hooks.odd_hook import ODDHook


class DQTestStatus(Enum):
    SUCCESS = QualityRunStatus.SUCCESS
    FAILED = QualityRunStatus.FAILED
    BROKEN = QualityRunStatus.BROKEN


@dataclass
class DQTestResult:
    suite: str
    name: str
    status: str
    reason: Optional[str]
    expected: Optional[Dict]
    actual: Optional[Dict]


class DQTest:
    """
    Class for data quality test.

    To use this class, you should create own class and inherit from this with own
        test_data method implementation
    """

    def __init__(self, suite: str, name: str) -> None:
        """
        Base constructor to create DQTest.

        Args:
            suite: name of suite of tests
            name: name of dq test
        """
        self.suite = suite
        self.name = name

    def test_data(self, df: pd.DataFrame, context: AirflowContext) -> DQTestResult:
        raise NotImplementedError()


def get_hook(db_conn_type: str, conn_id: str) -> Union[ClickHouseHook, PostgresHook]:
    if db_conn_type == 'clickhouse':
        return ClickHouseHook(clickhouse_conn_id=conn_id)

    return PostgresHook(postgres_conn_id=conn_id)


DQ_TEST_TEMPLATE = """
    Data quality test:
    suite_name - {suite_name}
    dataset_list - {dataset_list}
    linked_url_list - {linked_url_list}
    expectation - {expectation}
"""

DQ_TEST_ENTITY_TEMPLATE = """
    Data quality data entity:
    name - {name}
    dataset_list - {dataset_list}
    linked_url_list - {linked_url_list}
    expectation - {expectation}
"""

DQ_TEST_RUN_TEMPLATE = """
    Data quality test run:
    data_quality_test_oddrn - {data_quality_test_oddrn}
    start_time - {start_time}
    end_time - {end_time}
    status_reason - {status_reason}
    status - {status}
"""

DQ_TEST_RUN_ENTITY_TEMPLATE = """
    Data quality test run:
    data_quality_test_run - {data_quality_test_run}
    name - {name}
    oddrn - {oddrn}
    type - {type}
"""


class ODDSQLCheckDQTestOperator(BaseOperator):
    """
    Operator for creating Data Quality tests in ODD.

    Work with Postgres and Clickhouse only
    """

    template_fields = (
        'sql',
        'dataset_oddrn',
    )
    template_ext = ('.sql',)

    def __init__(
        self,
        dataset_oddrn: str,
        extract_sql: str,
        db_conn_id: str,
        dq_tests: List[DQTest],
        odd_conn_id: Optional[str] = None,
        db_conn_type: Optional[str] = None,  # TODO: infer this parameter from connection. Do we have ticket for that?
        linked_url_list: Optional[List[LinkedUrl]] = None,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create operator.

        Args:
            dataset_oddrn: oddrn of dataset in odd, that attached to dq test
            extract_sql: sql query to execute or path to sql file, executes in database of db_conn_type argument
            db_conn_id: db connection id in airflow
            dq_tests: list of DQTest to create dq tests in odd
            odd_conn_id: odd connection id in airflow
            db_conn_type: type of database, default is clickhouse
            linked_url_list: list of linked urls
            *args: additional arguments for parent constructor of BaseOperator
            **kwargs: additional keyword arguments for parent constructor of BaseOperator
        """
        super().__init__(*args, **kwargs)
        self.dataset_oddrn = dataset_oddrn
        self.sql = extract_sql
        self.db_conn_id = db_conn_id
        self.dq_tests = dq_tests
        self.odd_conn_id = odd_conn_id or 'odd'
        self.db_conn_type = db_conn_type or 'clickhouse'
        self.linked_url_list = linked_url_list  # TODO: what is it?
        self.odd_hook = ODDHook(self.odd_conn_id)
        self.airflow_oddrn = Variable.get('airflow_oddrn')

    def execute(self, context: AirflowContext) -> None:
        """
        Execute method of airflow operator.

        Execute sql, then run all tests of DQTest classes and create
            data entities in odd based on DQTestResult instances

        Args:
            context: Airflow context with DAG and task metadata

        Raises:
            FileNotFoundError: in case of absence of sql file
        """
        hook = get_hook(self.db_conn_type, self.db_conn_id)
        if self.sql[-4:] == '.sql':
            try:
                df = self._try_to_open_and_execute(hook)
            except FileNotFoundError as error:
                self.log.error(
                    'Error {error}: path to sql file no found'.format(
                        error=error,
                    ),
                )
                raise error
        else:
            self.log.info('Start to execute sql query:\n{query}'.format(query=self.sql))
            df = hook.get_pandas_df(sql=self.sql)

        self.log.info('Dataframe structure - {structure}'.format(structure=df.info()))
        self.log.info('Dataframe first 5 rows - {first_five_rows}'.format(first_five_rows=df.head()))

        dqt_results: List[DQTestResult] = []
        for dqt in self.dq_tests:
            self.log.info('Start to test data in {dqt_name} test'.format(dqt_name=dqt.name))
            try:
                dqt_results.append(dqt.test_data(df, context))
            except Exception:  # TODO: Which exception can be here? Is it raised from DQTest
                dqt_results.append(
                    DQTestResult(
                        suite=dqt.suite,
                        name=dqt.name,
                        status=DQTestStatus.BROKEN.name,
                        reason='Data testing algorithm failed',
                        expected={},
                        actual=None,
                    ),
                )
                self.log.info('Error: data quality test {dqt_name} failed. Skip test'.format(dqt_name=dqt.name))
                self.log.info('Error traceback - {traceback}'.format(traceback=traceback.print_exc()))

        self.log.info('Start creating dqt entities')
        dqt_data_entities = []
        for dqt_result in dqt_results:
            dqt_test_oddrn = (
                '{airflow_oddrn}/dq/{suite}/{name}'.format(
                    airflow_oddrn=self.airflow_oddrn,
                    suite=dqt_result.suite,
                    name=dqt_result.name,
                )
            )
            self.log.info('Data quality test oddrn: {dqt_test_oddrn}'.format(dqt_test_oddrn=dqt_test_oddrn))
            # Creating a DQ Test
            dq_test = DataQualityTest(
                suite_name=dqt_result.suite,
                dataset_list=[self.dataset_oddrn],
                linked_url_list=self.linked_url_list,
                expectation=DataQualityTestExpectation(**dqt_result.expected),
            )

            self.log.info(
                DQ_TEST_TEMPLATE.format(
                    suite_name=dq_test.suite_name,
                    dataset_list=dq_test.dataset_list,
                    linked_url_list=dq_test.linked_url_list,
                    expectation=dq_test.expectation,
                ),
            )

            dq_test_entity = DataEntity(
                name=dqt_result.name,
                oddrn=dqt_test_oddrn,
                type=DataEntityType.JOB,
                data_quality_test=dq_test,
            )

            self.log.info(
                DQ_TEST_ENTITY_TEMPLATE.format(
                    name=dq_test_entity.name,
                    dataset_list=dq_test_entity.oddrn,
                    linked_url_list=dq_test_entity.type,
                    expectation=dq_test_entity.data_quality_test,
                ),
            )

            date_format = '{isoformat}Z'

            # Creating a DQ Test Run
            dq_test_run = DataQualityTestRun(
                data_quality_test_oddrn=dqt_test_oddrn,
                start_time=date_format.format(
                    isoformat=context.get('ti').start_date.replace(tzinfo=None).isoformat(),
                ),
                end_time=date_format.format(
                    isoformat=datetime.now().isoformat(),
                ),
                status_reason=dqt_result.reason,
                status=dqt_result.status,
            )

            self.log.info(
                DQ_TEST_RUN_TEMPLATE.format(
                    data_quality_test_oddrn=dq_test_run.data_quality_test_oddrn,
                    start_time=dq_test_run.start_time,
                    end_time=dq_test_run.end_time,
                    status_reason=dq_test_run.status_reason,
                    status=dq_test_run.status,
                ),
            )

            dq_test_run_entity = DataEntity(
                data_quality_test_run=dq_test_run,
                name='{dqt_result_name}_run_{execution_date}'.format(
                    dqt_result_name=dqt_result.name,
                    execution_date=context['execution_date'],
                ),
                oddrn='{dqt_test_oddrn}/run/{execution_date}'.format(
                    dqt_test_oddrn=dqt_test_oddrn,
                    execution_date=context['execution_date'],
                ),
                type=DataEntityType.JOB_RUN,
            )

            self.log.info(
                DQ_TEST_RUN_ENTITY_TEMPLATE.format(
                    data_quality_test_run=dq_test_run_entity.data_quality_test_run,
                    name=dq_test_run_entity.name,
                    oddrn=dq_test_run_entity.oddrn,
                    type=dq_test_run_entity.type,
                ),
            )
            dqt_data_entities.extend([dq_test_entity, dq_test_run_entity])

        self.log.info('Start to post data into odd')
        self.log.info(
            'DQT list entites - {dqt_data_entities}'.format(
                dqt_data_entities=dqt_data_entities,
            ),
        )
        self.log.info(
            'Data source oddrn - {airflow_oddrn}'.format(
                airflow_oddrn=self.airflow_oddrn,
            ),
        )

        self.odd_hook.post_data_entity_list(
            data_source_oddrn=self.airflow_oddrn,
            data_entities=dqt_data_entities,
        )

    def _try_to_open_and_execute(self, hook) -> pd.DataFrame:
        with open(self.sql, 'r') as query:
            self.log.info(
                'Start to execute sql query from file_path: {query_path}'.format(
                    query_path=self.sql,
                ),
            )
            return hook.get_pandas_df(sql=query.read())
