from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache"


@dataclass
class HttpdTest(TestType):
    """The httpd test is used to check the version of an installed httpd binary.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an httpd_test
    and the optional state element specifies the data to check.
    """

    class Meta:
        name = "httpd_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache"

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
