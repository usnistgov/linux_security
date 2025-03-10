from dataclasses import dataclass, field

from scap.test_action_condition_type import TestActionConditionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceTestActionConditionType(TestActionConditionType):
    """
    The ChoiceTestActionConditionType type defines a structure that specifies the
    action to take in a choice_test_action when a particular choice is selected in
    response to a choice_question.

    :ivar choice_ref: The choice_ref element specifies the id of a
        choice.
    """

    choice_ref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        },
    )
