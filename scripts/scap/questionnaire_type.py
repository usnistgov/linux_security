from dataclasses import dataclass, field
from typing import Optional

from scap.compound_test_action_type import CompoundTestActionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionnaireType(CompoundTestActionType):
    """The QuestionnaireType type defines a structure that represents a specific
    question or set of questions that evaluate to a single result.

    A questionnaire may contain multiple test_actions. test_actions may
    be nested and aggregated through an acceptable operation to produce
    the result of a check.

    :ivar id: Each questionnaire is required to have a unique identifier
        that conforms to the definition of NCName in the Recommendation
        "Namespaces in XML 1.0", i.e., all XML 1.0 names that do not
        contain colons.
    :ivar child_only: This attribute specifies whether or not this
        questionnaire should only appear as a child of another
        questionnaire. All questionnaires must be defined within the
        body of the ocil element and, by default, interpreters might
        simply grab all questionnaires and evaluate them. However,
        questionnaires can reference other questionnaires through a
        test_action_ref. If an author references a questionnaire in this
        way, they may not wish that the questionnaire be evaluated
        except as a child of another questionnaire. By setting the
        child_only attribute to true, the author is indicating that the
        given questionnaire should not be a "top-level" questionnaire
        but should instead only be evaluated as the child of another
        questionnaire.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        },
    )
    child_only: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
