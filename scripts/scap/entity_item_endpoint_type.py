from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemEndpointType(Enum):
    """The EntityItemEndpointType complex type restricts a string value to a
    specific set of values that describe endpoint types associated with an Internet
    service.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar STREAM: The stream value is used to describe a stream socket.
    :cvar DGRAM: The dgram value is used to describe a datagram socket.
    :cvar RAW: The raw value is used to describe a raw socket.
    :cvar SEQPACKET: The seqpacket value is used to describe a sequenced
        packet socket.
    :cvar TLI: The tli value is used to describe all TLI endpoints.
    :cvar SUNRPC_TCP: The sunrpc_tcp value is used to describe all
        SUNRPC TCP endpoints.
    :cvar SUNRPC_UDP: The sunrpc_udp value is used to describe all
        SUNRPC UDP endpoints.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    STREAM = "stream"
    DGRAM = "dgram"
    RAW = "raw"
    SEQPACKET = "seqpacket"
    TLI = "tli"
    SUNRPC_TCP = "sunrpc_tcp"
    SUNRPC_UDP = "sunrpc_udp"
    VALUE = ""
