from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class StateRefType:
    """The StateRefType complex type defines a state reference to be used by OVAL
    Tests that are defined in the component schemas.

    The required state_ref attribute specifies the id of the OVAL State
    being referenced.
    """

    state_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:ste:[1-9][0-9]*",
        },
    )
