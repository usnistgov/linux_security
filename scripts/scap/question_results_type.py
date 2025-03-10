from dataclasses import dataclass, field

from scap.boolean_question_result import BooleanQuestionResult
from scap.choice_question_result import ChoiceQuestionResult
from scap.numeric_question_result import NumericQuestionResult
from scap.string_question_result import StringQuestionResult

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionResultsType:
    """
    The QuestionResultsType type defines structures containing computed results of
    all evaluated question types.
    """

    string_question_result: list[StringQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    numeric_question_result: list[NumericQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    choice_question_result: list[ChoiceQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    boolean_question_result: list[BooleanQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
