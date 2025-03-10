from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class RunlevelItem:
    """The runlevel item holds information about the start or kill state of a
    specified service at a given runlevel.

    Each runlevel item contains service name and runlevel information as
    well as start and kill information. It extends the standard ItemType
    as defined in the oval-system-characteristics schema and one should
    refer to the ItemType description for more information.

    :ivar service_name: The service_name entity is the actual name of
        the specific service.
    :ivar runlevel: The runlevel entity specifies the system runlevel
        associated with a service.
    :ivar start: The start entity specifies whether the service is
        scheduled to start at the runlevel.
    :ivar kill: The kill entity specifies whether the service is
        scheduled to be killed at the runlevel.
    """

    class Meta:
        name = "runlevel_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    runlevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    kill: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
