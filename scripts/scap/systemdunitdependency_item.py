from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class SystemdunitdependencyItem:
    """This item stores the dependencies of the systemd unit.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar dependency: The dependency entity refers to the name of a unit
        that was confirmed to be a dependency of the given unit.
    """

    class Meta:
        name = "systemdunitdependency_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    dependency: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
