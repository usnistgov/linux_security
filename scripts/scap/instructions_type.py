from dataclasses import dataclass, field
from typing import Optional

from scap.step_type import StepType
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class InstructionsType:
    """
    The InstructionsType type defines a series of steps intended to guide the user
    in answering a question.

    :ivar title: The title element contains a descriptive heading for
        the instructions.
    :ivar step: Each step element contains a single step within the
        instructions.
    """

    title: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    step: list[StepType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
