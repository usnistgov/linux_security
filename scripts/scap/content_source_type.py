from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class ContentSourceType:
    class Meta:
        name = "contentSourceType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
