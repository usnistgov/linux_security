from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_ipaddress_string_type import (
    EntityStateIpaddressStringType,
)
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class DnscacheState(StateType):
    """
    The dnscache_state contains three entities that are used to check the domain
    name, time to live, and IP addresses associated with the DNS cache entry.

    :ivar domain_name: The domain_name element contains a string that
        represents a domain name that was collected from the DNS cache
        on the local system.
    :ivar ttl: The ttl element contains an integer that represents the
        time to live in seconds of the DNS cache entry.
    :ivar ip_address: The ip_address element contains a string that
        represents an IP address associated with the specified domain
        name that was collected from the DNS cache on the local system.
        Note that the IP address can be IPv4 or IPv6.
    """

    class Meta:
        name = "dnscache_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    domain_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ttl: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ip_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
