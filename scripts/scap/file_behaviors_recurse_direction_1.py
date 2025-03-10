from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


class FileBehaviorsRecurseDirection1(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"
