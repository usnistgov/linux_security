from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class SelinuxbooleanItem:
    """This item describes the current and pending status of a SELinux boolean.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar name: The name of the SELinux boolean.
    :ivar current_status: The current_status entity indicates current
        state of the specified SELinux boolean.
    :ivar pending_status: The pending_status entity indicates the
        pending state of the specified SELinux boolean.
    """

    class Meta:
        name = "selinuxboolean_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    current_status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pending_status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
