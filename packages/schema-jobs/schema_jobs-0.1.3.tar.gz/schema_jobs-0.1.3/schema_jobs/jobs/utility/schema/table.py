from pyspark.sql import SparkSession

from schema_jobs.jobs.configuration.table_configs import TableConfig


def deploy_table(config: TableConfig):
    data_frame = SparkSession.getActiveSession().createDataFrame([], config.schema)
    table_name = config.table_name
    database_name = config.datanase_name
    data_frame.write.format("delta").mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
