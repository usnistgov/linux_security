from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class SccsItem:
    """
    :ivar filepath: Specifies the absolute path to an SCCS file. A
        directory cannot be specified as a filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to an SCCS file.
    :ivar filename: The name of an SCCS file.
    :ivar module_name:
    :ivar module_type:
    :ivar release:
    :ivar level:
    :ivar branch:
    :ivar sequence:
    :ivar what_string:
    """

    class Meta:
        name = "sccs_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    module_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    module_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    branch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    what_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
