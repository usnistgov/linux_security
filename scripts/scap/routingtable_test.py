from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class RoutingtableTest(TestType):
    """The routingtable_test is used to check information about the IPv4 and IPv6
    routing table entries found in a system's primary routing table.

    It is important to note that only numerical addresses will be
    collected and that their symbolic representations will not be
    resolved. This equivalent to using the '-n' option with route(8) or
    netstat(8). It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references a
    routingtable_object and the optional routingtable_state element
    specifies the data to check.
    """

    class Meta:
        name = "routingtable_test"
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
