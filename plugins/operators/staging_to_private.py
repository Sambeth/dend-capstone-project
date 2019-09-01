from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable

from helpers import (
    bnf_tables,
    practices_tables
)

REDSHIFT_CONN_ID = 'redshift_warehouse'


class StagingToPrivateOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 schema="",
                 *args, **kwargs):

        super(StagingToPrivateOperator, self).__init__(*args, **kwargs)
        self.schema = schema

    def execute(self, context):
        self.log.info("inserting data from staging to redshift private")

        redshift = PostgresHook(postgres_conn_id=REDSHIFT_CONN_ID)
        tables = bnf_tables + practices_tables

        for table in tables:
            insert_query = f"""
                BEGIN TRANSACTION;
                -- Load new data
                INSERT INTO private.{table}
                SELECT * FROM {self.schema}.{table};
                
                -- clear up table
                TRUNCATE TABLE {self.schema}.{table};
                END TRANSACTION ;
            """

            self.log.info(f'Executing INSERT command for table: {table}')
            self.log.info(insert_query)
            redshift.run(insert_query, autocommit=False)
            self.log.info(f"INSERT command complete for table: {table}")
