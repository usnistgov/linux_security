from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.group_id_datatype_1 import GroupIdDatatype1
from scap.state_type import StateType
from scap.user_id_datatype_1 import UserIdDatatype1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class PasswordState(StateType):
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

    username: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    password: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional["PasswordState.UserId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    group_id: Optional["PasswordState.GroupId"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    gcos: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    home_dir: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    login_shell: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    last_login: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
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
    class GroupId(EntityStateAnySimpleType):
        datatype: GroupIdDatatype1 = field(
            default=GroupIdDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )
