from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Environmentvariable58State(StateType):
    """
    The environmentvariable58_state element contains three entities that are used
    to check the name of the specified environment variable, the process ID of the
    process from which the environment variable was retrieved, and the value
    associated with the environment variable.

    :ivar pid: The process ID of the process from which the environment
        variable was retrieved.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
