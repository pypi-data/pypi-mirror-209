from pyspark.sql import SparkSession


def deploy_sql(sql:str):
    SparkSession.getActiveSession().sql(sql)