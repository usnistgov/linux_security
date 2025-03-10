from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceAnswerType:
    """
    The ChoiceAnswerType type defines structures containing a choice_ref attribute
    that identifies the selected choice.

    :ivar choice_ref: The choice_ref attribute specifies the id of the
        selected choice.
    """

    choice_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        },
    )
