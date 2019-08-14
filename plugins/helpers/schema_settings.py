from pyspark.sql.types import (
    StructField,
    StructType,
    StringType,
    DoubleType,
    IntegerType
)

# schema settings for datasets
practice_prescribing_schema = StructType([
    StructField("SHA", StringType(), True),
    StructField("PCT", StringType(), True),
    StructField("PRACTICE", StringType(), True),
    StructField("BNF_CODE", StringType(), True),
    StructField("BNF_NAME", StringType(), True),
    StructField("ITEMS", IntegerType(), True),
    StructField("NIC", DoubleType(), True),
    StructField("ACT_COST", DoubleType(), True),
    StructField("QUANTITY", IntegerType(), True),
    StructField("PERIOD", StringType(), True),
])

chemicals_schema = StructType([
    StructField("CHEM_SUB_CODE", StringType(), True),
    StructField("NAME", StringType(), True),
])

practices_schema = StructType([
    StructField("PERIOD", StringType(), True),
    StructField("PRACTICE_CODE", StringType(), True),
    StructField("PRACTICE_NAME", StringType(), True),
    StructField("ADDRESS_1", StringType(), True),
    StructField("ADDRESS_2", StringType(), True),
    StructField("ADDRESS_3", StringType(), True),
    StructField("ADDRESS_4", StringType(), True),
    StructField("POSTCODE", StringType(), True),
])

practice_size_schema = StructType([
    StructField("COMM_PROV", StringType(), True),
    StructField("GROUP_CODE", StringType(), True),
    StructField("PRACTICE_NAME", StringType(), True),
    StructField("PRACTICE_ADDRESS", StringType(), True),
    StructField("PRACTICE_CODE", StringType(), True),
    StructField("GP_COUNT", IntegerType(), True),
    StructField("DISPENSING_LIST_SIZE", IntegerType(), True),
    StructField("PRESCRIBING_LIST_SIZE", IntegerType(), True),
    StructField("TOTAL_LIST_SIZE", IntegerType(), True),
])

bnf_codes_schema = StructType([
    StructField("BNF_CHAPTER", StringType(), True),
    StructField("BNF_CHAPTER_CODE", StringType(), True),
    StructField("BNF_SECTION", StringType(), True),
    StructField("BNF_SECTION_CODE", StringType(), True),
    StructField("BNF_PARAGRAPH", StringType(), True),
    StructField("BNF_PARAGRAPH_CODE", StringType(), True),
    StructField("BNF_SUBPARAGRAPH", StringType(), True),
    StructField("BNF_SUBPARAGRAPH_CODE", StringType(), True),
    StructField("BNF_CHEMICAL_SUBSTANCE", StringType(), True),
    StructField("BNF_CHEMICAL_SUBSTANCE_CODE", StringType(), True),
    StructField("BNF_PRODUCT", StringType(), True),
    StructField("BNF_PRODUCT_CODE", StringType(), True),
    StructField("BNF_PRESENTATION", StringType(), True),
    StructField("BNF_PRESENTATION_CODE", StringType(), True),
])
