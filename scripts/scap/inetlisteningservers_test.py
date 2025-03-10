from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class InetlisteningserversTest(TestType):
    """The inet listening servers test is used to check what applications are
    listening on the network.

    This is limited to applications that are listening for connections
    that use the TCP or UDP protocols and have addresses represented as
    IPv4 or IPv6 addresses (AF_INET or AF_INET6). It is generally using
    the parsed output of running the command netstat -tuwlnpe with root
    privilege. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references an
    inetlisteningservers_object and the optional state element specifies
    the data to check.
    """

    class Meta:
        name = "inetlisteningservers_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
