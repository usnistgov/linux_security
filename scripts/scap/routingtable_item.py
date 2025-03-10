from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_routing_table_flags_type import (
    EntityItemRoutingTableFlagsType,
)

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class RoutingtableItem:
    """The routingtable_item holds information about an individual routing table
    entry found in a system's primary routing table.

    Each routingtable_item contains a destination IP address, gateway,
    netmask, flags, and the name of the interface associated with it. It
    is important to note that only numerical addresses will be collected
    and that their symbolic representations will not be resolved. This
    equivalent to using the '-n' option with route(8) or netstat(8). It
    extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar destination: The destination IP address prefix of the routing
        table entry. This is the destination IP address and
        netmask/prefix-length expressed using CIDR notation.
    :ivar gateway: The gateway of the specified routing table entry.
    :ivar flags: The flags associated with the specified routing table
        entry.
    :ivar interface_name: The name of the interface associated with the
        routing table entry.
    """

    class Meta:
        name = "routingtable_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    destination: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gateway: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flags: list[EntityItemRoutingTableFlagsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
