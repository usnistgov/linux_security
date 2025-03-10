from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_int_type import EntityObjectIntType
from scap.entity_object_ipaddress_string_type import (
    EntityObjectIpaddressStringType,
)
from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class InetlisteningserversObject(ObjectType2):
    """The inetlisteningservers_object element is used by an inet listening servers
    test to define the specific protocol-address-port to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An inet listening servers object consists of
    three entities. The first identifies a specific IP address. The
    second entity represents a certain port number. While the third
    identifies the protocol.

    :ivar set:
    :ivar protocol: The protocol entity defines a certain transport-
        layer protocol, in lowercase: tcp or udp.
    :ivar local_address: This is the IP address of the network interface
        on which an application listens. Note that the IP address can be
        IPv4 or IPv6.
    :ivar local_port: This is the TCP or UDP port on which an
        application would listen. Note that this is not a list -- if a
        program listens on multiple ports, or on a combination of TCP
        and UDP, each will be represented by its own object.
    :ivar filter:
    """

    class Meta:
        name = "inetlisteningservers_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    protocol: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_address: Optional[EntityObjectIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    local_port: Optional[EntityObjectIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
