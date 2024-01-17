from dbt.adapters.base import BaseAdapter

from dbt.adapters.incident import IncidentAdapterConnectionManager


class IncidentAdapter(BaseAdapter):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """

    def __init__(self, config):
        super().__init__(config)

    def __new__(cls, config):
        return super().__new__(cls)

    ConnectionManager = IncidentAdapterConnectionManager

    @classmethod
    def date_function(cls):
        """
        Returns canonical date func
        """
        return "datenow()"

    # may require more build out to make more user friendly to confer with team and community.
    @classmethod
    def type(cls) -> str:
        return "incident"
