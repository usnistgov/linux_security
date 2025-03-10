from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_family_type import EntityItemFamilyType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class FamilyItem:
    """
    This element stores high level system OS type, otherwise known as the family.

    :ivar family: This element describes the high level system OS type,
        otherwise known as the family.
    """

    class Meta:
        name = "family_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    family: Optional[EntityItemFamilyType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
