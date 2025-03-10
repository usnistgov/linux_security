from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_hash_type_type import EntityStateHashTypeType
from scap.entity_state_string_type import EntityStateStringType
from scap.entity_state_windows_view_type import EntityStateWindowsViewType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Filehash58State(StateType):
    """
    The filehash58_state element contains entities that are used to check the file
    path, name, hash_type, and hash associated with a specific file.

    :ivar filepath: The filepath entity specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path entity specifies the directory component of the
        absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of the file.
    :ivar hash_type: The hash_type entity specifies the hash algorithm
        to use when collecting the hash for each of the specifed files.
    :ivar hash: The hash entity specifies the result of applying the
        hash algorithm to the file.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "filehash58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

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
    hash_type: Optional[EntityStateHashTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    hash: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
