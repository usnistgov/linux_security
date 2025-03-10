from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class ShadowTest(TestType):
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

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
