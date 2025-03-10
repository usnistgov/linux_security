from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemInterfaceType(Enum):
    """The EntityItemInterfaceType complex type restricts a string value to a
    specific set of values.

    These values describe the different interface types which are
    defined in 'if_arp.h'. The empty string is also allowed to support
    empty element associated with variable references. Note that when
    using pattern matches and variables care must be taken to ensure
    that the regular expression and variable values align with the
    enumerated values.

    :cvar ARPHRD_ETHER: The ARPHRD_ETHER type is used to describe
        ethernet interfaces.
    :cvar ARPHRD_FDDI: The ARPHRD_FDDI type is used to describe fiber
        distributed data interfaces (FDDI).
    :cvar ARPHRD_LOOPBACK: The ARPHRD_LOOPBACK type is used to describe
        loopback interfaces.
    :cvar ARPHRD_VOID: The ARPHRD_VOID type is used to describe unknown
        interfaces.
    :cvar ARPHRD_PPP: The ARPHRD_PPP type is used to describe point-to-
        point protocol interfaces (PPP).
    :cvar ARPHRD_SLIP: The ARPHRD_SLIP type is used to describe serial
        line internet protocol interfaces (SLIP).
    :cvar ARPHRD_PRONET: The ARPHRD_PRONET type is used to describe
        PROnet token ring interfaces.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    ARPHRD_ETHER = "ARPHRD_ETHER"
    ARPHRD_FDDI = "ARPHRD_FDDI"
    ARPHRD_LOOPBACK = "ARPHRD_LOOPBACK"
    ARPHRD_VOID = "ARPHRD_VOID"
    ARPHRD_PPP = "ARPHRD_PPP"
    ARPHRD_SLIP = "ARPHRD_SLIP"
    ARPHRD_PRONET = "ARPHRD_PRONET"
    VALUE = ""
