from dataclasses import dataclass, field
from typing import Optional

from scap.choice_answer_type import ChoiceAnswerType
from scap.question_result_type import QuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionResultType(QuestionResultType):
    """
    The ChoiceQuestionResultType type defines structures containing a reference to
    a choice_question, the response, and whether the question was successfully
    posed.

    :ivar answer: The answer element contains a choice_ref attribute
        that identifies the selected choice.
    """

    answer: Optional[ChoiceAnswerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "nillable": True,
        },
    )
