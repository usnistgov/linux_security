from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceType:
    """
    The ChoiceType type defines structures that hold information about one
    acceptable answer to a choice_question.

    :ivar value:
    :ivar id: All choices are tagged with a unique identifier that may
        be referenced by a choice_test_action referencing the
        encapsulating choice_question.
    :ivar var_ref:
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        },
    )
