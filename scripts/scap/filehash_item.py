from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_windows_view_type import EntityItemWindowsViewType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class FilehashItem:
    """
    This element stores the different hash values associated with a specific file.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar md5: The md5 hash of the file
    :ivar sha1: The sha1 hash of the file
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "filehash_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

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
    md5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sha1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
