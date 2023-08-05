def get_provider_info():
    return {
        'package-name': 'airflow-commons',
        'name': 'KE Airflow Commons',
        'description': 'KE package with common operators for airflow',
        'versions': ['1.1.0.post6'],
        'additional-dependencies': ['apache-airflow>=2.3.3'],
        'operators': [
            {
                'integration-name': 'ClickHouse',
                'python-modules': [
                    'airflow_commons.operators.clickhouse_execute_operator',
                ],
            },
        ],
        'hooks': [
            {
                'integration-name': 'ClickHouse',
                'python-modules': ['airflow_commons.hooks.clickhouse_hook'],
            },
        ],
        'connection-types': [
            {
                'hook-class-name': 'airflow_commons.hooks.clickhouse_hook.ClickHouseHook',
                'connection-type': 'clickhouse',
            },
        ],
    }
