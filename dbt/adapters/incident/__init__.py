from dbt.adapters.incident.connections import IncidentAdapterConnectionManager # noqa
from dbt.adapters.incident.connections import IncidentAdapterCredentials
from dbt.adapters.incident.impl import IncidentAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import incident


Plugin = AdapterPlugin(
    adapter=IncidentAdapter,
    credentials=IncidentAdapterCredentials,
    include_path=incident.PACKAGE_PATH
    )
