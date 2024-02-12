from contextlib import contextmanager
from dataclasses import dataclass
from typing import Tuple

import dbt.exceptions  # noqa
from dbt.adapters.base import Credentials

from dbt.adapters.base import BaseConnectionManager as connection_cls

from dbt.logger import GLOBAL_LOGGER as logger


@dataclass
class IncidentAdapterCredentials(Credentials):
    """
    Defines database specific credentials that get added to
    profiles.yml to connect to new adapter
    """

    db_profile: str = ""

    def _connection_keys(self) -> Tuple[str, ...]:
        return () + super()._connection_keys()

    @property
    def type(self):
        """Return name of adapter."""
        return "incident"

    @property
    def unique_field(self) -> str:
        return self.db_profile
