from dataclasses import dataclass, field
from typing import Optional

from scap.element_map_item_type import ElementMapItemType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class ElementMapType:
    """
    The ElementMapType is used to document the association between OVAL test,
    object, state, and item entities.

    :ivar test: The local name of an OVAL test.
    :ivar object_value: The local name of an OVAL object.
    :ivar state: The local name of an OVAL state.
    :ivar item: The local name of an OVAL item.
    """

    test: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    object_value: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            
        },
    )
    state: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    item: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
