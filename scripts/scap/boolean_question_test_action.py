from dataclasses import dataclass

from scap.boolean_question_test_action_type import (
    BooleanQuestionTestActionType,
)

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestionTestAction(BooleanQuestionTestActionType):
    """
    A boolean_question_test_action element references a boolean_question and
    includes handlers for TRUE (YES) or FALSE (NO) responses.
    """

    class Meta:
        name = "boolean_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
