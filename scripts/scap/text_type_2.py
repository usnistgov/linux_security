from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class TextType2:
    """
    The TextType complex type allows the xml:lang attribute to associate a specific
    language with an element's string content.
    """

    class Meta:
        name = "TextType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
