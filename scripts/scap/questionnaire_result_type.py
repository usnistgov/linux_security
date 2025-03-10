from dataclasses import dataclass, field
from typing import Optional

from scap.artifact_results_type import ArtifactResultsType
from scap.result_type import ResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionnaireResultType:
    """
    The QuestionnaireResultType type defines structures containing the computed
    result, associated artifacts and targets of a particular questionnaire.

    :ivar artifact_results: The artifact_results element contains a set
        of retrieved artifacts.
    :ivar questionnaire_ref: The questionnaire_ref attribute identifies
        a particular questionnaire using its id.
    :ivar result: The result attribute holds the result of evaluating
        the specified questionnaire.
    """

    artifact_results: Optional[ArtifactResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    questionnaire_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        },
    )
    result: Optional[ResultType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
