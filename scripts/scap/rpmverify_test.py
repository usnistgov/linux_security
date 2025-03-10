from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpmverifyTest(TestType):
    """The rpmverify_test is used to verify the integrity of installed RPMs. This
    test aligns with the rpm -V command for verifying RPMs. It extends the standard
    TestType as defined in the oval-definitions-schema and one should refer to the
    TestType description for more information.

    The required object element references a rpmverify_object and the
    optional state element specifies the data to check.
    """

    class Meta:
        name = "rpmverify_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

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
