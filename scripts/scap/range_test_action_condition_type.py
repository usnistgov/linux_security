from dataclasses import dataclass, field

from scap.range_type import RangeType
from scap.test_action_condition_type import TestActionConditionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class RangeTestActionConditionType(TestActionConditionType):
    """
    The RangeTestActionConditionType type defines a structure that specifies the
    action to take in a numeric_test_action when a value given in response to a
    numeric_question falls within the indicated range.

    :ivar range: Each range element holds a single numeric range.
    """

    range: list[RangeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
