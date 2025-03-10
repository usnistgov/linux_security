from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue
from scap.sub_type import SubType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TextWithSubType:
    """
    Type for a string with embedded &lt;xccdf:Value&gt; substitutions and an
    @override attribute to help manage inheritance.

    :ivar lang:
    :ivar override: Used to manage inheritance.
    :ivar content:
    """

    class Meta:
        name = "textWithSubType"

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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": SubType,
                    
                },
            ),
        },
    )
