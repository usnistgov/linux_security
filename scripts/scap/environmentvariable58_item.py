from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class Environmentvariable58Item:
    """
    This item stores information about an environment variable, the process ID of
    the process from which it was retrieved, and its corresponding value.

    :ivar pid: The process ID of the process from which the environment
        variable was retrieved.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable58_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
