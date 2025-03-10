from dataclasses import dataclass, field
from typing import Optional

from scap.chg_allow_datatype_1 import ChgAllowDatatype1
from scap.chg_lst_datatype_1 import ChgLstDatatype1
from scap.chg_req_datatype_1 import ChgReqDatatype1
from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_encrypt_method_type import EntityStateEncryptMethodType
from scap.entity_state_string_type import EntityStateStringType
from scap.exp_date_datatype_1 import ExpDateDatatype1
from scap.exp_inact_datatype_1 import ExpInactDatatype1
from scap.exp_warn_datatype_1 import ExpWarnDatatype1
from scap.flag_datatype_1 import FlagDatatype1
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class ShadowState(StateType):
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
    :ivar chg_req: This describes how long the user can keep a password
        before the system forces them to change it.
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
    :ivar flag: This is a numeric reserved field that the shadow file
        may use in the future.
    :ivar encrypt_method: The encrypt_method entity describes method
        that is used for hashing passwords.
    """

    class Meta:
        name = "shadow_state"
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
    chg_lst: Optional["ShadowState.ChgLst"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    chg_allow: Optional["ShadowState.ChgAllow"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    chg_req: Optional["ShadowState.ChgReq"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exp_warn: Optional["ShadowState.ExpWarn"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exp_inact: Optional["ShadowState.ExpInact"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exp_date: Optional["ShadowState.ExpDate"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    flag: Optional["ShadowState.Flag"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    encrypt_method: Optional[EntityStateEncryptMethodType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class ChgLst(EntityStateAnySimpleType):
        datatype: ChgLstDatatype1 = field(
            default=ChgLstDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ChgAllow(EntityStateAnySimpleType):
        datatype: ChgAllowDatatype1 = field(
            default=ChgAllowDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ChgReq(EntityStateAnySimpleType):
        datatype: ChgReqDatatype1 = field(
            default=ChgReqDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpWarn(EntityStateAnySimpleType):
        datatype: ExpWarnDatatype1 = field(
            default=ExpWarnDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpInact(EntityStateAnySimpleType):
        datatype: ExpInactDatatype1 = field(
            default=ExpInactDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExpDate(EntityStateAnySimpleType):
        datatype: ExpDateDatatype1 = field(
            default=ExpDateDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Flag(EntityStateAnySimpleType):
        datatype: FlagDatatype1 = field(
            default=FlagDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )
