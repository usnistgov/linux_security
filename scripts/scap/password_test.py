from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class PasswordTest(TestType):
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
