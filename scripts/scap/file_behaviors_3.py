from dataclasses import dataclass, field

from scap.file_behaviors_recurse_1 import FileBehaviorsRecurse1
from scap.file_behaviors_recurse_direction_1 import (
    FileBehaviorsRecurseDirection1,
)
from scap.file_behaviors_recurse_file_system_1 import (
    FileBehaviorsRecurseFileSystem1,
)

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class FileBehaviors3:
    """The FileBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of the file_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file.

    :ivar max_depth: 'max_depth' defines the maximum depth of recursion
        to perform when a recurse_direction is specified. A value of '0'
        is equivalent to no recursion, '1' means to step only one
        directory level up/down, and so on. The default value is '-1'
        meaning no limitation. For a 'max_depth' of -1 or any value of 1
        or more the starting directory must be considered in the
        recursive search. Note that the default recurse_direction
        behavior is 'none' so even though max_depth specifies no
        limitation by default, the recurse_direction behavior turns
        recursion off. Note that this behavior only applies with the
        equality operation on the path entity.
    :ivar recurse: 'recurse' defines how to recurse into the path
        entity, in other words what to follow during recursion. Options
        include symlinks, directories, or both. Note that a max-depth
        other than 0 has to be specified for recursion to take place and
        for this attribute to mean anything. Note that this behavior
        only applies with the equality operation on the path entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction
        to recurse, either 'up' to parent directories, or 'down' into
        child directories. The default value is 'none' for no recursion.
        Note that this behavior only applies with the equality operation
        on the path entity.
    :ivar recurse_file_system: 'recurse_file_system' defines the file
        system limitation of any searching and applies to all operations
        as specified on the path or filepath entity. The value of
        'local' limits the search scope to local file systems (as
        opposed to file systems mounted from an external system). The
        value of 'defined' keeps any recursion within the file system
        that the file_object (path+filename or filepath) has specified.
        For example, if the path specified was "/", you would search
        only the filesystem mounted there, not other filesystems mounted
        to descendant paths. The value of 'defined' only applies when an
        equality operation is used for searching because the path or
        filepath entity must explicitly define a file system. The
        default value is 'all' meaning to search all available file
        systems for data collection. Note that in most cases it is
        recommended that the value of 'local' be used to ensure that
        file system searching is limited to only the local file systems.
        Searching 'all' file systems may have performance implications.
    """

    class Meta:
        name = "FileBehaviors"

    max_depth: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1,
            "fraction_digits": 0,
        },
    )
    recurse: FileBehaviorsRecurse1 = field(
        default=FileBehaviorsRecurse1.SYMLINKS_AND_DIRECTORIES,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: FileBehaviorsRecurseDirection1 = field(
        default=FileBehaviorsRecurseDirection1.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_file_system: FileBehaviorsRecurseFileSystem1 = field(
        default=FileBehaviorsRecurseFileSystem1.ALL,
        metadata={
            "type": "Attribute",
        },
    )
