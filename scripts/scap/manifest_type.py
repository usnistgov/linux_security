from dataclasses import dataclass, field
from typing import Optional

from scap.reference import Reference

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class ManifestType:
    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
