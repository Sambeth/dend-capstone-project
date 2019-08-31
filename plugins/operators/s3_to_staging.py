from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable

from helpers import (
    bnf_tables,
    practices_tables
)

REDSHIFT_CONN_ID = 'redshift_warehouse'
S3_BUCKET = Variable.get('bucket_name')
S3_KEY = Variable.get('key_name')
IAM_ROLE = Variable.get('iam_role')


class S3ToStagingOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 schema="",
                 *args, **kwargs):

        super(S3ToStagingOperator, self).__init__(*args, **kwargs)
        self.schema = schema

    def execute(self, context):
        self.log.info("loading data from s3 to redshift staging")

        redshift = PostgresHook(postgres_conn_id=REDSHIFT_CONN_ID)
        tables = bnf_tables + practices_tables

        for table in tables:
            copy_query = f"""
                COPY {self.schema}.{table}
                FROM 's3://{S3_BUCKET}/{S3_KEY}/{table}.parquet'
                IAM_ROLE '{IAM_ROLE}'
                FORMAT AS PARQUET;
            """

            self.log.info(f'Executing COPY command for table: {table}')
            self.log.info(copy_query)
            redshift.run(copy_query, autocommit=False)
            self.log.info(f"COPY command complete for table: {table}")
