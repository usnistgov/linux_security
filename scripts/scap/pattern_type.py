from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class PatternType:
    """
    The PatternType type defines a structure that specifies a regular expression
    against which a string will be compared.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        },
    )
