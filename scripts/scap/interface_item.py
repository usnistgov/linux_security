from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_interface_type import EntityItemInterfaceType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class InterfaceItem:
    """The interface item holds information about the interfaces on a system.

    Each interface item contains name and address information as well as
    any associated flags. It extends the standard ItemType as defined in
    the oval-system-characteristics schema and one should refer to the
    ItemType description for more information.

    :ivar name: The name entity is the actual name of the specific
        interface. Examples might be eth0, eth1, fwo, etc.
    :ivar type_value: This element specifies the type of interface.
    :ivar hardware_addr: The hardware_addr entity is the hardware or MAC
        address of the physical network card. MAC addresses should be
        formatted according to the IEEE 802-2001 standard which states
        that a MAC address is a sequence of six octet values, separated
        by hyphens, where each octet is represented by two hexadecimal
        digits.  Uppercase letters should also be used to represent the
        hexadecimal digits A through F.
    :ivar inet_addr: The inet_addr entity is the IP address of the
        specific interface. Note that the IP address can be IPv4 or
        IPv6. If the IP address is an IPv6 address, this entity should
        be expressed as an IPv6 address prefix using CIDR notation and
        the netmask entity should not be collected.
    :ivar broadcast_addr: The broadcast_addr entity is the broadcast IP
        address for this interface's network. Note that the IP address
        can be IPv4 or IPv6.
    :ivar netmask: This is the bitmask used to calculate the interface's
        IP network. The network number is calculated by bitwise-ANDing
        this with the IP address. The host number on that network is
        calculated by bitwise-XORing this with the IP address. Note that
        if the inet_addr entity contains an IPv6 address prefix, this
        entity should not be collected.
    :ivar flag: This is the interface flag line, which generally
        contains flags like "UP" to denote an active interface,
        "PROMISC" to note that the interface is listening for Ethernet
        frames not specifically addressed to it, and others.
    """

    class Meta:
        name = "interface_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[EntityItemInterfaceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    hardware_addr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    inet_addr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    broadcast_addr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    netmask: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flag: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
