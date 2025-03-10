from dataclasses import dataclass, field

from scap.questionnaire_result_type import QuestionnaireResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionnaireResultsType:
    """
    The QuestionnaireResultsType type defines structures containing computed
    results of all the evaluated questionnaires.

    :ivar questionnaire_result: The questionnaire_result element
        contains information about the result of a particular
        questionnaire.
    """

    questionnaire_result: list[QuestionnaireResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
