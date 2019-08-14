from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DropTablesOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 queries=[],
                 *args, **kwargs):
        """
        :param redshift_conn_id:
        :param table: table name
        :param args:
        :param kwargs:
        """

        super(DropTablesOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.queries = queries

    def execute(self, context):
        redshift = PostgresHook(self.redshift_conn_id)

        for query in self.queries:
            self.log.info(f"Running {query}")
            redshift.run(query)
