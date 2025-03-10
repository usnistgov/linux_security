from dataclasses import dataclass, field

from scap.operator_type import OperatorType
from scap.test_action_ref_type import TestActionRefType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class OperationType:
    """
    The OperationType type defines structures that hold a set of test_actions and
    provide instructions as to how to aggregate their individual results into a
    single result.

    :ivar test_action_ref: The test_action_ref element holds the
        identifier of a test_action element. At least one
        test_action_ref must be included.
    :ivar operation: The operation attribute describes how to aggregate
        the results of a set of test_actions. Its value defaults to the
        Boolean operator "AND".
    :ivar negate: The negate attribute can be used to specify whether to
        toggle the result from PASS to FAIL, and vice versa. A result
        other than PASS or FAIL (e.g. ERROR, NOT_TESTED) will be
        unchanged by a negate operation.
    """

    test_action_ref: list[TestActionRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
    operation: OperatorType = field(
        default=OperatorType.AND,
        metadata={
            "type": "Attribute",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
