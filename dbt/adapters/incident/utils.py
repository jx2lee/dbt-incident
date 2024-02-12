from typing import Optional

from dbt.config.renderer import ProfileRenderer


def find_target_name(
        target_override: Optional[str],
        raw_profile: dict,
        profile_renderer: ProfileRenderer
):
    if target_override is not None:
        target_name = target_override
    elif "target" in raw_profile:
        target_name = profile_renderer.render_value(raw_profile["target"])
    else:
        target_name = "default"

    return target_name
