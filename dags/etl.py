from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators import (PreprocessToS3Operator)

S3_CONN_ID = 's3_staging'

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
    'preprocessing_data',
    default_args=default_args,
)

start_operator = DummyOperator(task_id='start_preprocessing_data', dag=dag)
preprocess_data_to_s3 = PreprocessToS3Operator(
    task_id="preprocess_data",
    s3_coonection=S3_CONN_ID,
    dag=dag
)

end_operator = DummyOperator(task_id='end_preprocessing_data', dag=dag)

start_operator >> preprocess_data_to_s3 >> end_operator
