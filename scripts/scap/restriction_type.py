from dataclasses import dataclass, field
from typing import Optional

from scap.operation_enumeration import OperationEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class RestrictionType:
    """The RestrictionType complex type outlines a restriction that is placed on
    expected values for an external variable.

    For example, a possible value may be restricted to a integer less
    than 10. Please refer to the operationEnumeration simple type for a
    description of the valid operations.
    """

    value: Optional[object] = field(default=None)
    operation: Optional[OperationEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
