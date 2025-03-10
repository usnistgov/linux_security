from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class SymlinkObject(ObjectType2):
    """The symlink_object element is used by a symlink_test to define the object to
    be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A symlink_object consists of a filepath entity
    that contains the path to a symbolic link file.  The resulting item
    identifies the canonical path of the link target (followed to its
    final destination, if there are intermediate links), an error if the
    link target does not exist or is a circular link (e.g., a link to
    itself).  If the file located at filepath is not a symlink, or if
    there is no file located at the filepath, then any resulting item
    would itself have a status of does not exist.

    :ivar set:
    :ivar filepath: Specifies the filepath for the symbolic link.
    :ivar filter:
    """

    class Meta:
        name = "symlink_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    filepath: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
