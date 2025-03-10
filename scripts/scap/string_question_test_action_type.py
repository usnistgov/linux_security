from dataclasses import dataclass, field

from scap.pattern_test_action_condition_type import (
    PatternTestActionConditionType,
)
from scap.question_test_action_type import QuestionTestActionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionTestActionType(QuestionTestActionType):
    """
    The StringQuestionTestActionType type defines a structure that references a
    string_question and includes handlers that indicate actions to perform based on
    whether the response matches a given regular expression.

    :ivar when_pattern: This element holds information on what to do
        when the answer matches a specified regular expression pattern.
    """

    when_pattern: list[PatternTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
