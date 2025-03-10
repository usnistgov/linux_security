from dataclasses import dataclass, field
from typing import Optional

from scap.artifact_results_type import ArtifactResultsType
from scap.result_type import ResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestActionResultType:
    """The TestActionResultType type defines structures containing all computed
    results of a TestActionType.

    One of these elements will appear for each test_action evaluated.

    :ivar artifact_results: The artifact_results element contains a set
        of retrieved artifacts.
    :ivar test_action_ref: The test_action_ref attribute identifies a
        specific test_action using its id.
    :ivar result: The result attribute holds the result of evaluating
        the specified test_action specified.
    """

    artifact_results: Optional[ArtifactResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    test_action_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:testaction:[1-9][0-9]*|ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        },
    )
    result: Optional[ResultType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
