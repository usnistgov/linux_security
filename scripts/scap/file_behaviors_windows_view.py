from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


class FileBehaviorsWindowsView(Enum):
    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"
