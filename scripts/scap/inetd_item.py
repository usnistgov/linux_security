from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_endpoint_type import EntityItemEndpointType
from scap.entity_item_wait_status_type import EntityItemWaitStatusType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class InetdItem:
    """The inetd item holds information associated with different Internet
    services.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar protocol: A recognized protocol listed in the file
        /etc/inet/protocols.
    :ivar service_name: The name of a valid service listed in the
        services file. For RPC services, the value of the service-name
        field consists of the RPC service name or program number,
        followed by a '/' (slash) and either a version number or a range
        of version numbers (for example, rstatd/2-4).
    :ivar server_program: Either the pathname of a server program to be
        invoked by inetd to perform the requested service, or the value
        internal if inetd itself provides the service.
    :ivar server_arguments: The arguments for running the service.
        These are either passed to the server program invoked by inetd,
        or used to configure a service provided by inetd.  In the case
        of server programs, the arguments shall begin with argv[0],
        which is typically the name of the program.  In the case of a
        service provided by inted, the first argument shall be the word
        "internal".
    :ivar endpoint_type: The endpoint type (aka, socket type) associated
        with the service.
    :ivar exec_as_user: The user id of the user the server program
        should run under.  (This allows for running with less permission
        than root.)
    :ivar wait_status: This field has values wait or nowait. This entry
        specifies whether the server that is invoked by inetd will take
        over the listening socket associated with the service, and
        whether once launched, inetd will wait for that server to exit,
        if ever, before it resumes listening for new service requests.
    """

    class Meta:
        name = "inetd_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    server_program: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    server_arguments: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    endpoint_type: Optional[EntityItemEndpointType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exec_as_user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    wait_status: Optional[EntityItemWaitStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
