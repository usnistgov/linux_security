from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class SystemdunitpropertyItem:
    """
    This item stores the properties and values of a systemd unit.

    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar property: The name of the property associated with a systemd
        unit.
    :ivar value: The value of the property associated with a systemd
        unit. Exactly one value shall be used for all property types
        except dbus arrays - each array element shall be represented by
        one value.
    """

    class Meta:
        name = "systemdunitproperty_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    property: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
