from dataclasses import dataclass, field
from typing import Optional

from scap.chg_allow_datatype_2 import ChgAllowDatatype2
from scap.chg_lst_datatype_2 import ChgLstDatatype2
from scap.chg_req_datatype_2 import ChgReqDatatype2
from scap.entity_item_encrypt_method_type import EntityItemEncryptMethodType
from scap.exp_date_datatype_2 import ExpDateDatatype2
from scap.exp_inact_datatype_2 import ExpInactDatatype2
from scap.exp_warn_datatype_2 import ExpWarnDatatype2
from scap.flag_datatype_2 import FlagDatatype2

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
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
    chg_lst: Optional["ShadowItem.ChgLst"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    chg_allow: Optional["ShadowItem.ChgAllow"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    chg_req: Optional["ShadowItem.ChgReq"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exp_warn: Optional["ShadowItem.ExpWarn"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exp_inact: Optional["ShadowItem.ExpInact"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exp_date: Optional["ShadowItem.ExpDate"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flag: Optional["ShadowItem.Flag"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    encrypt_method: Optional[EntityItemEncryptMethodType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class ChgLst:
        datatype: ChgLstDatatype2 = field(
            default=ChgLstDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ChgAllow:
        datatype: ChgAllowDatatype2 = field(
            default=ChgAllowDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ChgReq:
        datatype: ChgReqDatatype2 = field(
            default=ChgReqDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpWarn:
        datatype: ExpWarnDatatype2 = field(
            default=ExpWarnDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpInact:
        datatype: ExpInactDatatype2 = field(
            default=ExpInactDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpDate:
        datatype: ExpDateDatatype2 = field(
            default=ExpDateDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Flag:
        datatype: FlagDatatype2 = field(
            default=FlagDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )
