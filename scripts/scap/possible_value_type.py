from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class PossibleValueType:
    """The PossibleValueType complex type is used to outline a single expected
    value of an external variable.

    The required hint attribute gives a short description of what the
    value means or represents.
    """

    value: Optional[object] = field(default=None)
    hint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
