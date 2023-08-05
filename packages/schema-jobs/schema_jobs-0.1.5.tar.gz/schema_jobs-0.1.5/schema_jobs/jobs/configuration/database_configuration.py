from dataclasses import dataclass

import abc


class DatabaseConfig(abc.ABC):
    pass


@dataclass
class DatabaseConfiguration(DatabaseConfig):
    database_name = "dev"
