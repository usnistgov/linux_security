from dataclasses import dataclass, field

from scap.test_action_result_type import TestActionResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestActionResultsType:
    """
    The TestActionResultsType type defines structures containing computed results
    of all the evaluated test action types.

    :ivar test_action_result: The test_action_result element contains
        the result of a test_action evaluation. One of these elements
        will appear for each test_action evaluated.
    """

    test_action_result: list[TestActionResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
