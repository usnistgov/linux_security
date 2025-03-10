from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_bool_type import EntityStateBoolType
from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_ipaddress_string_type import (
    EntityStateIpaddressStringType,
)
from scap.entity_state_string_type import EntityStateStringType
from scap.entity_state_xinetd_type_status_type import (
    EntityStateXinetdTypeStatusType,
)
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class XinetdState(StateType):
    """The xinetd_state element defines the different information associated with a
    specific Internet service.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar protocol: The protocol entity specifies the protocol that is
        used by the service.  The list of valid protocols can be found
        in /etc/protocols.
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
        name = "xinetd_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    protocol: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    service_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flags: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    no_access: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    only_from: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    port: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    server: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    server_arguments: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    socket_type: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[EntityStateXinetdTypeStatusType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    user: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    wait: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    disabled: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
