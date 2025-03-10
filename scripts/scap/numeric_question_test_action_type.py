from dataclasses import dataclass, field

from scap.equals_test_action_condition_type import (
    EqualsTestActionConditionType,
)
from scap.question_test_action_type import QuestionTestActionType
from scap.range_test_action_condition_type import RangeTestActionConditionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionTestActionType(QuestionTestActionType):
    """
    The NumericQuestionTestActionType type defines a structure that references a
    numeric_question and includes handlers that indicate actions to perform based
    on whether the response matches a particular value or falls within a particular
    range.

    :ivar when_equals: This element holds information on what to do when
        the answer matches the specified value.
    :ivar when_range: This element holds information on what to do when
        the answer is within a specified range of values.
    """

    when_equals: list[EqualsTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
    when_range: list[RangeTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
