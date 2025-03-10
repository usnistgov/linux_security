from dataclasses import dataclass, field
from typing import Optional

from scap.a_time_datatype_2 import ATimeDatatype2
from scap.c_time_datatype_2 import CTimeDatatype2
from scap.group_id_datatype_2 import GroupIdDatatype2
from scap.m_time_datatype_2 import MTimeDatatype2
from scap.user_id_datatype_2 import UserIdDatatype2

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
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

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    group_id: Optional["FileItem.GroupId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional["FileItem.UserId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    a_time: Optional["FileItem.ATime"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    c_time: Optional["FileItem.CTime"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    m_time: Optional["FileItem.MTime"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    suid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sgid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sticky: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uread: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uwrite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uexec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gread: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gwrite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gexec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    oread: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    owrite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    oexec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    has_extended_acl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class GroupId:
        datatype: GroupIdDatatype2 = field(
            default=GroupIdDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class UserId:
        datatype: UserIdDatatype2 = field(
            default=UserIdDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ATime:
        datatype: ATimeDatatype2 = field(
            default=ATimeDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class CTime:
        datatype: CTimeDatatype2 = field(
            default=CTimeDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class MTime:
        datatype: MTimeDatatype2 = field(
            default=MTimeDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )
