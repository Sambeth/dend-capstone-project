from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructField,
    StructType,
    StringType,
    DoubleType,
    IntegerType
)
import pyspark.sql.functions as f
from pyspark.sql.functions import udf, monotonically_increasing_id

from helpers import (
    practice_prescribing_schema,
    chemicals_schema,
    practices_schema,
    practice_size_schema,
    bnf_codes_schema
)

S3_OUTPUT_PATH = Variable.get('s3_output_bucket')
S3_INPUT_PATH = Variable.get('s3_input_bucket')
output_directory = Variable.get('local_data_directory_output')
input_directory = Variable.get('local_data_directory_input')
aws_access_key_id = Variable.get('aws_access_key_id')
aws_secret_key = Variable.get('aws_secret_access_key')


class PreprocessToS3Operator(BaseOperator):

    ui_color = '#80BD9E'

    bnf_filenames = [
        'bnf_chapters',
        'bnf_sections',
        'bnf_paragraphs',
        'bnf_subparagraphs',
        'bnf_chemicals',
        'bnf_products',
        'bnf_presentations'
    ]

    practices_filenames = [
        'chemicals',
        'practices',
        'practices_size',
        'practice_prescribing'
    ]

    @apply_defaults
    def __init__(self,
                 schema="",
                 s3_bucket="",
                 s3_key="",
                 filename="",
                 s3_connection="",
                 redshift_conn_id="",
                 *args, **kwargs):

        super(PreprocessToS3Operator, self).__init__(*args, **kwargs)
        self.schema = schema
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.filename = filename
        self.s3_connection = s3_connection
        self.redshift_conn_id = redshift_conn_id

        # setting udf functions
        self.get_year = udf(lambda x: int(x[:-2]) if x else None, IntegerType())
        self.get_month = udf(lambda x: int(x[-2:]) if x else None, IntegerType())

        self.get_chapter = udf(lambda x: x[:2] if x else None)
        self.get_section = udf(lambda x: x[:4] if x else None)
        self.get_paragraph = udf(lambda x: x[:6] if x else None)
        self.get_sub_paragraph = udf(lambda x: x[:7] if x else None)
        self.get_chemical = udf(lambda x: x[:9] if x else None)
        self.get_product = udf(lambda x: x[:11] if x else None)

        # files
        self.chemicals_file = f'{input_directory}/chem_subs.csv'
        self.practices_file = f'{input_directory}/practices.csv'
        self.practice_prescribing_file = f'{input_directory}/practice_prescribing.csv'
        self.practice_size_file = f'{input_directory}/practice_list_size_and_gp_count.csv'
        self.bnf_codes_file = f'{input_directory}/bnf_codes.csv'

        # create spark session
        self.log.info("Creating Spark Session")
        self.spark = SparkSession.builder.config(
            "spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0"
        ).appName("HealthPrescription").getOrCreate()
        self.spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.awsAccessKeyId", aws_access_key_id)
        self.spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.awsSecretAccessKey", aws_secret_key)
        self.spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", aws_access_key_id)
        self.spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", aws_secret_key)

    def process_bnf_data(self):
        self.log.info("preprocessing bnf codes data")
        bnf_codes = self.spark.read.csv(self.bnf_codes_file, header=True, schema=bnf_codes_schema)
        bnf_chapters = bnf_codes.select('BNF_CHAPTER_CODE', 'BNF_CHAPTER').dropDuplicates()
        bnf_sections = bnf_codes.select('BNF_SECTION_CODE', 'BNF_SECTION').dropDuplicates()
        bnf_paragraphs = bnf_codes.select('BNF_PARAGRAPH_CODE', 'BNF_PARAGRAPH').dropDuplicates()
        bnf_subparagraph = bnf_codes.select('BNF_SUBPARAGRAPH_CODE', 'BNF_SUBPARAGRAPH').dropDuplicates()
        bnf_chemicals = bnf_codes.select('BNF_CHEMICAL_SUBSTANCE_CODE', 'BNF_CHEMICAL_SUBSTANCE').dropDuplicates()
        bnf_products = bnf_codes.select('BNF_PRODUCT_CODE', 'BNF_PRODUCT').dropDuplicates()
        bnf_presentations = bnf_codes.select('BNF_PRESENTATION_CODE', 'BNF_PRESENTATION').dropDuplicates()

        self.log.info("saving bnf codes data")
        return bnf_chapters.write.parquet(f'{S3_OUTPUT_PATH}/bnf_chapters.parquet', mode='overwrite'), \
            bnf_sections.write.parquet(f'{S3_OUTPUT_PATH}/bnf_sections.parquet', mode='overwrite'), \
            bnf_paragraphs.write.parquet(f'{S3_OUTPUT_PATH}/bnf_paragraphs.parquet', mode='overwrite'), \
            bnf_subparagraph.write.parquet(f'{S3_OUTPUT_PATH}/bnf_subparagraphs.parquet', mode='overwrite'), \
            bnf_chemicals.write.parquet(f'{S3_OUTPUT_PATH}/bnf_chemicals.parquet', mode='overwrite'), \
            bnf_products.write.parquet(f'{S3_OUTPUT_PATH}/bnf_products.parquet', mode='overwrite'), \
            bnf_presentations.write.parquet(f'{S3_OUTPUT_PATH}/bnf_presentations.parquet', mode='overwrite')

    def process_practices_data(self):
        self.log.info("preprocessing practices data")
        practices = self.spark.read.csv(self.practices_file, header=False, schema=practices_schema)
        practices = practices.withColumn("YEAR", self.get_year(practices.PERIOD))
        practices = practices.withColumn("MONTH", self.get_month(practices.PERIOD))
        practices = practices.drop('PERIOD')
        practices = practices.na.drop(subset=["PRACTICE_CODE"])

        self.log.info("saving practices data")
        return practices.write.parquet(f'{S3_OUTPUT_PATH}/practices.parquet', mode='overwrite')

    def process_practices_size_and_group_data(self):
        self.log.info("preprocessing practices size data")
        practice_size_and_group = self.spark.read.csv(self.practice_size_file, header=True, schema=practice_size_schema)

        practice_groups = practice_size_and_group.select(
                                'GROUP_CODE',
                                'COMM_PROV',
                            ).dropDuplicates()
        practice_groups = practice_groups.na.drop(subset=["GROUP_CODE"])

        practice_size = practice_size_and_group.select(
            'PRACTICE_CODE',
            'GROUP_CODE',
            'GP_COUNT',
            'DISPENSING_LIST_SIZE',
            'PRESCRIBING_LIST_SIZE',
            'TOTAL_LIST_SIZE'
        )
        practice_size = practice_size.na.drop(subset=["PRACTICE_CODE"])

        self.log.info("saving practices size and group data")
        return practice_size.write.parquet(f'{S3_OUTPUT_PATH}/practices_size.parquet', mode='overwrite'),\
            practice_groups.write.parquet(f'{S3_OUTPUT_PATH}/practice_groups.parquet', mode='overwrite')

    def process_prescribing_data(self):
        self.log.info("preprocessing prescribing data")
        practice_prescribing = self.spark.read.csv(self.practice_prescribing_file,
                                                   header=True, schema=practice_prescribing_schema)
        practice_prescribing = practice_prescribing.withColumn("PRESCRIPTION_ID", monotonically_increasing_id())
        practice_prescribing = practice_prescribing.withColumn("YEAR", self.get_year(practice_prescribing.PERIOD))
        practice_prescribing = practice_prescribing.withColumn("MONTH", self.get_month(practice_prescribing.PERIOD))
        practice_prescribing = practice_prescribing.drop('PERIOD')
        practice_prescribing = practice_prescribing.withColumn("BNF_CHAPTER_CODE",
                                                               self.get_chapter(practice_prescribing['BNF_CODE']))
        practice_prescribing = practice_prescribing.withColumn("BNF_SECTION_CODE",
                                                               self.get_section(practice_prescribing['BNF_CODE']))
        practice_prescribing = practice_prescribing.withColumn("BNF_PARAGRAPH_CODE",
                                                               self.get_paragraph(practice_prescribing['BNF_CODE']))
        practice_prescribing = practice_prescribing.withColumn("BNF_SUBPARAGRAPH_CODE",
                                                               self.get_sub_paragraph(practice_prescribing['BNF_CODE']))
        practice_prescribing = practice_prescribing.withColumn("BNF_CHEMICAL_CODE",
                                                               self.get_chemical(practice_prescribing['BNF_CODE']))
        practice_prescribing = practice_prescribing.withColumn("BNF_PRODUCT_CODE",
                                                               self.get_product(practice_prescribing['BNF_CODE']))

        practice_prescribing = practice_prescribing.select(
            'PRESCRIPTION_ID',
            'SHA',
            'PCT',
            'PRACTICE',
            'BNF_CODE',
            'BNF_CHAPTER',
            'BNF_SECTION',
            'BNF_PARAGRAPH',
            'BNF_SUBPARAGRAPH',
            'BNF_CHEMICAL',
            'BNF_PRODUCT',
            'ITEMS',
            'NIC',
            'ACT_COST',
            'QUANTITY',
            'YEAR',
            'MONTH'
        )

        self.log.info("saving prescribing data")
        return practice_prescribing.write.parquet(f'{S3_OUTPUT_PATH}/practice_prescribing.parquet', mode='overwrite')

    def execute(self, context):
        self.log.info("saving parquet output files to s3")
        self.process_bnf_data()
        self.process_practices_data()
        self.process_practices_size_data()
        self.process_prescribing_data()
