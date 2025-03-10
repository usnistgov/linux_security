from dataclasses import dataclass

from scap.boolean_question_type import BooleanQuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestion(BooleanQuestionType):
    """
    A boolean_question is a type of question element with valid responses of either
    {TRUE, FALSE} or {YES, NO}.
    """

    class Meta:
        name = "boolean_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
