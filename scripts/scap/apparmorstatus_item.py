from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class ApparmorstatusItem:
    """The AppArmor Status Item displays various information about the current
    AppArmor policy.

    This item maps the counts of profiles and processes as per the
    results of the "apparmor_status" or "aa-status" command.  Each item
    extends the standard ItemType as defined in the oval-system-
    characteristics-schema and one should refer to the ItemType
    description for more information.

    :ivar loaded_profiles_count: Displays the number of loaded profiles
    :ivar enforce_mode_profiles_count: Displays the number of profiles
        in enforce mode
    :ivar complain_mode_profiles_count: Displays the number of profiles
        in complain mode
    :ivar processes_with_profiles_count: Displays the number of
        processes which have profiles defined
    :ivar enforce_mode_processes_count: Displays the number of processes
        in enforce mode
    :ivar complain_mode_processes_count: Displays the number of
        processes in complain mode
    :ivar unconfined_processes_with_profiles_count: Displays the number
        of processes which are unconfined but have a profile defined
    """

    class Meta:
        name = "apparmorstatus_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    loaded_profiles_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    enforce_mode_profiles_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    complain_mode_profiles_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    processes_with_profiles_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    enforce_mode_processes_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    complain_mode_processes_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unconfined_processes_with_profiles_count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
