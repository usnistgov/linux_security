from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_int_type import EntityStateIntType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class ApparmorstatusState(StateType):
    """The AppArmor Status Item displays various information about the current
    AppArmor policy.

    This item maps the counts of profiles and processes as per the
    results of the "apparmor_status" or "aa-status" command.  Please
    refer to the individual elements in the schema for more details
    about what each represents.

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
        name = "apparmorstatus_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    loaded_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    enforce_mode_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    complain_mode_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    processes_with_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    enforce_mode_processes_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    complain_mode_processes_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unconfined_processes_with_profiles_count: Optional[EntityStateIntType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                
            },
        )
    )
