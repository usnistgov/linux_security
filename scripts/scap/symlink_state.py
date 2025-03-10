from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class SymlinkState(StateType):
    """
    The symlink_state element defines a value used to evaluate the result of a
    specific symlink_object item.

    :ivar filepath: Specifies the filepath used to create the object.
    :ivar canonical_path: Specifies the canonical path for the target of
        a symbolic link file specified by the filepath.
    """

    class Meta:
        name = "symlink_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    canonical_path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
