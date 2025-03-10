from dataclasses import dataclass, field
from typing import Optional

from scap.set_expression_base_type import SetExpressionBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SetExpressionPatternType(SetExpressionBaseType):
    """
    :ivar pattern: The pattern attribute is a string representation of
        the pattern to be matched.
    """

    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
