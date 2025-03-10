from dataclasses import dataclass

from scap.numeric_question_result_type import NumericQuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionResult(NumericQuestionResultType):
    """
    A numeric_question_result element contains a reference to a numeric_question,
    the number provided in response, and whether the question was successfully
    posed.
    """

    class Meta:
        name = "numeric_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
