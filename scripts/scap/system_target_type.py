from dataclasses import dataclass, field
from typing import Optional

from scap.named_item_base_type import NamedItemBaseType
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SystemTargetType(NamedItemBaseType):
    """
    The SystemTargetType type defines structures containing information about the
    organization it belongs to, a set of ip addresses of computers/networks
    included in the system, descrioption about it, and the roles it performs.

    :ivar organization: The organization element specifies what company
        or institution the system belongs to.
    :ivar ipaddress: The ipaddress element holds the ip address of a
        target computer/network. TODO: define an IPv4/v6 address pattern
    :ivar description: The description element holds information on what
        the target system is about.
    """

    organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    ipaddress: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    description: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
