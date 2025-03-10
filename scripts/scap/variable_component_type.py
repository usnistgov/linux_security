from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class VariableComponentType:
    """The VariableComponentType complex type defines a specific value obtained by
    looking at the value of another OVAL Variable.

    The required var_ref attribute provides a reference to the variable.
    One must make sure that the variable reference does not point to the
    parent variable that uses this component to avoid a race condition.
    """

    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )
