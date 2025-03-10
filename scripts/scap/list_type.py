from dataclasses import dataclass, field
from typing import Optional

from scap.cpe_item import CpeItem
from scap.generator_type_2 import GeneratorType2

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class ListType:
    """The ListType complex type defines an element that is used to hold a
    collection of individual items.

    The required generator section provides information about when the
    definition file was compiled and under what version. Additional
    elements not part of the CPE namespace are allowed and are just
    skipped by validation. In essence, a dictionary file can contain
    additional information that a user can choose to use or not, but
    this information is not required to be used or understood.
    """

    generator: Optional[GeneratorType2] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    cpe_item: list[CpeItem] = field(
        default_factory=list,
        metadata={
            "name": "cpe-item",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/dictionary/2.0",
            "min_occurs": 1,
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
