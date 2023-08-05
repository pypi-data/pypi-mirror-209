from dataclasses import dataclass

import abc


class DatabaseConfig(abc.ABC):
    pass


@dataclass
class TableConfigBronzeMachineRaw(DatabaseConfig):
    database_name = "dev"
