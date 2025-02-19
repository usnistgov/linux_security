from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemCapabilityType(Enum):
    """The EntityItemCapabilityType complex type restricts a string value to a
    specific set of values that describe POSIX capability types associated with a
    process service.

    This list is based off the values defined in
    linux/include/linux/capability.h. Documentation on each allowed
    value can be found in capability.h.  The empty string is also
    allowed to support empty elements associated with error conditions.

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
    VALUE = ""


class EntityItemEncryptMethodType(Enum):
    """The EntityItemEncryptMethodType complex type restricts a string value to a
    set that corresponds to the allowed encrypt methods used for protected
    passwords in a shadow file.

    The empty string is also allowed to support empty elements
    associated with error conditions.

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


class EntityItemEndpointType(Enum):
    """The EntityItemEndpointType complex type restricts a string value to a
    specific set of values that describe endpoint types associated with an Internet
    service.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar STREAM: The stream value is used to describe a stream socket.
    :cvar DGRAM: The dgram value is used to describe a datagram socket.
    :cvar RAW: The raw value is used to describe a raw socket.
    :cvar SEQPACKET: The seqpacket value is used to describe a sequenced
        packet socket.
    :cvar TLI: The tli value is used to describe all TLI endpoints.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    STREAM = "stream"
    DGRAM = "dgram"
    RAW = "raw"
    SEQPACKET = "seqpacket"
    TLI = "tli"
    VALUE = ""


class EntityItemGconfTypeType(Enum):
    """The EntityItemGconfTypeType complex type restricts a string value to the
    seven values GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
    GCONF_VALUE_BOOL, GCONF_VALUE_SCHEMA, GCONF_VALUE_LIST, and GCONF_VALUE_PAIR
    that specify the type of the value associated with a GConf preference key.

    The empty string is also allowed to support empty elements
    associated with error conditions.

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
        detailed error reporting.
    """

    GCONF_VALUE_STRING = "GCONF_VALUE_STRING"
    GCONF_VALUE_INT = "GCONF_VALUE_INT"
    GCONF_VALUE_FLOAT = "GCONF_VALUE_FLOAT"
    GCONF_VALUE_BOOL = "GCONF_VALUE_BOOL"
    GCONF_VALUE_SCHEMA = "GCONF_VALUE_SCHEMA"
    GCONF_VALUE_LIST = "GCONF_VALUE_LIST"
    GCONF_VALUE_PAIR = "GCONF_VALUE_PAIR"
    VALUE = ""


class EntityItemInterfaceType(Enum):
    """The EntityItemInterfaceType complex type restricts a string value to a
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
        detailed error reporting.
    """

    ARPHRD_ETHER = "ARPHRD_ETHER"
    ARPHRD_FDDI = "ARPHRD_FDDI"
    ARPHRD_LOOPBACK = "ARPHRD_LOOPBACK"
    ARPHRD_VOID = "ARPHRD_VOID"
    ARPHRD_PPP = "ARPHRD_PPP"
    ARPHRD_SLIP = "ARPHRD_SLIP"
    ARPHRD_PRONET = "ARPHRD_PRONET"
    VALUE = ""


class EntityItemRoutingTableFlagsType(Enum):
    """The EntityItemRoutingTableFlagsType complex type restricts a string value to
    a specific set of values that describe the flags associated with a routing
    table entry.

    This list is based off the values defined in the man pages of
    various platforms. For Linux, please see route(8). For Solaris,
    please see netstat(1M). For HP-UX, please see netstat(1). For Mac
    OS, please see netstat(1). For FreeBSD, please see netstat(1).
    Documentation on each allowed value can be found in the previously
    listed man pages. The empty string is also allowed to support empty
    elements associated with error conditions.

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
        detailed error reporting.
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


class EntityItemWaitStatusType(Enum):
    """The EntityItemWaitStatusType complex type restricts a string value to two
    values, either wait or nowait, that specify whether the server that is invoked
    by inetd will take over the listening socket associated with the service, and
    whether once launched, inetd will wait for that server to exit, if ever, before
    it resumes listening for new service requests.

    The empty string is also allowed to support empty elements
    associated with error conditions.

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
        detailed error reporting.
    """

    WAIT = "wait"
    NOWAIT = "nowait"
    VALUE = ""


class EntityItemXinetdTypeStatusType(Enum):
    """The EntityItemXinetdTypeStatusType complex type restricts a string value to
    five values, either RPC, INTERNAL, UNLISTED, TCPMUX, or TCPMUXPLUS that specify
    the type of service registered in xinetd.

    The empty string is also allowed to support empty elements
    associated with error conditions.

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
        detailed error reporting.
    """

    INTERNAL = "INTERNAL"
    RPC = "RPC"
    UNLISTED = "UNLISTED"
    TCPMUX = "TCPMUX"
    TCPMUXPLUS = "TCPMUXPLUS"
    VALUE = ""


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
    ip_address: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileItem:
    """The file item holds information about the individual files found on a
    system.

    Each file item contains path and filename information as well as its
    type, associated user and group ids, relevant dates, and the
    privialeges granted. It extends the standard ItemType as defined in
    the oval-system-characteristics schema and one should refer to the
    ItemType description for more information.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file. If the xsi:nil attribute is
        set to true, then the item being represented is the higher
        directory represented by the path entity.
    :ivar type_value: This is the file's type: regular file (regular),
        directory, named pipe (fifo), symbolic link, socket or block
        special.
    :ivar group_id: This is the group owner of the file, by group
        number.
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
    :ivar gwrite: Can the group owner of the file write to this file, or
        if a directory, write to the directory?
    :ivar gexec: Can the group owner of the file execute it or, if a
        directory, change into the directory?
    :ivar oread: Can all other users read this file or, if a directory,
        read the directory contents?
    :ivar owrite: Can the other users write to this file, or if a
        directory, write to the directory?
    :ivar oexec: Can the other users execute this file or, if a
        directory, change into the directory?
    :ivar has_extended_acl: Does the file or directory have ACL
        permissions applied to it? If the file or directory doesn't have
        an ACL, or it matches the standard UNIX permissions, the value
        will be 'false'. Otherwise, if a file or directory has an ACL,
        the value will be 'true'. If the system does not support ACLs,
        the status will be 'does not exist' and if the system supports
        ACLs, the status will be 'exists'.
    """

    class Meta:
        name = "file_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
class FileextendedattributeItem:
    """The file extended attribute item holds information about the individual file
    extended attributes found on a system.

    Each file extended attribute item contains path, filename, and
    attribute name information as well as the attribute's value. It
    extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file. If the xsi:nil attribute is
        set to true, then the item being represented is the higher
        directory represented by the path entity.
    :ivar attribute_name: This is the extended attribute's name,
        identifier or key.
    :ivar value: This is the extended attribute's value or contents.
    """

    class Meta:
        name = "fileextendedattribute_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PasswordItem:
    """/etc/passwd.

    See passwd(4).

    :ivar username: This is the name of the user for which data was
        gathered.
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
        name = "password_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
class ProcessItem:
    """Output of /usr/bin/ps.

    See ps(1).

    :ivar command: This specifies the command/program name about which
        data has has been collected.
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
        name = "process_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
class RunlevelItem:
    """The runlevel item holds information about the start or kill state of a
    specified service at a given runlevel.

    Each runlevel item contains service name and runlevel information as
    well as start and kill information. It extends the standard ItemType
    as defined in the oval-system-characteristics schema and one should
    refer to the ItemType description for more information.

    :ivar service_name: The service_name entity is the actual name of
        the specific service.
    :ivar runlevel: The runlevel entity specifies the system runlevel
        associated with a service.
    :ivar start: The start entity specifies whether the service is
        scheduled to start at the runlevel.
    :ivar kill: The kill entity specifies whether the service is
        scheduled to be killed at the runlevel.
    """

    class Meta:
        name = "runlevel_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
class SccsItem:
    """
    :ivar filepath: Specifies the absolute path to an SCCS file. A
        directory cannot be specified as a filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to an SCCS file.
    :ivar filename: The name of an SCCS file.
    :ivar module_name:
    :ivar module_type:
    :ivar release:
    :ivar level:
    :ivar branch:
    :ivar sequence:
    :ivar what_string:
    """

    class Meta:
        name = "sccs_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
class SysctlItem:
    """
    The sysctl_item stores information retrieved from the local system about a
    kernel parameter and its respective value(s).

    :ivar name: The name element contains a string that represents the
        name of a kernel parameter that was collected from the local
        system.
    :ivar value: The value element contains a string that represents the
        current value(s) for the specified kernel parameter on the local
        system.
    """

    class Meta:
        name = "sysctl_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UnameItem:
    """Information about the hardware the machine is running on.

    This information is the parsed equivalent of uname -a.

    :ivar machine_class: This entity specifies the machine hardware
        name.  This corresponds to the command uname -m.
    :ivar node_name: This entity specifies the host name.  This
        corresponds to the command uname -n.
    :ivar os_name: This entity specifies the operating system name.
        This corresponds to the command uname -s.
    :ivar os_release: This entity specifies the build version.  This
        corresponds to the command uname -r.
    :ivar os_version: This entity specifies the operating system
        version.  This corresponds to the command uname -v.
    :ivar processor_type: This entity specifies the processor type.
        This corresponds to the command uname -p.
    """

    class Meta:
        name = "uname_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
class GconfItem:
    """The gconf_item holds information about an individual GConf preference key
    found on a system.

    Each gconf_item contains a preference key, source, type, whether
    it's writable, the user who last modified it, the time it was last
    modified, whether it's the default value, as well as the preference
    key's value. It extends the standard ItemType as defined in the
    oval-system-characteristics schema and one should refer to the
    ItemType description for more information.

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
        name = "gconf_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
    type_value: Optional[EntityItemGconfTypeType] = field(
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
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
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
    :ivar server_arguments:
    :ivar endpoint_type:
    :ivar exec_as_user:
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
    endpoint_type: Optional[EntityItemEndpointType] = field(
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
    wait_status: Optional[EntityItemWaitStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
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
            "namespace": "",
        },
    )
    type_value: Optional[EntityItemInterfaceType] = field(
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
    flag: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Process58Item:
    """Output of /usr/bin/ps.

    See ps(1).

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
        name = "process58_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
    posix_capability: list[EntityItemCapabilityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    selinux_domain_label: list[str] = field(
        default_factory=list,
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
class RoutingtableItem:
    """The routingtable_item holds information about an individual routing table
    entry found in a system's primary routing table.

    Each routingtable_item contains a destination IP address, gateway,
    netmask, flags, and the name of the interface associated with it. It
    is important to note that only numerical addresses will be collected
    and that their symbolic representations will not be resolved. This
    equivalent to using the '-n' option with route(8) or netstat(8). It
    extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

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
        name = "routingtable_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
    flags: list[EntityItemRoutingTableFlagsType] = field(
        default_factory=list,
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
class ShadowItem:
    """/etc/shadow.

    See shadow(4).

    :ivar username: This is the name of the user for which data was
        gathered.
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
    :ivar exp_inact: This describes how many days of account inactivity
        the system will wait after a password expires before locking the
        account? This window, usually only set to a few days, gives
        users who are logging in very seldomly a bit of extra time to
        receive the password expiration warning and change their
        password.
    :ivar exp_date: This specifies when will the account's password
        expire, in days since 1/1/1970.
    :ivar flag: This is a reserved field that the shadow file may use in
        the future.
    :ivar encrypt_method: The encrypt_method entity describes method
        that is used for hashing passwords.
    """

    class Meta:
        name = "shadow_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

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
    encrypt_method: Optional[EntityItemEncryptMethodType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
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
    flags: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    no_access: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    only_from: list[str] = field(
        default_factory=list,
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
    type_value: Optional[EntityItemXinetdTypeStatusType] = field(
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
