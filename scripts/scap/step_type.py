from dataclasses import dataclass, field
from typing import Optional

from scap.reference_type_3 import ReferenceType3
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StepType:
    """The StepType complex type defines structures that describe one step (out of
    possibly multiple steps) that a user should take to respond to a question.

    The steps would appear as part of the question's instructions
    element.

    :ivar description: The description element contains information
        about this step.
    :ivar reference: The reference element contains information about
        any external references related to this step.
    :ivar step: The step element contains a substep for this step.
    :ivar is_done: The is_done attribute indicates whether this step has
        been done. The value is true when it is done. Otherwise, it is
        false. It is an optional attribute that defaults to false.
    :ivar is_required: The is_required attribute indicates whether a
        step is required or not. If it is not, then it can be skipped.
        It is an optional attribute that defaults to true.
    """

    description: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    reference: list[ReferenceType3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    step: list["StepType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    is_done: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    is_required: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
