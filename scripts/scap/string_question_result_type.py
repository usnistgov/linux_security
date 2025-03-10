from dataclasses import dataclass, field
from typing import Optional

from scap.question_result_type import QuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionResultType(QuestionResultType):
    """
    The StringQuestionResultType type defines structures containing a reference to
    a string_question, the string provided in response, and whether the question
    was successfully posed.

    :ivar answer: The string value of the answer to a string_question.
    """

    answer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "nillable": True,
        },
    )
