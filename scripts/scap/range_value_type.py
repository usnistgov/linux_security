from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class RangeValueType:
    """
    Defines a specific bound in a range.

    :ivar value:
    :ivar inclusive: The inclusive attribute specifies whether the value
        should be in the specified range. The default is true,
        indicating it is included.
    :ivar var_ref: A reference to a variable to use as the value.
    """

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        },
    )
