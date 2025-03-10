from dataclasses import dataclass

from scap.boolean_question_result_type import BooleanQuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestionResult(BooleanQuestionResultType):
    """
    A boolean_question_result element contains a reference to a boolean_question,
    the response, and whether the question was successfully posed.
    """

    class Meta:
        name = "boolean_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
