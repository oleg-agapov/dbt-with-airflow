from datetime import datetime

from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator

@dag(
    dag_id="dbt_with_bash_operator",
    start_date=datetime(2024, 8, 15),
    schedule_interval="0 0 * * *",
    catchup=False,
)
def run_dbt():

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command="dbt build --project-dir /usr/local/airflow/dbt_jaffle_shop --profiles-dir /usr/local/airflow/dbt_jaffle_shop"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="dbt run --project-dir /usr/local/airflow/dbt_jaffle_shop --profiles-dir /usr/local/airflow/dbt_jaffle_shop"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="dbt test --project-dir /usr/local/airflow/dbt_jaffle_shop --profiles-dir /usr/local/airflow/dbt_jaffle_shop"
    )

    dbt_seed >> dbt_run >> dbt_test

dag = run_dbt()
