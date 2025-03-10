from dataclasses import dataclass, field
from typing import Optional

from scap.question_result_type import QuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestionResultType(QuestionResultType):
    """
    The BooleanQuestionResultType type defines structures containing a reference to
    a boolean_question, the response, and whether the question was successfully
    posed.

    :ivar answer: The value of the answer to the boolean_question. It
        could either be TRUE or FALSE.
    """

    answer: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "nillable": True,
        },
    )
