from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


class EntityItemWindowsViewType(Enum):
    """The EntityItemWindowsViewType restricts a string value to a specific set of values: 32-bit and 64-bit. These values describe the different values possible for the windows view behavior.

    :cvar VALUE_32_BIT: Indicates the 32_bit windows view.
    :cvar VALUE_64_BIT: Indicates the 64_bit windows view.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"
    VALUE = ""
