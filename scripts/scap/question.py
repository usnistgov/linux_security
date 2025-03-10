from dataclasses import dataclass

from scap.question_type import QuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Question(QuestionType):
    """A question element contains information for one question that needs to be
    answered.

    It can be a boolean_question, choice_question, numeric_question, or
    string_question depending on the set of acceptable answers.
    """

    class Meta:
        name = "question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
