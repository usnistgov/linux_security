from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.oval_system_characteristics_schema import (
    EntityItemAnySimpleType,
    EntityItemBoolType,
    EntityItemIntType,
    EntityItemIpaddressStringType,
    EntityItemIpaddressType,
    EntityItemStringType,
    ItemType,
)

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class ATimeDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class CTimeDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class ChgAllowDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class ChgLstDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class ChgReqDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class ExpDateDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class ExpInactDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class ExpWarnDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class FlagDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class GroupIdDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class MTimeDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class UserIdDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


@dataclass
class EntityItemCapabilityType(EntityItemStringType):
    """The EntityItemCapabilityType complex type restricts a string value to a
    specific set of values that describe POSIX capability types associated with a
    process service.

    This list is based off the values defined in
    linux/include/linux/capability.h. Documentation on each allowed
    value can be found in capability.h.  The empty string is also
    allowed to support empty elements associated with error conditions.
    """


@dataclass
class EntityItemEncryptMethodType(EntityItemStringType):
    """The EntityItemEncryptMethodType complex type restricts a string value to a
    set that corresponds to the allowed encrypt methods used for protected
    passwords in a shadow file.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class EntityItemEndpointType(EntityItemStringType):
    """The EntityItemEndpointType complex type restricts a string value to a
    specific set of values that describe endpoint types associated with an Internet
    service.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class EntityItemGconfTypeType(EntityItemStringType):
    """The EntityItemGconfTypeType complex type restricts a string value to the
    seven values GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
    GCONF_VALUE_BOOL, GCONF_VALUE_SCHEMA, GCONF_VALUE_LIST, and GCONF_VALUE_PAIR
    that specify the type of the value associated with a GConf preference key.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class EntityItemInterfaceType(EntityItemStringType):
    """The EntityItemInterfaceType complex type restricts a string value to a
    specific set of values.

    These values describe the different interface types which are
    defined in 'if_arp.h'. The empty string is also allowed to support
    empty element associated with variable references. Note that when
    using pattern matches and variables care must be taken to ensure
    that the regular expression and variable values align with the
    enumerated values.
    """


@dataclass
class EntityItemRoutingTableFlagsType(EntityItemStringType):
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
    """


@dataclass
class EntityItemWaitStatusType(EntityItemStringType):
    """The EntityItemWaitStatusType complex type restricts a string value to two
    values, either wait or nowait, that specify whether the server that is invoked
    by inetd will take over the listening socket associated with the service, and
    whether once launched, inetd will wait for that server to exit, if ever, before
    it resumes listening for new service requests.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class EntityItemXinetdTypeStatusType(EntityItemStringType):
    """The EntityItemXinetdTypeStatusType complex type restricts a string value to
    five values, either RPC, INTERNAL, UNLISTED, TCPMUX, or TCPMUXPLUS that specify
    the type of service registered in xinetd.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class DnscacheItem(ItemType):
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

    domain_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ttl: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ip_address: list[EntityItemIpaddressStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileItem(ItemType):
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
        permissions applied to it? If a system supports ACLs and the
        file or directory doesn't have an ACL, or it matches the
        standard UNIX permissions, the entity will have a status of
        'exists' and a value of 'false'. If the system supports ACLs and
        the file or directory has an ACL, the entity will have a status
        of 'exists' and a value of 'true'. Lastly, if a system doesn't
        support ACLs, the entity will have a status of 'does not exist'.
    """

    class Meta:
        name = "file_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    type_value: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    group_id: Optional["FileItem.GroupId"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional["FileItem.UserId"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a_time: Optional["FileItem.ATime"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c_time: Optional["FileItem.CTime"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    m_time: Optional["FileItem.MTime"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    suid: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sgid: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sticky: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uread: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uwrite: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uexec: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gread: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gwrite: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gexec: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    oread: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    owrite: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    oexec: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    has_extended_acl: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class GroupId(EntityItemAnySimpleType):
        datatype: GroupIdDatatype = field(
            default=GroupIdDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class UserId(EntityItemAnySimpleType):
        datatype: UserIdDatatype = field(
            default=UserIdDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ATime(EntityItemAnySimpleType):
        datatype: ATimeDatatype = field(
            default=ATimeDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class CTime(EntityItemAnySimpleType):
        datatype: CTimeDatatype = field(
            default=CTimeDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class MTime(EntityItemAnySimpleType):
        datatype: MTimeDatatype = field(
            default=MTimeDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class FileextendedattributeItem(ItemType):
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

    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityItemAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PasswordItem(ItemType):
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

    username: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    password: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional["PasswordItem.UserId"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group_id: Optional["PasswordItem.GroupId"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gcos: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    home_dir: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    login_shell: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    last_login: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class UserId(EntityItemAnySimpleType):
        datatype: UserIdDatatype = field(
            default=UserIdDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class GroupId(EntityItemAnySimpleType):
        datatype: GroupIdDatatype = field(
            default=GroupIdDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class ProcessItem(ItemType):
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

    command: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_time: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ppid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ruid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    scheduling_class: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start_time: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tty: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RunlevelItem(ItemType):
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

    service_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    runlevel: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    kill: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SccsItem(ItemType):
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

    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    module_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    module_type: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    level: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    branch: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sequence: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    what_string: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SshdItem(ItemType):
    """The sshd_item stores information retrieved from the local system about sshd
    parameters and their respective value(s).

    Information is collected from the target endpoint using the "sshd -f
    [FILEPATH] -T [NAME]" command and output values are parsed. Each
    output line begins with the name of the SSHD parameter, followed by
    a space, and potentially a tokenized list of values. It has been
    found that some parameter values are comma-delimited while some are
    space-delimited.  Implementers of this collection should account for
    both delimiters in SSHD parameter values.

    :ivar filepath: The filepath element specifies the absolute path to
        the sshd configuration file on the machine. A directory cannot
        be specified as a filepath. If the collecting object's filepath
        was specified as xsi:nil="true", then the value of this system
        characteristics element should be set to the default filepath,
        /etc/ssh/sshd_config.
    :ivar name: The name element contains a string that represents the
        name of a sshd parameter that was collected from the local
        system.
    :ivar value: The value element contains a string that represents the
        current value(s) for the specified sshd parameter on the local
        system.
    """

    class Meta:
        name = "sshd_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SymlinkItem(ItemType):
    """
    The symlink_item element identifies the result generated for a symlink_object.

    :ivar filepath: Specifies the filepath to the subject symbolic link
        file, specified by the symlink_object.
    :ivar canonical_path: Specifies the canonical path for the target of
        the symbolic link file specified by the filepath.
    """

    class Meta:
        name = "symlink_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    canonical_path: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class SysctlItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UnameItem(ItemType):
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

    machine_class: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    node_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    os_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    os_release: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    os_version: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    processor_type: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GconfItem(ItemType):
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

    key: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    source: Optional[EntityItemStringType] = field(
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
    is_writable: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mod_user: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mod_time: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    is_default: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InetdItem(ItemType):
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

    protocol: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server_program: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server_arguments: Optional[EntityItemStringType] = field(
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
    exec_as_user: Optional[EntityItemStringType] = field(
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
class InterfaceItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
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
    hardware_addr: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    inet_addr: Optional[EntityItemIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    broadcast_addr: Optional[EntityItemIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    netmask: Optional[EntityItemIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flag: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Process58Item(ItemType):
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

    command_line: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_time: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ppid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ruid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    scheduling_class: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start_time: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tty: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exec_shield: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loginuid: Optional[EntityItemIntType] = field(
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
    selinux_domain_label: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    session_id: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RoutingtableItem(ItemType):
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

    destination: Optional[EntityItemIpaddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gateway: Optional[EntityItemIpaddressType] = field(
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
    interface_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ShadowItem(ItemType):
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
    :ivar chg_req: This describes how long the user can keep a password
        before the system forces them to change it.
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
    :ivar flag: This is a numeric reserved field that the shadow file
        may use in the future.
    :ivar encrypt_method: The encrypt_method entity describes method
        that is used for hashing passwords.
    """

    class Meta:
        name = "shadow_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    username: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    password: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chg_lst: Optional["ShadowItem.ChgLst"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chg_allow: Optional["ShadowItem.ChgAllow"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chg_req: Optional["ShadowItem.ChgReq"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exp_warn: Optional["ShadowItem.ExpWarn"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exp_inact: Optional["ShadowItem.ExpInact"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exp_date: Optional["ShadowItem.ExpDate"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flag: Optional["ShadowItem.Flag"] = field(
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
    class ChgLst(EntityItemAnySimpleType):
        datatype: ChgLstDatatype = field(
            default=ChgLstDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ChgAllow(EntityItemAnySimpleType):
        datatype: ChgAllowDatatype = field(
            default=ChgAllowDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ChgReq(EntityItemAnySimpleType):
        datatype: ChgReqDatatype = field(
            default=ChgReqDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpWarn(EntityItemAnySimpleType):
        datatype: ExpWarnDatatype = field(
            default=ExpWarnDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpInact(EntityItemAnySimpleType):
        datatype: ExpInactDatatype = field(
            default=ExpInactDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpDate(EntityItemAnySimpleType):
        datatype: ExpDateDatatype = field(
            default=ExpDateDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Flag(EntityItemAnySimpleType):
        datatype: FlagDatatype = field(
            default=FlagDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class XinetdItem(ItemType):
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

    protocol: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    flags: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    no_access: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    only_from: list[EntityItemIpaddressStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    port: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    server_arguments: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    socket_type: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: list[EntityItemXinetdTypeStatusType] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    user: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wait: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    disabled: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
