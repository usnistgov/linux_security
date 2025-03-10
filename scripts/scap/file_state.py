from dataclasses import dataclass, field
from typing import Optional

from scap.a_time_datatype_1 import ATimeDatatype1
from scap.c_time_datatype_1 import CTimeDatatype1
from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_bool_type import EntityStateBoolType
from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.group_id_datatype_1 import GroupIdDatatype1
from scap.m_time_datatype_1 import MTimeDatatype1
from scap.state_type import StateType
from scap.user_id_datatype_1 import UserIdDatatype1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class FileState(StateType):
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

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    group_id: Optional["FileState.GroupId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional["FileState.UserId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    a_time: Optional["FileState.ATime"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    c_time: Optional["FileState.CTime"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    m_time: Optional["FileState.MTime"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    size: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    suid: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sgid: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sticky: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uread: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uwrite: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uexec: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gread: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gwrite: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gexec: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    oread: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    owrite: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    oexec: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    has_extended_acl: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class GroupId(EntityStateAnySimpleType):
        datatype: GroupIdDatatype1 = field(
            default=GroupIdDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class UserId(EntityStateAnySimpleType):
        datatype: UserIdDatatype1 = field(
            default=UserIdDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ATime(EntityStateAnySimpleType):
        datatype: ATimeDatatype1 = field(
            default=ATimeDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class CTime(EntityStateAnySimpleType):
        datatype: CTimeDatatype1 = field(
            default=CTimeDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class MTime(EntityStateAnySimpleType):
        datatype: MTimeDatatype1 = field(
            default=MTimeDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )
