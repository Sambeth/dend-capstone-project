from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators import (
    PreprocessToS3Operator,
    S3ToStagingOperator,
    StagingQualityCheckOperator,
    StagingToPrivateOperator
)

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
    'etl',
    default_args=default_args,
    description='Load data from s3 staging to redshift staging',
    schedule_interval='@monthly'
)

start_operator = DummyOperator(task_id='start_preprocessing_data', dag=dag)

preprocess_data_to_s3 = PreprocessToS3Operator(
    task_id="preprocess_data",
    dag=dag
)

end_operator = DummyOperator(task_id='end_preprocessing_data', dag=dag)

load_data_to_redshift_staging = S3ToStagingOperator(
    task_id="load_data_to_redshift",
    dag=dag,
    schema='staging'
)

check_staging_data_quality = StagingQualityCheckOperator(
    task_id="check_data_quality_in_staging",
    dag=dag,
    schema='staging'
)

end_loading = DummyOperator(task_id='end_loading_to_redshift', dag=dag)

insert_data_into_private = StagingToPrivateOperator(
    task_id="insert_data_into_private",
    dag=dag,
    schema='staging'
)

start_operator >> preprocess_data_to_s3 >> end_operator
end_operator >> load_data_to_redshift_staging >> check_staging_data_quality >> end_loading
end_loading >> insert_data_into_private
