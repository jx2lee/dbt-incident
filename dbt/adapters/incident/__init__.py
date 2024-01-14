from dbt.adapters.incident.connections import IncidentAdapterConnectionManager # noqa
from dbt.adapters.incident.connections import IncidentAdapterCredentials
from dbt.adapters.incident.impl import IncidentAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import incidentadapter


Plugin = AdapterPlugin(
    adapter=IncidentAdapter,
    credentials=IncidentAdapterCredentials,
    include_path=incidentadapter.PACKAGE_PATH
    )
