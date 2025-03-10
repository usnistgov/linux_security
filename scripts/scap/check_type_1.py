from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class CheckType1:
    """The CheckType complex type is used to define an element to hold information
    about an individual check.

    It includes a checking system specification URI, string content, and
    an optional external file reference. The checking system
    specification should be the URI for a particular version of OVAL or
    a related system testing language, and the content will be an
    identifier of a test written in that language. The external file
    reference could be used to point to the file in which the content
    test identifier is defined.
    """

    class Meta:
        name = "CheckType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
