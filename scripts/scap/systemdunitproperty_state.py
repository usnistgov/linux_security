from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class SystemdunitpropertyState(StateType):
    """The systemdunitproperty_state element holds information about properties of
    a specific systemd unit.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar property: The name of the property associated with a systemd
        unit.
    :ivar value: The value of the property associated with a systemd
        unit.
    """

    class Meta:
        name = "systemdunitproperty_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    unit: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    property: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
