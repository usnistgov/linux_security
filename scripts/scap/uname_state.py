from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class UnameState(StateType):
    """The uname_state element defines the information about the hardware the
    machine is running one.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar machine_class: This entity specifies a machine hardware name.
        This corresponds to the command uname -m.
    :ivar node_name: This entity specifies a host name. This corresponds
        to the command uname -n.
    :ivar os_name: This entity specifies an operating system name. This
        corresponds to the command uname -s.
    :ivar os_release: This entity specifies a build version. This
        corresponds to the command uname -r.
    :ivar os_version: This entity specifies an operating system version.
        This corresponds to the command uname -v.
    :ivar processor_type: This entity specifies a processor type. This
        corresponds to the command uname -p.
    """

    class Meta:
        name = "uname_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    machine_class: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    node_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    os_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    os_release: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    os_version: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    processor_type: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
