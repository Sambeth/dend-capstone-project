from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import (
    bnf_tables,
    practices_tables
)

REDSHIFT_CONN_ID = 'redshift_warehouse'


class StagingQualityCheckOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 schema="",
                 *args, **kwargs):

        super(StagingQualityCheckOperator, self).__init__(*args, **kwargs)
        self.schema = schema

    def execute(self, context):
        self.log.info("checking if data exists in redshift staging table")

        redshift = PostgresHook(postgres_conn_id=REDSHIFT_CONN_ID)
        tables = bnf_tables + practices_tables

        for table in tables:
            records = redshift.get_records(f"SELECT COUNT(*) FROM {self.schema}.{table}")

            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError(f"{table} is empty. Data Quality check failed.")

            num_records = records[0][0]

            if num_records < 1:
                raise ValueError(f"{self.schema}.{table} is empty. Data Quality check failed.")

            self.log.info(f"Data Quality check successful. {self.schema}.{table} has {num_records} of records")
