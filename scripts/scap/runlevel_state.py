from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_bool_type import EntityStateBoolType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class RunlevelState(StateType):
    """The runlevel_state element holds information about whether a specific
    service is scheduled to start or stop at a given runlevel.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar service_name: The service_name entity refers the name
        associated with a service. This name is usually the filename of
        the script file located in the /etc/init.d directory.
    :ivar runlevel: The runlevel entity refers to the system runlevel
        associated with a service. A runlevel is defined as a software
        configuration of the system that allows only a selected group of
        processes to exist.
    :ivar start: The start entity determines if the process is scheduled
        to be spawned at the specified runlevel.
    :ivar kill: The kill entity determines if the process is supposed to
        be killed at the specified runlevel.
    """

    class Meta:
        name = "runlevel_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    service_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    runlevel: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    start: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    kill: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
