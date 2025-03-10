from dataclasses import dataclass, field
from typing import Optional

from scap.version_datatype_3 import VersionDatatype3

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#freebsd"
)


@dataclass
class PortinfoItem:
    class Meta:
        name = "portinfo_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#freebsd"

    pkginst: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["PortinfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class Version:
        datatype: VersionDatatype3 = field(
            default=VersionDatatype3.STRING,
            metadata={
                "type": "Attribute",
            },
        )
