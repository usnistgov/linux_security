from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class DnscacheItem:
    """
    The dnscache_item stores information retrieved from the DNS cache about a
    domain name, its time to live, and its corresponding IP addresses.

    :ivar domain_name: The domain_name element contains a string that
        represents a domain name that was collected from the DNS cache
        on the local system.
    :ivar ttl: The ttl element contains an integer that represents the
        time to live in seconds of the DNS cache entry.
    :ivar ip_address: The ip_address element contains a string that
        represents an IP address associated with the specified domain
        name. Note that the IP address can be IPv4 or IPv6.
    """

    class Meta:
        name = "dnscache_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    domain_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ttl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ip_address: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
