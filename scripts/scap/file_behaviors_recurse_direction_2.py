from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


class FileBehaviorsRecurseDirection2(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"
