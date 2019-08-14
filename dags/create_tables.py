from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from operators import (
    DropTablesOperator,
    CreateTablesOperator
)

from helpers import drop_statements, create_statements

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

start_drops = DummyOperator(task_id='start_table_drops',  dag=dag)

drop_tables = DropTablesOperator(
    task_id='drop_tables',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=drop_statements,
    dag=dag
)

end_drops = DummyOperator(task_id='end_table_drops',  dag=dag)

start_creations = DummyOperator(task_id='start_table_creations',  dag=dag)

create_tables = CreateTablesOperator(
    task_id='create_tables',
    redshift_conn_id=REDSHIFT_CONN_ID,
    queries=create_statements,
    dag=dag
)

end_creations = DummyOperator(task_id='end_table_creations',  dag=dag)

start_drops >> drop_tables >> end_drops
end_drops >> start_creations >> create_tables >> end_creations
