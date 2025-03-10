from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class NotesType2:
    """The NotesType complex type defines an element that consists of one or more
    child note elements.

    It is assumed that each of these note elements is representative of
    the same language as defined by their parent.
    """

    class Meta:
        name = "NotesType"

    note: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
