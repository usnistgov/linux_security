from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class ElementMapItemType:
    """
    Defines a reference to an OVAL entity using the schema namespace and element
    name.

    :ivar value:
    :ivar target_namespace: The target_namespace attributes indicates
        what XML namespace the element belongs to. If not present, the
        namespace is that of the document in which the
        ElementMapItemType instance element appears.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
