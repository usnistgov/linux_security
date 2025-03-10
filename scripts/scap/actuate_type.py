from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class ActuateType(Enum):
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"
    NONE = "none"
