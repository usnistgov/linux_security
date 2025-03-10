from dataclasses import dataclass, field

from scap.choice_test_action_condition_type import (
    ChoiceTestActionConditionType,
)
from scap.question_test_action_type import QuestionTestActionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionTestActionType(QuestionTestActionType):
    """
    The ChoiceQuestionTestActionType type defines a structure that references a
    choice_question and includes handlers for the various choices set out in the
    choice_question.

    :ivar when_choice: Specifies the action to perform when the
        indicated choice is selected.
    """

    when_choice: list[ChoiceTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
