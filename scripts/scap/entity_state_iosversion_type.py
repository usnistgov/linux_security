from dataclasses import dataclass, field

from scap.entity_state_iosversion_type_datatype import (
    EntityStateIosversionTypeDatatype,
)
from scap.entity_state_simple_base_type import EntityStateSimpleBaseType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateIosversionType(EntityStateSimpleBaseType):
    """The EntityStateIOSVersionType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type represents the version string related to CISCO IOS.
    """

    class Meta:
        name = "EntityStateIOSVersionType"

    value: str = field(default="")
    datatype: EntityStateIosversionTypeDatatype = field(
        default=EntityStateIosversionTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )
