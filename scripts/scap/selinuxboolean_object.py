from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class SelinuxbooleanObject(ObjectType2):
    """
    The selinuxboolean_object element is used by an selinuxboolean_test to define
    the items to evaluate based on a specified state.

    :ivar set:
    :ivar name: The name of the SELinux boolean.
    :ivar filter:
    """

    class Meta:
        name = "selinuxboolean_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
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
