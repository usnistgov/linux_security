from dataclasses import dataclass

from scap.string_question_test_action_type import StringQuestionTestActionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionTestAction(StringQuestionTestActionType):
    """
    A string_question_test_action element references a string_question and includes
    handlers that indicate actions to perform based on whether the response matches
    a given regular expression.
    """

    class Meta:
        name = "string_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
