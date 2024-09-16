
from airflow.models import DAG
from airflow.providers.dbt.cloud.operators.dbt import (
    DbtCloudGetJobRunArtifactOperator,
    DbtCloudListJobsOperator,
    DbtCloudRunJobOperator,
)
from airflow.providers.dbt.cloud.sensors.dbt import DbtCloudJobRunSensor

ACCOUNT_ID = 12345
JOB_ID = 54321

with DAG(
    dag_id="dbt_with_dbt_cloud",
    default_args={
        "dbt_cloud_conn_id": "dbt", 
        "account_id": ACCOUNT_ID
    },
) as dag:
    DbtCloudRunJobOperator(
        task_id="trigger_job",
        job_id=JOB_ID,
        check_interval=10,
        timeout=300,
    )
