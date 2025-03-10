from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class FileextendedattributeItem:
    """The file extended attribute item holds information about the individual file
    extended attributes found on a system.

    Each file extended attribute item contains path, filename, and
    attribute name information as well as the attribute's value. It
    extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file. If the xsi:nil attribute is
        set to true, then the item being represented is the higher
        directory represented by the path entity.
    :ivar attribute_name: This is the extended attribute's name,
        identifier or key.
    :ivar value: This is the extended attribute's value or contents.
    """

    class Meta:
        name = "fileextendedattribute_item"
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
            
            "nillable": True,
        },
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
