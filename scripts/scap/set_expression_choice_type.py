from dataclasses import dataclass, field
from typing import Optional

from scap.set_expression_base_type import SetExpressionBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SetExpressionChoiceType(SetExpressionBaseType):
    """
    :ivar choice_ref: The choice_ref attribute is a reference to the
        choice associated with the question.
    """

    choice_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        },
    )
