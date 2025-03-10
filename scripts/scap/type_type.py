from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class TypeType(Enum):
    SIMPLE = "simple"
    EXTENDED = "extended"
    TITLE = "title"
    RESOURCE = "resource"
    LOCATOR = "locator"
    ARC = "arc"
