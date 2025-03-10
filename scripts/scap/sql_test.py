from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class SqlTest(TestType):
    """The sql test is used to check information stored in a database.

    It is often the case that applications store configuration settings
    in a database as opposed to a file. This test has been designed to
    enable those settings to be tested. It extends the standard TestType
    as defined in the oval-definitions-schema and one should refer to
    the TestType description for more information. The required object
    element references a wmi_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "sql_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

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
