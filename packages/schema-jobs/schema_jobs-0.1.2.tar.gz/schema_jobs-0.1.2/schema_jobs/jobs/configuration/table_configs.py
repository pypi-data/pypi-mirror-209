from dataclasses import dataclass

from schema_jobs.jobs.utility.schema.schemas import bronze_machine_raw, bronze_sap_bseg, bronze_sales, gold_sales

import abc


class TableConfig(abc.ABC):
    pass


@dataclass
class TableConfigBronzeMachineRaw(TableConfig):
    table_name = "machine_raw"
    database_name = "dev"
    schema = bronze_machine_raw()


@dataclass
class TableConfigBronzSapBseg(TableConfig):
    table_name = "sap_bseg"
    database_name = "dev"
    schema = bronze_sap_bseg()


@dataclass
class TableConfigBronzeSales(TableConfig):
    table_name = "sales"
    database_name = "dev"
    schema = bronze_sales()


@dataclass
class TableConfigGoldSales(TableConfig):
    table_name = "gold_sales"
    database_name = "dev"
    schema = gold_sales()


tables = [TableConfigBronzeMachineRaw, TableConfigBronzSapBseg, TableConfigBronzeSales, TableConfigGoldSales]
