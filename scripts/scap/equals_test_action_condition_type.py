from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from scap.test_action_condition_type import TestActionConditionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class EqualsTestActionConditionType(TestActionConditionType):
    """
    The EqualsTestActionConditionType defines a structure that specifies the action
    to take in a numeric_test_action when a particular value is given in response
    to a numeric_question.

    :ivar value: Each value holds what is to be matched.
    :ivar var_ref:
    """

    value: list[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        },
    )
