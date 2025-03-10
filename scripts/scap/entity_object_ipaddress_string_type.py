from dataclasses import dataclass, field

from scap.entity_object_ipaddress_string_type_datatype import (
    EntityObjectIpaddressStringTypeDatatype,
)
from scap.entity_simple_base_type import EntitySimpleBaseType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityObjectIpaddressStringType(EntitySimpleBaseType):
    """The EntityObjectIPAddressStringType type is extended by the entities of an
    individual OVAL Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes any IPv4/IPv6 address, address prefix, or its string
    representation.
    """

    class Meta:
        name = "EntityObjectIPAddressStringType"

    value: str = field(default="")
    datatype: EntityObjectIpaddressStringTypeDatatype = field(
        default=EntityObjectIpaddressStringTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )
