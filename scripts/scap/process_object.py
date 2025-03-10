from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class ProcessObject(ObjectType2):
    """The process_object element is used by a process test to define the specific
    process(es) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A process object defines the command line used
    to start the process(es).

    :ivar set:
    :ivar command: The command element specifies the command/program
        name to check.
    """

    class Meta:
        name = "process_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    command: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
