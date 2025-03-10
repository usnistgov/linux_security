from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ObjectRefType:
    """The ObjectRefType complex type defines an object reference to be used by
    OVAL Tests that are defined in the component schemas.

    The required object_ref attribute specifies the id of the OVAL
    Object being referenced.
    """

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
