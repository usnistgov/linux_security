from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class IflistenersTest(TestType):
    """The iflisteners_test is used to check what applications such as packet
    sniffers that are bound to an interface on the system.

    This is limited to applications that are listening on AF_PACKET
    sockets. Furthermore, only applications bound to an ethernet
    interface should be collected. It extends the standard TestType as
    defined in the oval-definitions-schema and one should refer to the
    TestType description for more information. The required object
    element references an iflisteners_object and the optional
    iflisteners_state element specifies the data to check.
    """

    class Meta:
        name = "iflisteners_test"
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
