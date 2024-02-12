from argparse import Namespace
from typing import Optional, Tuple, Dict, Any

from dbt.adapters.base import BaseAdapter
from dbt.adapters.protocol import AdapterConfig
from dbt.config import Profile
from dbt.config.profile import read_profile
from dbt.config.project import _raw_project_from
from dbt.config.renderer import ProfileRenderer
from dbt.flags import get_flag_dict

from dbt.adapters.incident.utils import find_target_name


class IncidentConfigs(AdapterConfig):
    incident_environment: Optional[str]


class IncidentAdapter(BaseAdapter):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """
    AdapterSpecificConfigs = IncidentConfigs

    def __init__(self, config):
        super().__init__(config)

    def __new__(cls, config):
        credentials = config.credentials
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


def load_profiles() -> Tuple[Profile, Dict[str, Any]]:
    flags: Namespace = get_flag_dict()

    profile_renderer = ProfileRenderer(getattr(flags, "VARS", {}))

    if flags.PROFILE is not None:
        profile_name = flags.PROFILE
    else:
        raw_project = _raw_project_from(flags.PROJECT_DIR)
        raw_profile_name = raw_project.get("profile")
        profile_name = profile_renderer.render_value(raw_profile_name)

    raw_profiles = read_profile(flags.PROFILES_DIR)
    raw_profile = raw_profiles[profile_name]

    target_name = find_target_name(flags.TARGET, raw_profile, profile_renderer)

    fal_dict = Profile._get_profile_data(
        profile=raw_profile,
        profile_name=profile_name,
        target_name=target_name,
    )
    db_profile_target_name = fal_dict.get("db_profile")
    assert (
        db_profile_target_name
    ), "`db_profile` property must be set"

    try:
        db_profile = Profile.from_raw_profile_info(
            raw_profile=raw_profile,
            profile_name=profile_name,
            renderer=profile_renderer,
            user_config=raw_profile.get("config"),
            target_override=db_profile_target_name,
        )
    except RecursionError as error:
        raise AttributeError(
            "Did you wrap a type 'incident' profile with another type 'incident' profile?"
        ) from error

    override_properties = {
        "threads": getattr(flags, "THREADS", None) or fal_dict.get("threads") or db_profile.threads,
    }

    return db_profile, override_properties
