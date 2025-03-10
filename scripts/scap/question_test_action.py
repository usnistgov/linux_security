from dataclasses import dataclass

from scap.question_test_action_type import QuestionTestActionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionTestAction(QuestionTestActionType):
    """The question_test_action element contains a reference to a single question
    along with a set of handlers that indicate how processing should proceed based
    on the answer provided.

    This element is abstract and is implemented in a document as a
    boolean_question_test_action, choice_question_test_action,
    numeric_question_test_action, or string_question_test_action. The
    type of question_test_action must match the type of question
    referenced (e.g. a boolean_question_test_action MUST reference a
    boolean_question.)
    """

    class Meta:
        name = "question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
