from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class ReferencesType1:
    """The ReferencesType complex type defines an element used to hold a collection
    of individual references.

    Each reference consists of a piece of text (intended to be human-
    readable) and a URI (intended to be a URL, and point to a real
    resource) and is used to point to extra descriptive material, for
    example a supplier's web site or platform documentation.
    """

    class Meta:
        name = "ReferencesType"

    reference: list["ReferencesType1.Reference"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )

    @dataclass
    class Reference:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
