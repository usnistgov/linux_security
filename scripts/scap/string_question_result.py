from dataclasses import dataclass

from scap.string_question_result_type import StringQuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionResult(StringQuestionResultType):
    """
    A string_question_result element contains a reference to a string_question, the
    string provided in response, and whether the question was successfully posed.
    """

    class Meta:
        name = "string_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
