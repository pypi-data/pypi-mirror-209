from pyspark.sql.types import StructType,FloatType,BinaryType, StructField, StringType, IntegerType


def bronze_machine_raw():
    schema = StructType([
        StructField("N8j2", FloatType(), True),
        StructField("42mj", FloatType(), True),
        StructField("6tk3", BinaryType(), True),
        ])
    return schema


def silver_machine_raw():
    schema = StructType([
        StructField("N8j2", FloatType(), True),
        StructField("42mj", FloatType(), True),
        StructField("6tk3", BinaryType(), True),
        StructField("engine_type", StringType(), True)
        ])
    return schema


def bronze_sap_bseg():
    schema = StructType([
        StructField("MANDT", StringType(), True),
        StructField("BUKRS", StringType(), True),
        StructField("BELNR", StringType(), True),
        StructField("GJAHR", FloatType(), True),
        StructField("BUZEI", FloatType(), True)
        ])
    return schema


def bronze_sales():
    schema = StructType([
        StructField("ORDERNUMBER", IntegerType(), True),
        StructField("SALE", FloatType(), True),
        StructField("ORDERDATE", IntegerType(), True),
        StructField("STATUS", BinaryType(), True),
        StructField("CUSTOMERNAME", StringType(), True),
        StructField("ADDRESSLINE", IntegerType(), True),
        StructField("CITY", StringType(), True),
        StructField("STATE", StringType(), True),
        StructField("STORE", StringType(), True)
        ])
    return schema

def gold_sales():
    schema = StructType([
        StructField("CUSTOMERNAME", StringType(), True),
        StructField("AVG", FloatType(), True),
        StructField("TOTAL", FloatType(), True),
        ])
    return schema
