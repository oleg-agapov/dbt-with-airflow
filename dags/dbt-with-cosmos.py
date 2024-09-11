from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="astro",
    profiles_yml_filepath="/usr/local/airflow/dbt_jaffle_shop/profiles.yml",
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
