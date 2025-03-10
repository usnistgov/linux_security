from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.file_behaviors_3 import FileBehaviors3
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class FileObject(ObjectType2):
    """The file_object element is used by a file test to define the specific
    file(s) to be evaluated.

    The file_object will collect all UNIX file types (directory, regular
    file, character device, block device, fifo, symbolic link, and
    socket). Each object extends the standard ObjectType as defined in
    the oval-definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A file object defines the path and filename of
    the file(s). In addition, a number of behaviors may be provided that
    help guide the collection of objects. Please refer to the
    FileBehaviors complex type for more information about specific
    behaviors. The set of files to be evaluated may be identified with
    either a complete filepath or a path and filename. Only one of these
    options may be selected. It is important to note that the
    'max_depth' and 'recurse_direction' attributes of the 'behaviors'
    element do not apply to the 'filepath' element, only to the 'path'
    and 'filename' elements.  This is because the 'filepath' element
    represents an absolute path to a particular file and it is not
    possible to recurse over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        evaluate. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level directory object (not
        all the files in the directory).  In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar filter:
    """

    class Meta:
        name = "file_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileBehaviors3] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filepath: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
