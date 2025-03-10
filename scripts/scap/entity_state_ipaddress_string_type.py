from dataclasses import dataclass, field

from scap.entity_state_ipaddress_string_type_datatype import (
    EntityStateIpaddressStringTypeDatatype,
)
from scap.entity_state_simple_base_type import EntityStateSimpleBaseType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateIpaddressStringType(EntityStateSimpleBaseType):
    """The EntityStateIPAddressStringType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each object entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes any IPv4/IPv6 address, address prefix, or its string
    representation.
    """

    class Meta:
        name = "EntityStateIPAddressStringType"

    value: str = field(default="")
    datatype: EntityStateIpaddressStringTypeDatatype = field(
        default=EntityStateIpaddressStringTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )
