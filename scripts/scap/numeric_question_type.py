from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from scap.question_type import QuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionType(QuestionType):
    """The NumericQuestionType type defines a question that requires a numeric
    answer.

    Acceptable values may be positive or negative and may include
    decimals.

    :ivar default_answer: An optional default value may be specified as
        the answer.
    """

    default_answer: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
