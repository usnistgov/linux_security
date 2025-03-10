from dataclasses import dataclass, field

from scap.boolean_question import BooleanQuestion
from scap.choice_group_type import ChoiceGroupType
from scap.choice_question import ChoiceQuestion
from scap.numeric_question import NumericQuestion
from scap.string_question import StringQuestion

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionsType:
    """
    The QuestionsType type defines structures containing a set of QuestionType and
    ChoiceGroupType elements.

    :ivar string_question:
    :ivar numeric_question:
    :ivar choice_question:
    :ivar boolean_question:
    :ivar choice_group: Holds choice groups which represent possible
        sets of choices for choice_questions. Choice_groups may be
        reused across multiple choice_questions.
    """

    string_question: list[StringQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    numeric_question: list[NumericQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    choice_question: list[ChoiceQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    boolean_question: list[BooleanQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    choice_group: list[ChoiceGroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
