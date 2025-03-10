from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_variable_ref_type import EntityItemVariableRefType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class VariableItem:
    """
    This item stores information about OVAL Variables and their values.

    :ivar var_ref: The id of the variable.
    :ivar value: The value of the variable. If a variable represents and
        array of values, then multiple value elements should exist.
    """

    class Meta:
        name = "variable_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    var_ref: Optional[EntityItemVariableRefType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
