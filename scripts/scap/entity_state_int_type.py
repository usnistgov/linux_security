from dataclasses import dataclass, field
from typing import Union

from scap.entity_state_simple_base_type import EntityStateSimpleBaseType
from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateIntType(EntityStateSimpleBaseType):
    """The EntityStateIntType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple integer data. The empty string is also allowed
    when using a variable reference with an element.
    """

    value: Union[int, str] = field(
        default="",
        metadata={
            "max_length": 0,
        },
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.INT,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
