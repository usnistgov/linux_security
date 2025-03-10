from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:oasis:names:tc:entity:xmlns:xml:catalog"


@dataclass
class SystemSuffix:
    class Meta:
        name = "systemSuffix"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    system_id_suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemIdSuffix",
            "type": "Attribute",
            "required": True,
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
