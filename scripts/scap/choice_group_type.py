from dataclasses import dataclass, field
from typing import Optional

from scap.choice_type import ChoiceType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceGroupType:
    """The ChoiceGroupType type defines a group of choices that may then be reused
    in multiple choice_question elements.

    For example, a document may include multiple choice_questions with
    the options of "Good", "Fair", or "Poor". By defining these choices
    in a single choice_group, the author would not need to list them out
    explicitly in every choice_question.

    :ivar choice: Holds the information associated with one of the
        possible responses for a choice_question.
    :ivar id: Holds the id of this choice group. This id is referenced
        within choice_question elements to include the choices contained
        in a group.
    """

    choice: list[ChoiceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choicegroup:[1-9][0-9]*",
        },
    )
