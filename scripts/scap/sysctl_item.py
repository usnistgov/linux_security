from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class SysctlItem:
    """
    The sysctl_item stores information retrieved from the local system about a
    kernel parameter and its respective value(s).

    :ivar name: The name element contains a string that represents the
        name of a kernel parameter that was collected from the local
        system.
    :ivar value: The value element contains a string that represents the
        current value(s) for the specified kernel parameter on the local
        system.
    """

    class Meta:
        name = "sysctl_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    name: Optional[str] = field(
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
