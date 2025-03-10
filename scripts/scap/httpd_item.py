from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#apache"
)


@dataclass
class HttpdItem:
    """The httpd item holds information about a installed Apache HTTPD binary.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar path: The path element specifies the directory component of
        the absolute path to a httpd binary found on the system.
    :ivar binary_name: The name of the httpd binary.
    :ivar version: The version entity holds the version of the specified
        httpd binary.
    """

    class Meta:
        name = "httpd_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#apache"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    binary_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
