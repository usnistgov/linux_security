from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_variable_ref_type import EntityStateVariableRefType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class VariableState(StateType):
    """
    The variable_state element contains two entities that are used to check the
    var_ref of the specified varible and the value associated with it.

    :ivar var_ref: The id of the variable.
    :ivar value: The value of the variable.
    """

    class Meta:
        name = "variable_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    var_ref: Optional[EntityStateVariableRefType] = field(
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
