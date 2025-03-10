from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_ipaddress_string_type import (
    EntityStateIpaddressStringType,
)
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class InetlisteningserversState(StateType):
    """The inetlisteningservers_state element defines the different information
    that can be used to evaluate the specified inet listening server.

    This includes the local address, foreign address, port information,
    and process id. Please refer to the individual elements in the
    schema for more details about what each represents.

    :ivar protocol: The protocol entity defines the specific transport-
        layer protocol, in lowercase: tcp or udp, associated with the
        inet listening server.
    :ivar local_address: This is the IP address of the network interface
        on which the program listens. Note that the IP address can be
        IPv4 or IPv6.
    :ivar local_port: This is the TCP or UDP port number associated with
        the inet listening server.
    :ivar local_full_address: This is the IP address and network port
        number associated with the inet listening server, equivalent to
        local_address:local_port. Note that the IP address can be IPv4
        or IPv6.
    :ivar program_name: This is the name of the communicating program.
    :ivar foreign_address: This is the IP address with which the program
        is communicating, or with which it will communicate, in the case
        of a listening server. Note that the IP address can be IPv4 or
        IPv6.
    :ivar foreign_port: This is the TCP or UDP port to which the program
        communicates. In the case of a listening program accepting new
        connections, the value will be 0.
    :ivar foreign_full_address: This is the IP address and network port
        to which the program is communicating or will accept
        communications from, equivalent to foreign_address:foreign_port.
        Note that the IP address can be IPv4 or IPv6.
    :ivar pid: The pid is the process ID of a specific process.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "inetlisteningservers_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    protocol: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_port: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_full_address: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    program_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    foreign_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    foreign_port: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    foreign_full_address: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
