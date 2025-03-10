from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


class FileBehaviorsRecurse1(Enum):
    NONE = "none"
    FILES = "files"
    DIRECTORIES = "directories"
    FILES_AND_DIRECTORIES = "files and directories"
    SYMLINKS = "symlinks"
    SYMLINKS_AND_DIRECTORIES = "symlinks and directories"
