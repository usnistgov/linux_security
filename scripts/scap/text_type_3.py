from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TextType3:
    """
    The TextType complex type defines an element that holds basic string
    information.

    :ivar value:
    :ivar lang: This attribute specifies the language in which to
        interpret the information.
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
