from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class FileextendedattributeState(StateType):
    """The fileextendedattribute_state element defines an extended attribute
    associated with a UNIX file.

    This includes the path, filename, attribute name, and attribute
    value.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory can be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar attribute_name: This is the extended attribute's name,
        identifier or key.
    :ivar value: The value entity represents the extended attribute's
        value or contents. To test for an attribute with no value
        assigned to it, this entity would be used with an empty value.
    """

    class Meta:
        name = "fileextendedattribute_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    attribute_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
