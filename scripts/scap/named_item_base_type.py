from dataclasses import dataclass, field
from typing import Optional

from scap.item_base_type import ItemBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NamedItemBaseType(ItemBaseType):
    """
    The NamedItemBaseType complex type defines structures allowing a set of notes
    and the name of a target (system or user) to be included.

    :ivar name: The name element holds the name of a target (system or
        user).
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
