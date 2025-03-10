from dataclasses import dataclass, field
from typing import Optional

from scap.transforms import Transforms

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RetrievalMethodType:
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
