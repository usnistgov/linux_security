from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_protocol_type import EntityItemProtocolType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class IflistenersItem:
    """An iflisteners_item stores the results of checking for applications that are
    bound to an interface on the system.

    Only applications that are bound to an ethernet interface should be
    collected.

    :ivar interface_name: This is the name of the interface (eth0, eth1,
        fw0, etc.).
    :ivar protocol: This is the physical layer protocol used by the
        AF_PACKET socket.
    :ivar hw_address: This is the hardware address associated with the
        interface.
    :ivar program_name: This is the name of the communicating program.
    :ivar pid: This is the process ID of the process. The process in
        question is that of the program communicating on the network.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "iflisteners_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    protocol: Optional[EntityItemProtocolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    hw_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    program_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
