from dataclasses import dataclass, field

from scap.entity_state_simple_base_type import EntityStateSimpleBaseType
from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateStringType(EntityStateSimpleBaseType):
    """The EntityStateStringType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple string data.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )
