from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemRoutingTableFlagsType(Enum):
    """The EntityItemRoutingTableFlagsType complex type restricts a string value to
    a specific set of values that describe the flags associated with a routing
    table entry.

    This list is based off the values defined in the man pages of
    various platforms. For Linux, please see route(8). For Solaris,
    please see netstat(1M). For HP-UX, please see netstat(1). For Mac
    OS, please see netstat(1). For FreeBSD, please see netstat(1).
    Documentation on each allowed value can be found in the previously
    listed man pages. The empty string is also allowed to support empty
    elements associated with error conditions.

    :cvar UP:
    :cvar GATEWAY:
    :cvar HOST:
    :cvar REINSTATE:
    :cvar DYNAMIC:
    :cvar MODIFIED:
    :cvar ADDRCONF:
    :cvar CACHE:
    :cvar REJECT:
    :cvar REDUNDANT:
    :cvar SETSRC:
    :cvar BROADCAST:
    :cvar LOCAL:
    :cvar PROTOCOL_1:
    :cvar PROTOCOL_2:
    :cvar PROTOCOL_3:
    :cvar BLACK_HOLE:
    :cvar CLONING:
    :cvar PROTOCOL_CLONING:
    :cvar INTERFACE_SCOPE:
    :cvar LINK_LAYER:
    :cvar MULTICAST:
    :cvar STATIC:
    :cvar WAS_CLONED:
    :cvar XRESOLVE:
    :cvar USABLE:
    :cvar PINNED:
    :cvar ACTIVE_DEAD_GATEWAY_DETECTION:
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    UP = "UP"
    GATEWAY = "GATEWAY"
    HOST = "HOST"
    REINSTATE = "REINSTATE"
    DYNAMIC = "DYNAMIC"
    MODIFIED = "MODIFIED"
    ADDRCONF = "ADDRCONF"
    CACHE = "CACHE"
    REJECT = "REJECT"
    REDUNDANT = "REDUNDANT"
    SETSRC = "SETSRC"
    BROADCAST = "BROADCAST"
    LOCAL = "LOCAL"
    PROTOCOL_1 = "PROTOCOL_1"
    PROTOCOL_2 = "PROTOCOL_2"
    PROTOCOL_3 = "PROTOCOL_3"
    BLACK_HOLE = "BLACK_HOLE"
    CLONING = "CLONING"
    PROTOCOL_CLONING = "PROTOCOL_CLONING"
    INTERFACE_SCOPE = "INTERFACE_SCOPE"
    LINK_LAYER = "LINK_LAYER"
    MULTICAST = "MULTICAST"
    STATIC = "STATIC"
    WAS_CLONED = "WAS_CLONED"
    XRESOLVE = "XRESOLVE"
    USABLE = "USABLE"
    PINNED = "PINNED"
    ACTIVE_DEAD_GATEWAY_DETECTION = "ACTIVE_DEAD_GATEWAY_DETECTION"
    VALUE = ""
