from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class InetlisteningserverItem:
    """An inet listening server item stores the results of checking for network
    servers currently active on a system.

    It holds information pertaining to a specific protocol-address-port
    combination.

    :ivar protocol: This is the transport-layer protocol, in lowercase:
        tcp or udp.
    :ivar local_address: This is the IP address associated with the inet
        listening server. Note that the IP address can be IPv4 or IPv6.
    :ivar local_port: This is the TCP or UDP port on which the program
        listens.
    :ivar local_full_address: This is the IP address and network port on
        which the program listens, equivalent to
        local_address:local_port. Note that the IP address can be IPv4
        or IPv6.
    :ivar program_name: This is the name of the communicating program.
    :ivar foreign_address: This is the IP address with which the program
        is communicating, or with which it will communicate, in the case
        of a listening server. Note that the IP address can be IPv4 or
        IPv6.
    :ivar foreign_port: This is the TCP or UDP port to which the program
        communicates. In the case of a listening program accepting new
        connections, this value will be 0.
    :ivar foreign_full_address: This is the IP address and network port
        to which the program is communicating or will accept
        communications from, equivalent to foreign_address:foreign_port.
        Note that the IP address can be IPv4 or IPv6.
    :ivar pid: This is the process ID of the process. The process in
        question is that of the program communicating on the network.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "inetlisteningserver_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_port: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_full_address: Optional[str] = field(
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
    foreign_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    foreign_port: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    foreign_full_address: Optional[str] = field(
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
