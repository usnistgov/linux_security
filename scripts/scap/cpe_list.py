from dataclasses import dataclass

from scap.list_type import ListType

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class CpeList(ListType):
    """The cpe-list element acts as a top-level container for CPE Name items.

    Each individual item must be unique. Please refer to the description
    of ListType for additional information about the structure of this
    element.
    """

    class Meta:
        name = "cpe-list"
        namespace = "http://cpe.mitre.org/dictionary/2.0"
