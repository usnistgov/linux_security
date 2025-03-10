from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TextType4:
    """
    Type for a simple text string with an @override attribute for controlling
    inheritance.

    :ivar value:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "textType"

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
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
