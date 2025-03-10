from dataclasses import dataclass, field
from typing import Optional

from scap.set_expression_base_type import SetExpressionBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SetExpressionBooleanType(SetExpressionBaseType):
    """
    :ivar value_attribute: The boolean value to match.
    """

    value_attribute: Optional[bool] = field(
        default=None,
        metadata={
            "name": "value",
            "type": "Attribute",
            "required": True,
        },
    )
