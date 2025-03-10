from dataclasses import dataclass

from scap.question_result_type import QuestionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionResult(QuestionResultType):
    """A question_result element contains result information associated with a
    specific question.

    The specific type of question_result (boolean_question_result,
    choice_question_result, etc.) depends on the type of the associated
    question (boolean_question, choice_question, etc.)
    """

    class Meta:
        name = "question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
