from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


class FileBehaviorsRecurse2(Enum):
    DIRECTORIES = "directories"
    SYMLINKS = "symlinks"
    SYMLINKS_AND_DIRECTORIES = "symlinks and directories"
