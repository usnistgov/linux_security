from dataclasses import dataclass, field

from scap.questionnaire_type import QuestionnaireType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionnairesType:
    """
    The QuestionnairesType type defines a container for a set of questionnaire
    elements.

    :ivar questionnaire: A questionnaire contains a set of questions
        that determines compliance with a check. Each questionnaire
        returns a value based on the responses to the various questions
        that it references. Each questionnaire acting as top-level
        should represent a single compliance check, such as might be
        referenced by an XCCDF Rule.
    """

    questionnaire: list[QuestionnaireType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
