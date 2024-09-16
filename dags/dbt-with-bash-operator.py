from datetime import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator

@dag(
    dag_id="dbt_with_bash_operator",
    schedule_interval="0 0 * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
)
def run_dbt():

    project_dir = "/usr/local/airflow/dbt_jaffle_shop"
    profiles_dir = "/usr/local/airflow/dbt_jaffle_shop"

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"dbt seed --project-dir {project_dir} --profiles-dir {profiles_dir}"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {project_dir} --profiles-dir {profiles_dir}"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir {project_dir} --profiles-dir {profiles_dir}"
    )

    dbt_seed >> dbt_run >> dbt_test

dag = run_dbt()
