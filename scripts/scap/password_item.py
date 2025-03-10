from dataclasses import dataclass, field
from typing import Optional

from scap.group_id_datatype_2 import GroupIdDatatype2
from scap.user_id_datatype_2 import UserIdDatatype2

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
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
            
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional["PasswordItem.UserId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    group_id: Optional["PasswordItem.GroupId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gcos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    home_dir: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    login_shell: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    last_login: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
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
    class GroupId:
        datatype: GroupIdDatatype2 = field(
            default=GroupIdDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )
