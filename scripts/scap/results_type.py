from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.artifact_results_type import ArtifactResultsType
from scap.question_results_type import QuestionResultsType
from scap.questionnaire_results_type import QuestionnaireResultsType
from scap.targets_type import TargetsType
from scap.test_action_results_type import TestActionResultsType
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ResultsType:
    """
    The ResultsType type defines structures containing results from questionnaires,
    test actions, questions, artifacts, and metadata about the start/end time of
    evaluation, any targets, and a short caption or title.

    :ivar title: The title element contains a descriptive heading or
        caption describing the result set.
    :ivar questionnaire_results: The questionnare_results element
        contains computed results of all the evaluated questionnaires.
    :ivar test_action_results: The test_action_results element contains
        computed results of all the evaluated test_action types.
    :ivar question_results: The question_results element contains
        computed results of all evaluated question types.
    :ivar artifact_results: The artifact_results element contains all
        artifacts that have been retrieved during evaluation. Scope is
        the entire document.
    :ivar targets: The targets element contains all the actual target
        users, systems, and roles for which the OCIL document has been
        applied.
    :ivar start_time: The start_time attribute is an optional attribute
        that specifies when the evaluation of this OCIL file started.
    :ivar end_time: The end_time attribute is an optional attribute that
        specifies when the evaluation of this OCIL file ended.
    """

    title: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    questionnaire_results: Optional[QuestionnaireResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    test_action_results: Optional[TestActionResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    question_results: Optional[QuestionResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    artifact_results: Optional[ArtifactResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    targets: Optional[TargetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
