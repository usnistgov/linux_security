from dataclasses import dataclass, field
from typing import Optional

from scap.version_datatype_4 import VersionDatatype4

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class SlackwarepkginfoItem:
    """This item describes info related to Slackware packages.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar name: This is the pakage name to check.
    :ivar version: This is the version number of the pakage.
    :ivar architecture: This is the architecture the package is designed
        for.
    :ivar revision: This is the revision of the package.
    """

    class Meta:
        name = "slackwarepkginfo_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["SlackwarepkginfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    architecture: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    revision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class Version:
        datatype: VersionDatatype4 = field(
            default=VersionDatatype4.STRING,
            metadata={
                "type": "Attribute",
            },
        )
