from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:oasis:names:tc:entity:xmlns:xml:catalog"


@dataclass
class RewriteUri:
    class Meta:
        name = "rewriteURI"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    uri_start_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriStartString",
            "type": "Attribute",
            "required": True,
        },
    )
    rewrite_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "rewritePrefix",
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
