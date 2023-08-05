from schema_jobs.jobs.configuration.database_configuration import DatabaseConfig
from pyspark.sql import SparkSession


def deploy_database(config: DatabaseConfig):
    SparkSession.getActiveSession()
    SparkSession.getActiveSession().sql(f"CREATE DATABASE IF NOT EXISTS {config.database_name};")
