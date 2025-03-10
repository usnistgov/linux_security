from dataclasses import dataclass, field
from typing import Optional

from scap.choice_type import ChoiceType
from scap.question_type import QuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionType(QuestionType):
    """The ChoiceQuestionType type defines a question with one or more acceptable
    answers specified by the author.

    The response will be one of these specified answers. Acceptable
    answers are specified either explicitly using the choice element or
    implicitly using the choice_group_ref element to reference a
    choice_group element. Choices are presented in the order in which
    they are provided. All the choices in a choice_group are inserted in
    the order in which they appear within the choice_group.

    :ivar choice: Holds the information associated with one of the
        possible responses to this choice_question.
    :ivar choice_group_ref: Holds a reference to a choice_group. The
        questions described in this choice group are used as possible
        responses for this choice_question.
    :ivar default_answer_ref: The default_answer_ref specifies the
        choice id of the default answer to the question.
    """

    choice: list[ChoiceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    choice_group_ref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choicegroup:[1-9][0-9]*",
        },
    )
    default_answer_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        },
    )
