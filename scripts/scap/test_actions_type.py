from dataclasses import dataclass, field

from scap.boolean_question_test_action import BooleanQuestionTestAction
from scap.choice_question_test_action import ChoiceQuestionTestAction
from scap.numeric_question_test_action import NumericQuestionTestAction
from scap.string_question_test_action import StringQuestionTestAction

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestActionsType:
    """
    The TestActionsType type defines a container for a set of test action elements.
    """

    string_question_test_action: list[StringQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    numeric_question_test_action: list[NumericQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    choice_question_test_action: list[ChoiceQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    boolean_question_test_action: list[BooleanQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
