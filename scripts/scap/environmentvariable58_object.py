from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_int_type import EntityObjectIntType
from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Environmentvariable58Object(ObjectType2):
    """The environmentvariable58_object element is used by an
    environmentvariable58_test to define the specific environment variable(s) and
    process IDs to be evaluated.

    If a tool is unable to collect the environment variables of another
    process, an error must be reported.  Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. Again, please refer to the description of the
    set element in the oval-definitions-schema.

    :ivar set:
    :ivar pid: The process ID of the process from which the environment
        variable should be retrieved. If the xsi:nil attribute is set to
        true, the process ID shall be the tool's running process; for
        scanners with no process ID (e.g., an agentless network
        scanner), no corresponding items will exist.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar filter:
    """

    class Meta:
        name = "environmentvariable58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    pid: Optional[EntityObjectIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
