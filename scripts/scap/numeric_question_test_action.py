from dataclasses import dataclass

from scap.numeric_question_test_action_type import (
    NumericQuestionTestActionType,
)

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionTestAction(NumericQuestionTestActionType):
    """
    A numeric_question_test_action element references a numeric_question and
    includes handlers that indicate actions to perform based on whether the
    response matches a particular value or falls within a particular range.
    """

    class Meta:
        name = "numeric_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
