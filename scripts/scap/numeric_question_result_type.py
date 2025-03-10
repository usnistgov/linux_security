from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from scap.question_result_type import QuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionResultType(QuestionResultType):
    """
    The NumericQuestionResultType type defines structures containing a reference to
    a numeric_question, the provided response, and whether the question was
    successfully posed.

    :ivar answer: The decimal value of the answer to a numeric_question.
    """

    answer: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "nillable": True,
        },
    )
