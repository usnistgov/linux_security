from dataclasses import dataclass, field
from typing import Optional

from scap.question_test_action_type import QuestionTestActionType
from scap.test_action_condition_type import TestActionConditionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestionTestActionType(QuestionTestActionType):
    """
    The BooleanQuestionTestActionType type defines a structure that references a
    boolean_question and includes handlers for TRUE (YES) or FALSE (NO) responses.

    :ivar when_true: The element when_true specifies the action to do
        when the answer is true.
    :ivar when_false: The element when_false specifies the action to do
        when the answer is false.
    """

    when_true: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    when_false: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
