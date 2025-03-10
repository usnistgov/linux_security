from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_interface_type import EntityStateInterfaceType
from scap.entity_state_ipaddress_string_type import (
    EntityStateIpaddressStringType,
)
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class InterfaceState(StateType):
    """The interface_state element enumerates the different properties associate
    with a Unix interface.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar name: The name element is the interface (eth0, eth1, fw0,
        etc.) name to check.
    :ivar type_value: The type element specifies the type of interface.
    :ivar hardware_addr: The hardware_addr element is the hardware or
        MAC address of the physical network card. MAC addresses should
        be formatted according to the IEEE 802-2001 standard which
        states that a MAC address is a sequence of six octet values,
        separated by hyphens, where each octet is represented by two
        hexadecimal digits.  Uppercase letters should also be used to
        represent the hexadecimal digits A through F.
    :ivar inet_addr: This is the IP address of the interface. Note that
        the IP address can be IPv4 or IPv6. If the IP address is an IPv6
        address, this entity will be expressed as an IPv6 address prefix
        using CIDR notation and the netmask entity will not be
        collected.
    :ivar broadcast_addr: This is the broadcast IP address for this
        interface's network. Note that the IP address can be IPv4 or
        IPv6.
    :ivar netmask: This is the bitmask used to calculate the interface's
        IP network. The network number is calculated by bitwise-ANDing
        this with the IP address. The host number on that network is
        calculated by bitwise-XORing this with the IP address.  Note
        that if the inet_addr entity contains an IPv6 address prefix,
        this entity will not be collected.
    :ivar flag: The flag entity represents the interface flag line,
        which generally contains flags like "UP" to denote an active
        interface, "PROMISC" to note that the interface is listening for
        Ethernet frames not specifically addressed to it, and others.
        This element can be included multiple times in a system
        characteristic item in order to record a multitude of flags.
        Note that the entity_check attribute associated with
        EntityStateStringType guides the evaluation of entities like
        this that refer to items that can occur an unbounded number of
        times.
    """

    class Meta:
        name = "interface_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[EntityStateInterfaceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    hardware_addr: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    inet_addr: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    broadcast_addr: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    netmask: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flag: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
