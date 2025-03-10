from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class FactRefType:
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
