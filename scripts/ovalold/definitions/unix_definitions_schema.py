from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


class EntityStateCapabilityType(Enum):
    """The EntityStateCapabilityType complex type restricts a string value to a
    specific set of values that describe POSIX capability types associated with a
    process service.

    This list is based off the values defined in
    linux/include/linux/capability.h. Documentation on each allowed
    value can be found in capability.h. The empty string is also allowed
    to support empty elements associated with variable references. Note
    that when using pattern matches and variables care must be taken to
    ensure that the regular expression and variable values align with
    the enumerated values.

    :cvar CAP_CHOWN:
    :cvar CAP_DAC_OVERRIDE:
    :cvar CAP_DAC_READ_SEARCH:
    :cvar CAP_FOWNER:
    :cvar CAP_FSETID:
    :cvar CAP_KILL:
    :cvar CAP_SETGID:
    :cvar CAP_SETUID:
    :cvar CAP_SETPCAP:
    :cvar CAP_LINUX_IMMUTABLE:
    :cvar CAP_NET_BIND_SERVICE:
    :cvar CAP_NET_BROADCAST:
    :cvar CAP_NET_ADMIN:
    :cvar CAP_NET_RAW:
    :cvar CAP_IPC_LOCK:
    :cvar CAP_IPC_OWNER:
    :cvar CAP_SYS_MODULE:
    :cvar CAP_SYS_RAWIO:
    :cvar CAP_SYS_CHROOT:
    :cvar CAP_SYS_PTRACE:
    :cvar CAP_SYS_ADMIN:
    :cvar CAP_SYS_BOOT:
    :cvar CAP_SYS_NICE:
    :cvar CAP_SYS_RESOURCE:
    :cvar CAP_SYS_TIME:
    :cvar CAP_SYS_TTY_CONFIG:
    :cvar CAP_MKNOD:
    :cvar CAP_LEASE:
    :cvar CAP_AUDIT_WRITE:
    :cvar CAP_AUDIT_CONTROL:
    :cvar CAP_SETFCAP:
    :cvar CAP_MAC_OVERRIDE:
    :cvar CAP_MAC_ADMIN:
    :cvar CAP_SYS_PACCT:
    :cvar CAP_SYSLOG:
    :cvar CAP_WAKE_ALARM:
    :cvar CAP_BLOCK_SUSPEND:
    :cvar CAP_AUDIT_READ:
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    CAP_CHOWN = "CAP_CHOWN"
    CAP_DAC_OVERRIDE = "CAP_DAC_OVERRIDE"
    CAP_DAC_READ_SEARCH = "CAP_DAC_READ_SEARCH"
    CAP_FOWNER = "CAP_FOWNER"
    CAP_FSETID = "CAP_FSETID"
    CAP_KILL = "CAP_KILL"
    CAP_SETGID = "CAP_SETGID"
    CAP_SETUID = "CAP_SETUID"
    CAP_SETPCAP = "CAP_SETPCAP"
    CAP_LINUX_IMMUTABLE = "CAP_LINUX_IMMUTABLE"
    CAP_NET_BIND_SERVICE = "CAP_NET_BIND_SERVICE"
    CAP_NET_BROADCAST = "CAP_NET_BROADCAST"
    CAP_NET_ADMIN = "CAP_NET_ADMIN"
    CAP_NET_RAW = "CAP_NET_RAW"
    CAP_IPC_LOCK = "CAP_IPC_LOCK"
    CAP_IPC_OWNER = "CAP_IPC_OWNER"
    CAP_SYS_MODULE = "CAP_SYS_MODULE"
    CAP_SYS_RAWIO = "CAP_SYS_RAWIO"
    CAP_SYS_CHROOT = "CAP_SYS_CHROOT"
    CAP_SYS_PTRACE = "CAP_SYS_PTRACE"
    CAP_SYS_ADMIN = "CAP_SYS_ADMIN"
    CAP_SYS_BOOT = "CAP_SYS_BOOT"
    CAP_SYS_NICE = "CAP_SYS_NICE"
    CAP_SYS_RESOURCE = "CAP_SYS_RESOURCE"
    CAP_SYS_TIME = "CAP_SYS_TIME"
    CAP_SYS_TTY_CONFIG = "CAP_SYS_TTY_CONFIG"
    CAP_MKNOD = "CAP_MKNOD"
    CAP_LEASE = "CAP_LEASE"
    CAP_AUDIT_WRITE = "CAP_AUDIT_WRITE"
    CAP_AUDIT_CONTROL = "CAP_AUDIT_CONTROL"
    CAP_SETFCAP = "CAP_SETFCAP"
    CAP_MAC_OVERRIDE = "CAP_MAC_OVERRIDE"
    CAP_MAC_ADMIN = "CAP_MAC_ADMIN"
    CAP_SYS_PACCT = "CAP_SYS_PACCT"
    CAP_SYSLOG = "CAP_SYSLOG"
    CAP_WAKE_ALARM = "CAP_WAKE_ALARM"
    CAP_BLOCK_SUSPEND = "CAP_BLOCK_SUSPEND"
    CAP_AUDIT_READ = "CAP_AUDIT_READ"
    VALUE = ""


class EntityStateEncryptMethodType(Enum):
    """The EntityStateEncryptMethodType complex type restricts a string value to a
    set that corresponds to the allowed encrypt methods used for protected
    passwords in a shadow file.

    The empty string is also allowed to support empty element associated
    with variable references.  Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.

    :cvar DES: The DES method corresponds to the (none) prefix.
    :cvar BSDI: The BSDi method corresponds to BSDi modified DES or the
        '_' prefix.
    :cvar MD5: The MD5 method corresponds to MD5 for Linux/BSD or the
        $1$ prefix.
    :cvar BLOWFISH: The Blowfish method corresponds to Blowfish
        (OpenBSD) or the $2$ or $2a$ prefixes.
    :cvar SUN_MD5: The Sun MD5 method corresponds to the $md5$ prefix.
    :cvar SHA_256: The SHA-256 method corresponds to the $5$ prefix.
    :cvar SHA_512: The SHA-512 method corresponds to the $6$ prefix.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    DES = "DES"
    BSDI = "BSDi"
    MD5 = "MD5"
    BLOWFISH = "Blowfish"
    SUN_MD5 = "Sun MD5"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"
    VALUE = ""


class EntityStateEndpointType(Enum):
    """The EntityStateEndpointType complex type restricts a string value to a
    specific set of values that describe endpoint types associated with an Internet
    service.

    The empty string is also allowed to support empty elements
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar STREAM: The stream value is used to describe a stream socket.
    :cvar DGRAM: The dgram value is used to describe a datagram socket.
    :cvar RAW: The raw value is used to describe a raw socket.
    :cvar SEQPACKET: The seqpacket value is used to describe a sequenced
        packet socket.
    :cvar TLI: The tli value is used to describe all TLI endpoints.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    STREAM = "stream"
    DGRAM = "dgram"
    RAW = "raw"
    SEQPACKET = "seqpacket"
    TLI = "tli"
    VALUE = ""


class EntityStateGconfTypeType(Enum):
    """The EntityStateGconfTypeType complex type restricts a string value to the
    seven values GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
    GCONF_VALUE_BOOL, GCONF_VALUE_SCHEMA, GCONF_VALUE_LIST, and GCONF_VALUE_PAIR
    that specify the datatype of the value associated with a GConf preference key.

    The empty string is also allowed to support empty elements
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar GCONF_VALUE_STRING: The GCONF_VALUE_STRING type is used to
        describe a preference key that has a string value.
    :cvar GCONF_VALUE_INT: The GCONF_VALUE_INT type is used to describe
        a preference key that has a integer value.
    :cvar GCONF_VALUE_FLOAT: The GCONF_VALUE_FLOAT type is used to
        describe a preference key that has a float value.
    :cvar GCONF_VALUE_BOOL: The GCONF_VALUE_BOOL type is used to
        describe a preference key that has a boolean value.
    :cvar GCONF_VALUE_SCHEMA: The GCONF_VALUE_SCHEMA type is used to
        describe a preference key that has a schema value. The actual
        value will be the default value as specified in the GConf
        schema.
    :cvar GCONF_VALUE_LIST: The GCONF_VALUE_LIST type is used to
        describe a preference key that has a list of values. The actual
        values will be one of the primitive GConf datatypes
        GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
        GCONF_VALUE_BOOL, and GCONF_VALUE_SCHEMA. Note that all of the
        values associated with a GCONF_VALUE_LIST are required to have
        the same type.
    :cvar GCONF_VALUE_PAIR: The GCONF_VALUE_PAIR type is used to
        describe a preference key that has a pair of values. The actual
        values will consist of the primitive GConf datatypes
        GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
        GCONF_VALUE_BOOL, and GCONF_VALUE_SCHEMA. Note that the values
        associated with a GCONF_VALUE_PAIR are not required to have the
        same type.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    GCONF_VALUE_STRING = "GCONF_VALUE_STRING"
    GCONF_VALUE_INT = "GCONF_VALUE_INT"
    GCONF_VALUE_FLOAT = "GCONF_VALUE_FLOAT"
    GCONF_VALUE_BOOL = "GCONF_VALUE_BOOL"
    GCONF_VALUE_SCHEMA = "GCONF_VALUE_SCHEMA"
    GCONF_VALUE_LIST = "GCONF_VALUE_LIST"
    GCONF_VALUE_PAIR = "GCONF_VALUE_PAIR"
    VALUE = ""


class EntityStateInterfaceType(Enum):
    """The EntityStateInterfaceType complex type restricts a string value to a
    specific set of values.

    These values describe the different interface types which are
    defined in 'if_arp.h'. The empty string is also allowed to support
    empty element associated with variable references. Note that when
    using pattern matches and variables care must be taken to ensure
    that the regular expression and variable values align with the
    enumerated values.

    :cvar ARPHRD_ETHER: The ARPHRD_ETHER type is used to describe
        ethernet interfaces.
    :cvar ARPHRD_FDDI: The ARPHRD_FDDI type is used to describe fiber
        distributed data interfaces (FDDI).
    :cvar ARPHRD_LOOPBACK: The ARPHRD_LOOPBACK type is used to describe
        loopback interfaces.
    :cvar ARPHRD_VOID: The ARPHRD_VOID type is used to describe unknown
        interfaces.
    :cvar ARPHRD_PPP: The ARPHRD_PPP type is used to describe point-to-
        point protocol interfaces (PPP).
    :cvar ARPHRD_SLIP: The ARPHRD_SLIP type is used to describe serial
        line internet protocol interfaces (SLIP).
    :cvar ARPHRD_PRONET: The ARPHRD_PRONET type is used to describe
        PROnet token ring interfaces.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    ARPHRD_ETHER = "ARPHRD_ETHER"
    ARPHRD_FDDI = "ARPHRD_FDDI"
    ARPHRD_LOOPBACK = "ARPHRD_LOOPBACK"
    ARPHRD_VOID = "ARPHRD_VOID"
    ARPHRD_PPP = "ARPHRD_PPP"
    ARPHRD_SLIP = "ARPHRD_SLIP"
    ARPHRD_PRONET = "ARPHRD_PRONET"
    VALUE = ""


class EntityStateRoutingTableFlagsType(Enum):
    """The EntityStateRoutingTableFlagsType complex type restricts a string value
    to a specific set of values that describe the flags associated with a routing
    table entry.

    This list is based off the values defined in the man pages of
    various platforms. For Linux, please see route(8). For Solaris,
    please see netstat(1M). For HP-UX, please see netstat(1). For Mac
    OS, please see netstat(1). For FreeBSD, please see netstat(1).
    Documentation on each allowed value can be found in the previously
    listed man pages. The empty string is also allowed to support empty
    elements associated with variable references. Note that when using
    pattern matches and variables care must be taken to ensure that the
    regular expression and variable values align with the enumerated
    values.

    :cvar UP:
    :cvar GATEWAY:
    :cvar HOST:
    :cvar REINSTATE:
    :cvar DYNAMIC:
    :cvar MODIFIED:
    :cvar ADDRCONF:
    :cvar CACHE:
    :cvar REJECT:
    :cvar REDUNDANT:
    :cvar SETSRC:
    :cvar BROADCAST:
    :cvar LOCAL:
    :cvar PROTOCOL_1:
    :cvar PROTOCOL_2:
    :cvar PROTOCOL_3:
    :cvar BLACK_HOLE:
    :cvar CLONING:
    :cvar PROTOCOL_CLONING:
    :cvar INTERFACE_SCOPE:
    :cvar LINK_LAYER:
    :cvar MULTICAST:
    :cvar STATIC:
    :cvar WAS_CLONED:
    :cvar XRESOLVE:
    :cvar USABLE:
    :cvar PINNED:
    :cvar ACTIVE_DEAD_GATEWAY_DETECTION:
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    UP = "UP"
    GATEWAY = "GATEWAY"
    HOST = "HOST"
    REINSTATE = "REINSTATE"
    DYNAMIC = "DYNAMIC"
    MODIFIED = "MODIFIED"
    ADDRCONF = "ADDRCONF"
    CACHE = "CACHE"
    REJECT = "REJECT"
    REDUNDANT = "REDUNDANT"
    SETSRC = "SETSRC"
    BROADCAST = "BROADCAST"
    LOCAL = "LOCAL"
    PROTOCOL_1 = "PROTOCOL_1"
    PROTOCOL_2 = "PROTOCOL_2"
    PROTOCOL_3 = "PROTOCOL_3"
    BLACK_HOLE = "BLACK_HOLE"
    CLONING = "CLONING"
    PROTOCOL_CLONING = "PROTOCOL_CLONING"
    INTERFACE_SCOPE = "INTERFACE_SCOPE"
    LINK_LAYER = "LINK_LAYER"
    MULTICAST = "MULTICAST"
    STATIC = "STATIC"
    WAS_CLONED = "WAS_CLONED"
    XRESOLVE = "XRESOLVE"
    USABLE = "USABLE"
    PINNED = "PINNED"
    ACTIVE_DEAD_GATEWAY_DETECTION = "ACTIVE_DEAD_GATEWAY_DETECTION"
    VALUE = ""


class EntityStateWaitStatusType(Enum):
    """The EntityStateWaitStatusType complex type restricts a string value to two
    values, either wait or nowait, that specify whether the server that is invoked
    by inetd will take over the listening socket associated with the service, and
    whether once launched, inetd will wait for that server to exit, if ever, before
    it resumes listening for new service requests.

    The empty string is also allowed to support empty elements
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar WAIT: The value of 'wait' specifies that the server that is
        invoked by inetd will take over the listening socket associated
        with the service, and once launched, inetd will wait for that
        server to exit, if ever, before it resumes listening for new
        service requests.
    :cvar NOWAIT: The value of 'nowait' specifies that the server that
        is invoked by inetd will not wait for any existing server to
        finish before taking over the listening socket associated with
        the service.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    WAIT = "wait"
    NOWAIT = "nowait"
    VALUE = ""


class EntityStateXinetdTypeStatusType(Enum):
    """The EntityStateXinetdTypeStatusType complex type restricts a string value to
    five values, either RPC, INTERNAL, UNLISTED, TCPMUX, or TCPMUXPLUS that specify
    the type of service registered in xinetd.

    The empty string is also allowed to support empty elements
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar INTERNAL: The INTERNAL type is used to describe services like
        echo, chargen, and others whose functionality is supplied by
        xinetd itself.
    :cvar RPC: The RPC type is used to describe services that use remote
        procedure call ala NFS.
    :cvar UNLISTED: The UNLISTED type is used to describe services that
        aren't listed in /etc/protocols or /etc/rpc.
    :cvar TCPMUX: The TCPMUX type is used to describe services that
        conform to RFC 1078. This type indiciates that the service is
        responsible for handling the protocol handshake.
    :cvar TCPMUXPLUS: The TCPMUXPLUS type is used to describe services
        that conform to RFC 1078. This type indicates that xinetd is
        responsible for handling the protocol handshake.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    INTERNAL = "INTERNAL"
    RPC = "RPC"
    UNLISTED = "UNLISTED"
    TCPMUX = "TCPMUX"
    TCPMUXPLUS = "TCPMUXPLUS"
    VALUE = ""


class FileBehaviorsRecurse(Enum):
    NONE = "none"
    FILES = "files"
    DIRECTORIES = "directories"
    FILES_AND_DIRECTORIES = "files and directories"
    SYMLINKS = "symlinks"
    SYMLINKS_AND_DIRECTORIES = "symlinks and directories"


class FileBehaviorsRecurseDirection(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"


class FileBehaviorsRecurseFileSystem(Enum):
    ALL = "all"
    LOCAL = "local"
    DEFINED = "defined"


@dataclass
class DnscacheObject:
    """The dnscache_object is used by the dnscache_test to specify the domain
    name(s) that should be collected from the DNS cache on the local system.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar domain_name: The domain_name element specifies the domain
        name(s) that should be collected from the DNS cache on the local
        system.
    :ivar filter:
    """

    class Meta:
        name = "dnscache_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    domain_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class DnscacheState:
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

    domain_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ttl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ip_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class DnscacheTest:
    """The dnscache_test is used to check the time to live and IP addresses
    associated with a domain name.

    The time to live and IP addresses for a particular domain name are
    retrieved from the DNS cache on the local system. It extends the
    standard TestType as defined in the oval-definitions-schema and one
    should refer to the TestType description for more information. The
    required object element references a dnscache_object and the
    optional state element specifies the metadata to check.
    """

    class Meta:
        name = "dnscache_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileState:
    """The file_state element defines the different metadata associate with a UNIX
    file.

    This includes the path, filename, type, group id, user id, size,
    etc. In addition, the permission associated with the file are also
    included. Please refer to the individual elements in the schema for
    more details about what each represents.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar type_value: This is the file's type: regular file (regular),
        directory, named pipe (fifo), symbolic link, socket or block
        special.
    :ivar group_id: The group_id entity represents the group owner of a
        file, by group number.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. This element represents the
        owner of the file.
    :ivar a_time: This is the time that the file was last accessed, in
        seconds since the Unix epoch. The Unix epoch is the time
        00:00:00 UTC on January 1, 1970.
    :ivar c_time: This is the time of the last change to the file's
        inode, in seconds since the Unix epoch. The Unix epoch is the
        time 00:00:00 UTC on January 1, 1970. An inode is a Unix data
        structure that stores all of the information about a particular
        file.
    :ivar m_time: This is the time of the last change to the file's
        contents, in seconds since the Unix epoch. The Unix epoch is the
        time 00:00:00 UTC on January 1, 1970.
    :ivar size: This is the size of the file in bytes.
    :ivar suid: Does the program run with the uid (thus privileges) of
        the file's owner, rather than the calling user?
    :ivar sgid: Does the program run with the gid (thus privileges) of
        the file's group owner, rather than the calling user's group?
    :ivar sticky: Can users delete each other's files in this directory,
        when said directory is writable by those users?
    :ivar uread: Can the owner (user owner) of the file read this file
        or, if a directory, read the directory contents?
    :ivar uwrite: Can the owner (user owner) of the file write to this
        file or, if a directory, write to the directory?
    :ivar uexec: Can the owner (user owner) of the file execute it or,
        if a directory, change into the directory?
    :ivar gread: Can the group owner of the file read this file or, if a
        directory, read the directory contents?
    :ivar gwrite: Can the group owner of the file write to this file or,
        if a directory, write to the directory?
    :ivar gexec: Can the group owner of the file execute it or, if a
        directory, change into the directory?
    :ivar oread: Can all other users read this file or, if a directory,
        read the directory contents?
    :ivar owrite: Can the other users write to this file or, if a
        directory, write to the directory?
    :ivar oexec: Can the other users execute this file or, if a
        directory, change into the directory?
    :ivar has_extended_acl: Does the file or directory have ACL
        permissions applied to it? If the file or directory doesn't have
        an ACL, or it matches the standard UNIX permissions, the value
        will be 'false'. Otherwise, if a file or directory has an ACL,
        the value will be 'true'.
    """

    class Meta:
        name = "file_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    group_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    m_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    suid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sgid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sticky: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uread: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uwrite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uexec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gread: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gwrite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gexec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    oread: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    owrite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    oexec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    has_extended_acl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileTest:
    """The file test is used to check metadata associated with UNIX files, of the
    sort returned by either an ls command, stat command or stat() system call.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a file_object
    and the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "file_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileextendedattributeState:
    """The fileextendedattribute_state element defines an extended attribute
    associated with a UNIX file.

    This includes the path, filename, attribute name, and attribute
    value.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory can be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar attribute_name: This is the extended attribute's name,
        identifier or key.
    :ivar value: The value entity represents the extended attribute's
        value or contents. To test for an attribute with no value
        assigned to it, this entity would be used with an empty value.
    """

    class Meta:
        name = "fileextendedattribute_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileextendedattributeTest:
    """The file extended attribute test is used to check extended attribute values
    associated with UNIX files, of the sort returned by the getfattr command or
    getxattr() system call.

    It extends the standard TestType as defined in the oval-definitions-schema and one should refer to the TestType description for more information. The required object element references a fileextendedattribute_object and the optional state element specifies the extended attributes to check.
    NOTE: Solaris has a very different implementation of "extended attributes" in which the attributes are really an orthogonal directory hierarchy of files. See the Solaris documentation for more details. The file extended attribute test only handles simple name/value pairs as implemented by most other UNIX derived operating systems.
    """

    class Meta:
        name = "fileextendedattribute_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GconfObject:
    """The gconf_object element is used by a gconf_test to define the preference
    keys to collect and the sources from which to collect the preference keys.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar key: This is the preference key to check.
    :ivar source: The source element specifies the source from which to
        collect the preference key. The source is represented by the
        absolute path to a GConf XML file as XML is the current backend
        for GConf.  Note that other backends may become available in the
        future. If the xsi:nil attribute is set to 'true', the
        preference key is looked up using the GConf daemon. Otherwise,
        the preference key is looked up using the values specified in
        this entity.
    :ivar filter:
    """

    class Meta:
        name = "gconf_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class GconfTest:
    """The gconf_test is used to check the attributes and value(s) associated with
    GConf preference keys.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a gconf_object
    and the optional gconf_state element specifies the data to check.
    """

    class Meta:
        name = "gconf_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InetdObject:
    """The inetd_object element is used by an inetd test to define the specific
    protocol-service to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An inetd object consists of a protocol entity
    and a service_name entity that identifies the specific service to be
    tested.

    :ivar set:
    :ivar protocol: A recognized protocol listed in the file
        /etc/inet/protocols.
    :ivar service_name: The name of a valid service listed in the
        services file. For RPC services, the value of the service-name
        field consists of the RPC service name or program number,
        followed by a '/' (slash) and either a version number or a range
        of version numbers (for example, rstatd/2-4).
    :ivar filter:
    """

    class Meta:
        name = "inetd_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class InetdTest:
    """The inetd test is used to check information associated with different
    Internet services.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an inetd_object
    and the optional state element specifies the information to check.
    """

    class Meta:
        name = "inetd_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InterfaceObject:
    """The interface_object element is used by an interface test to define the
    specific interfaces(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An interface object consists of a single name
    entity that identifies which interface is being specified.

    :ivar set:
    :ivar name: The name element is the interface (eth0, eth1, fw0,
        etc.) name to check.
    :ivar filter:
    """

    class Meta:
        name = "interface_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class InterfaceTest:
    """The interface test enumerates various attributes about the interfaces on a
    system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    interface_object and the optional state element specifies the
    interface information to check.
    """

    class Meta:
        name = "interface_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PasswordObject:
    """The password_object element is used by a password test to define the object
    to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A password object consists of a single username
    entity that identifies the user(s) whose password is to be
    evaluated.

    :ivar set:
    :ivar username: The user(s) account whose password is to be
        evaluated.
    :ivar filter:
    """

    class Meta:
        name = "password_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    username: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class PasswordState:
    """The password_state element defines the different information associated with
    the system passwords.

    Please refer to the individual elements in the schema for more
    details about what each represents. See documentation on /etc/passwd
    for more details on the fields.

    :ivar username: The UNIX account name.
    :ivar password: This is the encrypted version of the user's
        password.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd.
    :ivar group_id: The id of the primary UNIX group the user belongs
        to.
    :ivar gcos: The GECOS (or GCOS) field from /etc/passwd; typically
        contains the user's full name.
    :ivar home_dir: The user's home directory.
    :ivar login_shell: The user's shell program.
    :ivar last_login: The date and time when the last login occurred.
        This value is stored as the number of seconds that have elapsed
        since 00:00:00, January 1, 1970, UTC.
    """

    class Meta:
        name = "password_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    username: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gcos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    home_dir: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    login_shell: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    last_login: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PasswordTest:
    """/etc/passwd.

    See passwd(4). The password test is used to check metadata
    associated with the UNIX password file, of the sort returned by the
    passwd command. It extends the standard TestType as defined in the
    oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a password_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "password_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Process58Object:
    """The process58_object element is used by a process58_test to define the
    specific process(es) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A process58_object defines the command line used
    to start the process(es) and pid.

    :ivar set:
    :ivar command_line: The command_line entity is the string used to
        start the process. This includes any parameters that are part of
        the command line.
    :ivar pid: The pid entity is the process ID of the process.
    :ivar filter:
    """

    class Meta:
        name = "process58_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    command_line: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class Process58Test:
    """The process58_test is used to check information found in the UNIX processes.

    It is equivalent to parsing the output of the ps command. It extends
    the standard TestType as defined in the oval-definitions-schema and
    one should refer to the TestType description for more information.
    The required object element references a process58_object and the
    optional state element references a process58_state that specifies
    the process information to check.
    """

    class Meta:
        name = "process58_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ProcessObject:
    """The process_object element is used by a process test to define the specific
    process(es) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A process object defines the command line used
    to start the process(es).

    :ivar set:
    :ivar command: The command element specifies the command/program
        name to check.
    """

    class Meta:
        name = "process_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    command: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ProcessState:
    """The process_state element defines the different metadata associated with a
    UNIX process.

    This includes the command line, pid, ppid, priority, and user id.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar command: The command element specifies the command/program
        name to check.
    :ivar exec_time: This is the cumulative CPU time, formatted in
        [DD-]HH:MM:SS where DD is the number of days when execution time
        is 24 hours or more.
    :ivar pid: This is the process ID of the process.
    :ivar ppid: This is the process ID of the process's parent process.
    :ivar priority: This is the scheduling priority with which the
        process runs. This can be adjusted with the nice command or
        nice() system call.
    :ivar ruid: This is the real user id which represents the user who
        has created the process.
    :ivar scheduling_class: A platform specific characteristic
        maintained by the scheduler: RT (real-time), TS (timeshare), FF
        (fifo), SYS (system), etc.
    :ivar start_time: This is the time of day the process started
        formatted in HH:MM:SS if the same day the process started or
        formatted as MMM_DD (Ex.: Feb_5) if process started the previous
        day or further in the past.
    :ivar tty: This is the TTY on which the process was started, if
        applicable.
    :ivar user_id: This is the effective user id which represents the
        actual privileges of the process.
    """

    class Meta:
        name = "process_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    command: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ppid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ruid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    scheduling_class: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ProcessTest:
    """The process test is used to check information found in the UNIX processes.

    It is equivalent to parsing the output of the ps command. It extends
    the standard TestType as defined in the oval-definitions-schema and
    one should refer to the TestType description for more information.
    The required object element references a process_object and the
    optional state element specifies the process information to check.
    """

    class Meta:
        name = "process_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RoutingtableObject:
    """The routingtable_object element is used by a routingtable_test to define the
    destination IP address(es), found in a system's primary routing table, to
    collect.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar destination: This is the destination IP address of the routing
        table entry to check.
    :ivar filter:
    """

    class Meta:
        name = "routingtable_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class RoutingtableTest:
    """The routingtable_test is used to check information about the IPv4 and IPv6
    routing table entries found in a system's primary routing table.

    It is important to note that only numerical addresses will be
    collected and that their symbolic representations will not be
    resolved. This equivalent to using the '-n' option with route(8) or
    netstat(8). It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references a
    routingtable_object and the optional routingtable_state element
    specifies the data to check.
    """

    class Meta:
        name = "routingtable_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RunlevelObject:
    """The runlevel_object element is used by a runlevel_test to define the
    specific service(s)/runlevel combination to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar service_name: The service_name entity refers to the name
        associated with a service. This name is usually the filename of
        the script file located in the /etc/init.d directory.
    :ivar runlevel: The system runlevel to examine. A runlevel is
        defined as a software configuration of the system that allows
        only a selected group of processes to exist.
    :ivar filter:
    """

    class Meta:
        name = "runlevel_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    runlevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class RunlevelState:
    """The runlevel_state element holds information about whether a specific
    service is scheduled to start or stop at a given runlevel.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar service_name: The service_name entity refers the name
        associated with a service. This name is usually the filename of
        the script file located in the /etc/init.d directory.
    :ivar runlevel: The runlevel entity refers to the system runlevel
        associated with a service. A runlevel is defined as a software
        configuration of the system that allows only a selected group of
        processes to exist.
    :ivar start: The start entity determines if the process is scheduled
        to be spawned at the specified runlevel.
    :ivar kill: The kill entity determines if the process is supposed to
        be killed at the specified runlevel.
    """

    class Meta:
        name = "runlevel_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    runlevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    kill: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RunlevelTest:
    """The runlevel test is used to check information about which runlevel
    specified services are scheduled to exist at.

    For more information see the output generated by a chkconfig --list.
    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    runlevel_object and the optional state element specifies the data to
    check.
    """

    class Meta:
        name = "runlevel_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SccsState:
    """
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to an SCCS file.
    :ivar filename: This is the name of a SCCS file.
    :ivar module_name:
    :ivar module_type:
    :ivar release:
    :ivar level:
    :ivar branch:
    :ivar sequence:
    :ivar what_string:
    """

    class Meta:
        name = "sccs_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    module_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    module_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    branch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    what_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SccsTest:
    class Meta:
        name = "sccs_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ShadowObject:
    """The shadow_object element is used by a shadow test to define the shadow file
    to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A shdow object consists of a single user entity
    that identifies the username associted with the shadow file.
    """

    class Meta:
        name = "shadow_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    username: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class ShadowTest:
    """The shadow test is used to check information from the /etc/shadow file for a
    specific user.

    This file contains a user's password, but also their password aging
    and lockout information. It extends the standard TestType as defined
    in the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references an shadow_object and the optional state element specifies
    the information to check.
    """

    class Meta:
        name = "shadow_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SymlinkObject:
    """The symlink_object element is used by a symlink_test to define the object to
    be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A symlink_object consists of a filepath entity
    that contains the path to a symbolic link file.  The resulting item
    identifies the canonical path of the link target (followed to its
    final destination, if there are intermediate links), an error if the
    link target does not exist or is a circular link (e.g., a link to
    itself).  If the file located at filepath is not a symlink, or if
    there is no file located at the filepath, then any resulting item
    would itself have a status of does not exist.

    :ivar set:
    :ivar filepath: Specifies the filepath for the symbolic link.
    :ivar filter:
    """

    class Meta:
        name = "symlink_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class SymlinkState:
    """
    The symlink_state element defines a value used to evaluate the result of a
    specific symlink_object item.

    :ivar filepath: Specifies the filepath used to create the object.
    :ivar canonical_path: Specifies the canonical path for the target of
        a symbolic link file specified by the filepath.
    """

    class Meta:
        name = "symlink_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    canonical_path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SymlinkTest:
    """
    The symlink_test is used to obtain canonical path information for symbolic
    links.
    """

    class Meta:
        name = "symlink_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SysctlObject:
    """The sysctl_object is used by a sysctl_test to define which kernel parameters
    on the local system should be collected.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar name: The name element specifies the name(s) of the kernel
        parameter(s) that should be collected from the local system.
    :ivar filter:
    """

    class Meta:
        name = "sysctl_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class SysctlState:
    """
    The sysctl_state contains two entities that are used to check the kernel
    parameter name and value(s).

    :ivar name: The name element contains a string that represents the
        name of a kernel parameter that was collected from the local
        system.
    :ivar value: The value element contains a string that represents the
        value(s) associated with the specified kernel parameter.
    """

    class Meta:
        name = "sysctl_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SysctlTest:
    """The sysctl_test is used to check the values associated with the kernel
    parameters that are used by the local system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a sysctl_object
    and the optional state element references a sysctl_state that
    specifies the information to check.
    """

    class Meta:
        name = "sysctl_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UnameObject:
    """The uname_object element is used by an uname test to define those objects to
    evaluated based on a specified state.

    There is actually only one object relating to uname and this is the
    system as a whole. Therefore, there are no child entities defined.
    Any OVAL Test written to check uname will reference the same
    uname_object which is basically an empty object element.
    """

    class Meta:
        name = "uname_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class UnameState:
    """The uname_state element defines the information about the hardware the
    machine is running one.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar machine_class: This entity specifies a machine hardware name.
        This corresponds to the command uname -m.
    :ivar node_name: This entity specifies a host name. This corresponds
        to the command uname -n.
    :ivar os_name: This entity specifies an operating system name. This
        corresponds to the command uname -s.
    :ivar os_release: This entity specifies a build version. This
        corresponds to the command uname -r.
    :ivar os_version: This entity specifies an operating system version.
        This corresponds to the command uname -v.
    :ivar processor_type: This entity specifies a processor type. This
        corresponds to the command uname -p.
    """

    class Meta:
        name = "uname_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    machine_class: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    node_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    os_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    os_release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    os_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    processor_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UnameTest:
    """The uname test reveals information about the hardware the machine is running
    on.

    This information is the parsed equivalent of uname -a. For example:
    "Linux quark 2.6.5-7.108-default #1 Wed Aug 25 13:34:40 UTC 2004
    i686 i686 i386 GNU/Linux" or "Darwin TestHost 7.7.0 Darwin Kernel
    Version 7.7.0: Sun Nov 7 16:06:51 PST 2004;
    root:xnu/xnu-517.9.5.obj~1/RELEASE_PPC Power Macintosh powerpc". It
    extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a uname_object
    and the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "uname_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class XinetdObject:
    """The xinetd_object element is used by an xinetd test to define the specific
    protocol-service to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An xinetd object consists of a protocol entity
    and a service_name entity that identifies the specific service to be
    tested.

    :ivar set:
    :ivar protocol: The protocol entity specifies the protocol that is
        used by the service.  The list of valid protocols can be found
        in /etc/protocols.
    :ivar service_name: The service_name entity specifies the name of
        the service.
    :ivar filter:
    """

    class Meta:
        name = "xinetd_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class XinetdTest:
    """The xinetd test is used to check information associated with different
    Internet services.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an inetd_object
    and the optional state element specifies the information to check.
    """

    class Meta:
        name = "xinetd_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileBehaviors:
    """The FileBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of the file_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file.

    :ivar max_depth: 'max_depth' defines the maximum depth of recursion
        to perform when a recurse_direction is specified. A value of '0'
        is equivalent to no recursion, '1' means to step only one
        directory level up/down, and so on. The default value is '-1'
        meaning no limitation. For a 'max_depth' of -1 or any value of 1
        or more the starting directory must be considered in the
        recursive search. Note that the default recurse_direction
        behavior is 'none' so even though max_depth specifies no
        limitation by default, the recurse_direction behavior turns
        recursion off. Note that this behavior only applies with the
        equality operation on the path entity.
    :ivar recurse: 'recurse' defines how to recurse into the path
        entity, in other words what to follow during recursion. Options
        include symlinks, directories, or both. Note that a max-depth
        other than 0 has to be specified for recursion to take place and
        for this attribute to mean anything. Note that this behavior
        only applies with the equality operation on the path entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction
        to recurse, either 'up' to parent directories, or 'down' into
        child directories. The default value is 'none' for no recursion.
        Note that this behavior only applies with the equality operation
        on the path entity.
    :ivar recurse_file_system: 'recurse_file_system' defines the file
        system limitation of any searching and applies to all operations
        as specified on the path or filepath entity. The value of
        'local' limits the search scope to local file systems (as
        opposed to file systems mounted from an external system). The
        value of 'defined' keeps any recursion within the file system
        that the file_object (path+filename or filepath) has specified.
        For example, if the path specified was "/", you would search
        only the filesystem mounted there, not other filesystems mounted
        to descendant paths. The value of 'defined' only applies when an
        equality operation is used for searching because the path or
        filepath entity must explicitly define a file system. The
        default value is 'all' meaning to search all available file
        systems for data collection. Note that in most cases it is
        recommended that the value of 'local' be used to ensure that
        file system searching is limited to only the local file systems.
        Searching 'all' file systems may have performance implications.
    """

    max_depth: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1,
            "fraction_digits": 0,
        },
    )
    recurse: FileBehaviorsRecurse = field(
        default=FileBehaviorsRecurse.SYMLINKS_AND_DIRECTORIES,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: FileBehaviorsRecurseDirection = field(
        default=FileBehaviorsRecurseDirection.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_file_system: FileBehaviorsRecurseFileSystem = field(
        default=FileBehaviorsRecurseFileSystem.ALL,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GconfState:
    """The gconf_state element defines the different information that can be used
    to evaluate the specified GConf preference key.

    This includes the preference key, source, type, whether it's
    writable, the user who last modified it, the time it was last
    modified, whether it's the default value, as well as the preference
    key's value. Please refer to the individual elements in the schema
    for more details about what each represents.

    :ivar key: The preference key to check.
    :ivar source: The source used to look up the preference key.
    :ivar type_value: The type of the preference key.
    :ivar is_writable: Is the preference key writable? If true, the
        preference key is writable. If false, the preference key is not
        writable.
    :ivar mod_user: The user who last modified the preference key.
    :ivar mod_time: The time the preference key was last modified in
        seconds since the Unix epoch. The Unix epoch is the time
        00:00:00 UTC on January 1, 1970.
    :ivar is_default: Is the preference key value the default value. If
        true, the preference key value is the default value. If false,
        the preference key value is not the default value.
    :ivar value: The value of the preference key.
    """

    class Meta:
        name = "gconf_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateGconfTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    is_writable: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mod_user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mod_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    is_default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InetdState:
    """The inetd_state element defines the different information associated with a
    specific Internet service.

    Please refer to the individual elements in the schema for more
    details about what each represents.

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
        name = "inetd_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server_program: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server_arguments: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    endpoint_type: Optional[EntityStateEndpointType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_as_user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wait_status: Optional[EntityStateWaitStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InterfaceState:
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

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateInterfaceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    hardware_addr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    inet_addr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    broadcast_addr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    netmask: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Process58State:
    """The process58_state element defines the different metadata associated with a
    UNIX process.

    This includes the command line, pid, ppid, priority, and user id.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar command_line: This is the string used to start the process.
        This includes any parameters that are part of the command line.
    :ivar exec_time: This is the cumulative CPU time, formatted in
        [DD-]HH:MM:SS where DD is the number of days when execution time
        is 24 hours or more.
    :ivar pid: This is the process ID of the process.
    :ivar ppid: This is the process ID of the process's parent process.
    :ivar priority: This is the scheduling priority with which the
        process runs. This can be adjusted with the nice command or
        nice() system call.
    :ivar ruid: This is the real user id which represents the user who
        has created the process.
    :ivar scheduling_class: A platform specific characteristic
        maintained by the scheduler: RT (real-time), TS (timeshare), FF
        (fifo), SYS (system), etc.
    :ivar start_time: This is the time of day the process started
        formatted in HH:MM:SS if the same day the process started or
        formatted as MMM_DD (Ex.: Feb_5) if process started the previous
        day or further in the past.
    :ivar tty: This is the TTY on which the process was started, if
        applicable.
    :ivar user_id: This is the effective user id which represents the
        actual privileges of the process.
    :ivar exec_shield: A boolean that when true would indicates that
        ExecShield is enabled for the process.
    :ivar loginuid: The loginuid shows which account a user gained
        access to the system with. The /proc/XXXX/loginuid shows this
        value.
    :ivar posix_capability: An effective capability associated with the
        process. See linux/include/linux/capability.h for more
        information.
    :ivar selinux_domain_label: An selinux domain label associated with
        the process.
    :ivar session_id: The session ID of the process.
    """

    class Meta:
        name = "process58_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    command_line: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ppid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ruid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    scheduling_class: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_shield: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loginuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    posix_capability: Optional[EntityStateCapabilityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    selinux_domain_label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    session_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RoutingtableState:
    """The routingtable_state element defines the different information that can be
    used to check an entry found in a system's primary routing table.

    This includes the destination IP address, gateway, netmask, flags,
    and the name of the interface associated with it. Please refer to
    the individual elements in the schema for more details about what
    each represents.

    :ivar destination: The destination IP address prefix of the routing
        table entry. This is the destination IP address and
        netmask/prefix-length expressed using CIDR notation.
    :ivar gateway: The gateway of the specified routing table entry.
    :ivar flags: The flags associated with the specified routing table
        entry.
    :ivar interface_name: The name of the interface associated with the
        routing table entry.
    """

    class Meta:
        name = "routingtable_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    destination: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gateway: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flags: Optional[EntityStateRoutingTableFlagsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ShadowState:
    """The shadows_state element defines the different information associated with
    the system shadow file.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar username: This is the name of the user being checked.
    :ivar password: This is the encrypted version of the user's
        password.
    :ivar chg_lst: This is the date of the last password change in days
        since 1/1/1970.
    :ivar chg_allow: This specifies how often in days a user may change
        their password. It can also be thought of as the minimum age of
        a password.
    :ivar chg_req: This describes how long a user can keep a password
        before the system forces her to change it.
    :ivar exp_warn: This describes how long before password expiration
        the system begins warning the user. The system will warn the
        user at each login.
    :ivar exp_inact: The exp_inact entity describes how many days of
        account inactivity the system will wait after a password expires
        before locking the account. Unix systems are generally
        configured to only allow a given password to last for a fixed
        period of time. When this time, the chg_req parameter, is near
        running out, the system begins warning the user at each login.
        How soon before the expiration the user receives these warnings
        is specified in exp_warn. The only hiccup in this design is that
        a user may not login in time to ever receive a warning before
        account expiration. The exp_inact parameter gives the sysadmin
        flexibility so that a user who reaches the end of their
        expiration time gains exp_inact more days to login and change
        their password manually.
    :ivar exp_date: This specifies when will the account's password
        expire, in days since 1/1/1970.
    :ivar flag: This is a reserved field that the shadow file may use in
        the future.
    :ivar encrypt_method: The encrypt_method entity describes method
        that is used for hashing passwords.
    """

    class Meta:
        name = "shadow_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    username: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chg_lst: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chg_allow: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chg_req: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exp_warn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exp_inact: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exp_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    encrypt_method: Optional[EntityStateEncryptMethodType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class XinetdState:
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

    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flags: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    no_access: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    only_from: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    port: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server_arguments: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    socket_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateXinetdTypeStatusType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wait: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    disabled: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileObject:
    """The file_object element is used by a file test to define the specific
    file(s) to be evaluated.

    The file_object will collect all UNIX file types (directory, regular
    file, character device, block device, fifo, symbolic link, and
    socket). Each object extends the standard ObjectType as defined in
    the oval-definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A file object defines the path and filename of
    the file(s). In addition, a number of behaviors may be provided that
    help guide the collection of objects. Please refer to the
    FileBehaviors complex type for more information about specific
    behaviors. The set of files to be evaluated may be identified with
    either a complete filepath or a path and filename. Only one of these
    options may be selected. It is important to note that the
    'max_depth' and 'recurse_direction' attributes of the 'behaviors'
    element do not apply to the 'filepath' element, only to the 'path'
    and 'filename' elements.  This is because the 'filepath' element
    represents an absolute path to a particular file and it is not
    possible to recurse over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        evaluate. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level directory object (not
        all the files in the directory).  In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar filter:
    """

    class Meta:
        name = "file_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class FileextendedattributeObject:
    """The fileextendedattribute_object element is used by a file extended
    attribute test to define the specific file(s) and attribute(s) to be evaluated.

    The fileextendedattribute_object will collect all UNIX file types
    (directory, regular file, character device, block device, fifo,
    symbolic link, and socket). Each object extends the standard
    ObjectType as defined in the oval-definitions-schema and one should
    refer to the ObjectType description for more information. The common
    set element allows complex objects to be created using filters and
    set logic. Again, please refer to the description of the set element
    in the oval-definitions-schema. A file extended attribute object
    defines the path, filename and attribute name. In addition, a number
    of behaviors may be provided that help guide the collection of
    objects. Please refer to the FileExtendedAttributeBehaviors complex
    type for more information about specific behaviors. The set of files
    to be evaluated may be identified with either a complete filepath or
    a path and filename. Only one of these options may be selected. It
    is important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        evaluate. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level directory object (not
        all the files in the directory).  In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes associated with a directory. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every file under a given path.
    :ivar attribute_name: The attribute_name element specifies the name
        of an extended attribute to evaluate.
    :ivar filter:
    """

    class Meta:
        name = "fileextendedattribute_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class SccsObject:
    """The set of files to be evaluated may be identified with either a complete
    filepath or a path and filename.

    Only one of these options may be selected. It is important to note
    that the 'max_depth' and 'recurse_direction' attributes of the
    'behaviors' element do not apply to the 'filepath' element, only to
    the 'path' and 'filename' elements.  This is because the 'filepath'
    element represents an absolute path to a particular file and it is
    not possible to recurse over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to an SCCS file.
    :ivar filename: The name of an SCCS file.
    :ivar filter:
    """

    class Meta:
        name = "sccs_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
