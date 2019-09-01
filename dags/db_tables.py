from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators import PreliminaryQueriesOperator

from helpers import create_schemas, drop_statements, create_statements

REDSHIFT_CONN_ID = 'redshift_warehouse'

default_args = {
    'owner': 'airflow',
    'start_date': datetime.today(),
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'depends_on_past': False
}

dag = DAG(
    'drop_and_create_tables',
    default_args=default_args,
    description='Prepare redshift for ETL by dropping and creating tables'
)

start_schemas = DummyOperator(task_id='start_schema_creation',  dag=dag)

schema_creation = PreliminaryQueriesOperator(
    task_id='create_schemas',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=create_schemas,
    dag=dag
)

start_drops = DummyOperator(task_id='start_table_drops',  dag=dag)

drop_staging_tables = PreliminaryQueriesOperator(
    task_id='dropping_staging_tables',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=[query.format('staging') for query in drop_statements],
    dag=dag
)

drop_private_tables = PreliminaryQueriesOperator(
    task_id='dropping_private_tables',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=[query.format('private') for query in drop_statements],
    dag=dag
)

end_drops = DummyOperator(task_id='end_table_drops',  dag=dag)

start_creations = DummyOperator(task_id='start_table_creations',  dag=dag)

create_staging_tables = PreliminaryQueriesOperator(
    task_id='creating_staging_tables',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=[query.format('staging') for query in create_statements],
    dag=dag
)

create_private_tables = PreliminaryQueriesOperator(
    task_id='creating_private_tables',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=[query.format('private') for query in create_statements],
    dag=dag
)

end_creations = DummyOperator(task_id='end_table_creations',  dag=dag)

start_schemas >> schema_creation >> start_drops >> drop_staging_tables >> drop_private_tables >> end_drops
end_drops >> start_creations >> create_staging_tables >> create_private_tables >> end_creations
