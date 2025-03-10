from dataclasses import dataclass, field

from scap.pattern_type import PatternType
from scap.test_action_condition_type import TestActionConditionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class PatternTestActionConditionType(TestActionConditionType):
    """
    The PatternTestActionConditionType type defines a structure that specifies the
    action to take in a string_test_action when a string given in response to a
    string_question matches the given regular expression.

    :ivar pattern: Each pattern element holds a regular expression
        against which the response string is to be compared.
    """

    pattern: list[PatternType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
