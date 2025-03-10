from dataclasses import dataclass

from scap.numeric_question_type import NumericQuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestion(NumericQuestionType):
    """A numeric_question is a type of question element that requires a numeric
    answer.

    Acceptable values may be positive or negative and may include
    decimals.
    """

    class Meta:
        name = "numeric_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
