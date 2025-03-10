from dataclasses import dataclass

from scap.item_type import ItemType

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class CpeItem(ItemType):
    """The cpe-item element denotes a single CPE Name.

    Please refer to the description of ItemType for additional
    information about the structure of this element.
    """

    class Meta:
        name = "cpe-item"
        namespace = "http://cpe.mitre.org/dictionary/2.0"
