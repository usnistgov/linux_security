from dataclasses import dataclass, field

from scap.file_behaviors_recurse_3 import FileBehaviorsRecurse3
from scap.file_behaviors_recurse_direction_3 import (
    FileBehaviorsRecurseDirection3,
)
from scap.file_behaviors_recurse_file_system_3 import (
    FileBehaviorsRecurseFileSystem3,
)
from scap.file_behaviors_windows_view import FileBehaviorsWindowsView

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class FileBehaviors1:
    """The FileBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of a set of files or file related items to collect.

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
        for this attribute to mean anything. Also note that on Windows,
        the 'symlink' value is equivalent to the 'junction' recurse
        value in win-def:FileBehaviors. Note that this behavior only
        applies with the equality operation on the path entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction
        to recurse, either 'up' to parent directories, or 'down' into
        child directories. The default value is 'none' for no recursion.
        Note that this behavior only applies with the equality operation
        on the path entity.
    :ivar recurse_file_system: 'recurse_file_system' defines the file
        system limitation of any searching and applies to all operations
        as specified on the path or filepath entity. The value of
        'local' limits the search scope to local file systems (as
        opposed to file systems mounted from an external system).  The
        value of 'defined' keeps any recursion within the file system
        that the file_object (path+filename or filepath) has specified.
        For example, on Windows, if the path specified was "C:\\", you
        would search only the C: drive, not other filesystems mounted to
        descendant paths. Similarly, on UNIX, if the path specified was
        "/", you would search only the filesystem mounted there, not
        other filesystems mounted to descendant paths. The value of
        'defined' only applies when an equality operation is used for
        searching because the path or filepath entity must explicitly
        define a file system. The default value is 'all' meaning to
        search all available file systems for data collection. Note that
        in most cases it is recommended that the value of 'local' be
        used to ensure that file system searching is limited to only the
        local file systems. Searching 'all' file systems may have
        performance implications.
    :ivar windows_view: 64-bit versions of Windows provide an alternate
        file system and registry views to 32-bit applications. This
        behavior allows the OVAL Object to specify which view should be
        examined. This behavior only applies to 64-bit Windows, and must
        not be applied on other platforms. Note that the values have the
        following meaning: '64_bit' – Indicates that the 64-bit view on
        64-bit Windows operating systems must be examined. On a 32-bit
        system, the Object must be evaluated without applying the
        behavior. '32_bit' – Indicates that the 32-bit view must be
        examined. On a 32-bit system, the Object must be evaluated
        without applying the behavior. It is recommended that the
        corresponding 'windows_view' entity be set on the OVAL Items
        that are collected when this behavior is used to distinguish
        between the OVAL Items that are collected in the 32-bit or
        64-bit views.
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
    recurse: FileBehaviorsRecurse3 = field(
        default=FileBehaviorsRecurse3.SYMLINKS_AND_DIRECTORIES,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: FileBehaviorsRecurseDirection3 = field(
        default=FileBehaviorsRecurseDirection3.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_file_system: FileBehaviorsRecurseFileSystem3 = field(
        default=FileBehaviorsRecurseFileSystem3.ALL,
        metadata={
            "type": "Attribute",
        },
    )
    windows_view: FileBehaviorsWindowsView = field(
        default=FileBehaviorsWindowsView.VALUE_64_BIT,
        metadata={
            "type": "Attribute",
        },
    )
