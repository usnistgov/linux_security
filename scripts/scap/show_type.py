from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class ShowType(Enum):
    NEW = "new"
    REPLACE = "replace"
    EMBED = "embed"
    OTHER = "other"
    NONE = "none"
