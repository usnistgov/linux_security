from dataclasses import dataclass, field
from typing import Optional

from scap.fact_ref_type import FactRefType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class CheckFactRefType(FactRefType):
    """A reference to a check that always evaluates to a TRUE, FALSE, or ERROR
    result.

    The CheckFactRefType complex type is used to define an element for
    holding information about an individual check. It includes a
    checking system specification URI, string content identifying the
    check content to invoke, and an external reference. The checking
    system specification should be the URI that uniquely identifies a
    revision of a check system language, and the id-ref will be an
    identifier of a test written in that language. The external
    reference should be used to point to the content in which the check
    identifier is defined.
    """

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
            "required": True,
        },
    )
    id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-ref",
            "type": "Attribute",
            "required": True,
        },
    )
