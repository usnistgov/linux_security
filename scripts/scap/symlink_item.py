from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class SymlinkItem:
    """
    The symlink_item element identifies the result generated for a symlink_object.

    :ivar filepath: Specifies the filepath to the subject symbolic link
        file, specified by the symlink_object.
    :ivar canonical_path: Specifies the canonical path for the target of
        the symbolic link file specified by the filepath.
    """

    class Meta:
        name = "symlink_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    canonical_path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
