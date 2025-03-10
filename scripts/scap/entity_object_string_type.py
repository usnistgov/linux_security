from dataclasses import dataclass, field

from scap.entity_simple_base_type import EntitySimpleBaseType
from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityObjectStringType(EntitySimpleBaseType):
    """The EntityStringType type is extended by the entities of an individual OVAL
    Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes simple string data.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )
