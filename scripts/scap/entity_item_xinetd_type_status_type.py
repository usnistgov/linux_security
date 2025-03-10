from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemXinetdTypeStatusType(Enum):
    """The EntityItemXinetdTypeStatusType complex type restricts a string value to
    five values, either RPC, INTERNAL, UNLISTED, TCPMUX, or TCPMUXPLUS that specify
    the type of service registered in xinetd.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar INTERNAL: The INTERNAL type is used to describe services like
        echo, chargen, and others whose functionality is supplied by
        xinetd itself.
    :cvar RPC: The RPC type is used to describe services that use remote
        procedure call ala NFS.
    :cvar UNLISTED: The UNLISTED type is used to describe services that
        aren't listed in /etc/protocols or /etc/rpc.
    :cvar TCPMUX: The TCPMUX type is used to describe services that
        conform to RFC 1078. This type indiciates that the service is
        responsible for handling the protocol handshake.
    :cvar TCPMUXPLUS: The TCPMUXPLUS type is used to describe services
        that conform to RFC 1078. This type indicates that xinetd is
        responsible for handling the protocol handshake.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    INTERNAL = "INTERNAL"
    RPC = "RPC"
    UNLISTED = "UNLISTED"
    TCPMUX = "TCPMUX"
    TCPMUXPLUS = "TCPMUXPLUS"
    VALUE = ""
