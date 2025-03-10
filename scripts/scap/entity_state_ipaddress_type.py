from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_ipaddress_type_datatype import (
    EntityStateIpaddressTypeDatatype,
)
from scap.entity_state_simple_base_type import EntityStateSimpleBaseType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateIpaddressType(EntityStateSimpleBaseType):
    """The EntityStateIPAddressType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each object entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes any IPv4/IPv6 address or address prefix.
    """

    class Meta:
        name = "EntityStateIPAddressType"

    value: str = field(default="")
    datatype: Optional[EntityStateIpaddressTypeDatatype] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
