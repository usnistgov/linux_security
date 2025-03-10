from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_xinetd_type_status_type import (
    EntityItemXinetdTypeStatusType,
)

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class XinetdItem:
    """The xinetd item holds information associated with different Internet
    services.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar protocol: The protocol entity specifies the protocol that is
        used by the service. The list of valid protocols can be found in
        /etc/protocols.
    :ivar service_name: The service_name entity specifies the name of
        the service.
    :ivar flags: The flags entity specifies miscellaneous settings
        associated with the service.
    :ivar no_access: The no_access entity specifies the remote hosts to
        which the service is unavailable.  Please see the xinetd.conf(5)
        man page for information on the different formats that can be
        used to describe a host.
    :ivar only_from: The only_from entity specifies the remote hosts to
        which the service is available.  Please see the xinetd.conf(5)
        man page for information on the different formats that can be
        used to describe a host.
    :ivar port: The port entity specifies the port used by the service.
    :ivar server: The server entity specifies the executable that is
        used to launch the service.
    :ivar server_arguments: The server_arguments entity specifies the
        arguments that are passed to the executable when launching the
        service.
    :ivar socket_type: The socket_type entity specifies the type of
        socket that is used by the service.  Possible values include:
        stream, dgram, raw, or seqpacket.
    :ivar type_value: The type entity specifies the type of the service.
        A service may have multiple types.
    :ivar user: The user entity specifies the user identifier of the
        process that is running the service.  The user identifier may be
        expressed as a numerical value or as a user name that exists in
        /etc/passwd.
    :ivar wait: The wait entity specifies whether or not the service is
        single-threaded or multi-threaded and whether or not xinetd
        accepts the connection or the service accepts the connection.  A
        value of 'true' indicates that the service is single-threaded
        and the service will accept the connection.  A value of 'false'
        indicates that the service is multi-threaded and xinetd will
        accept the connection.
    :ivar disabled: The disabled entity specifies whether or not the
        service is disabled.  A value of 'true' indicates that the
        service is disabled and will not start.  A value of 'false'
        indicates that the service is not disabled.
    """

    class Meta:
        name = "xinetd_item"
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
    flags: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    no_access: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    only_from: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    port: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    server: Optional[str] = field(
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
    socket_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: list[EntityItemXinetdTypeStatusType] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    wait: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    disabled: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
