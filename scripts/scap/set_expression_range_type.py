from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from scap.set_expression_base_type import SetExpressionBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SetExpressionRangeType(SetExpressionBaseType):
    """
    :ivar min: The minimum decimal value of the range (inclusive).
    :ivar max: The maximum decimal value of the range (inclusive).
    """

    min: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    max: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
