from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EnvironmentvariableState(StateType):
    """
    The environmentvariable_state element contains two entities that are used to
    check the name of the specified environment variable and the value associated
    with it.

    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
