from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_ipaddress_type_datatype import (
    EntityObjectIpaddressTypeDatatype,
)
from scap.entity_simple_base_type import EntitySimpleBaseType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityObjectIpaddressType(EntitySimpleBaseType):
    """The EntityObjectIPAddressType type is extended by the entities of an
    individual OVAL Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes any IPv4/IPv6 address or address prefix.
    """

    class Meta:
        name = "EntityObjectIPAddressType"

    value: str = field(default="")
    datatype: Optional[EntityObjectIpaddressTypeDatatype] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
