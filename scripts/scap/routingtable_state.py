from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_ipaddress_type import EntityStateIpaddressType
from scap.entity_state_routing_table_flags_type import (
    EntityStateRoutingTableFlagsType,
)
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class RoutingtableState(StateType):
    """The routingtable_state element defines the different information that can be
    used to check an entry found in a system's primary routing table.

    This includes the destination IP address, gateway, netmask, flags,
    and the name of the interface associated with it. Please refer to
    the individual elements in the schema for more details about what
    each represents.

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
        name = "routingtable_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    destination: Optional[EntityStateIpaddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gateway: Optional[EntityStateIpaddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flags: Optional[EntityStateRoutingTableFlagsType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    interface_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
