from dataclasses import dataclass

from scap.choice_question_result_type import ChoiceQuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionResult(ChoiceQuestionResultType):
    """
    A choice_question_result element contains a reference to a choice_question, the
    response, and whether the question was successfully posed.
    """

    class Meta:
        name = "choice_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
