from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="astro",
    profile_mapping=SnowflakeUserPasswordProfileMapping( 
        conn_id="snowflake_prod", 
        profile_args={"schema": "dbt"}, 
    ),
)

cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        "/usr/local/airflow/dbt_jaffle_shop",
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path="/usr/local/bin/dbt",
    ),
    dag_id="dbt_with_cosmos",
    default_args={"retries": 2},
)
