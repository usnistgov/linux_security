from dataclasses import dataclass

from scap.string_question_type import StringQuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestion(StringQuestionType):
    """
    A string_question is a type of question element that requires a string answer.
    """

    class Meta:
        name = "string_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
