from dataclasses import dataclass, field
from typing import Optional

from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ReferenceType3(TextType3):
    """The ReferenceType complex type defines structures used to hold information
    about an external reference given its URI and description.

    This structure may be used to reference other standards such as CVE,
    CCE, or CPE. To do so, the href attribute would give the relevant
    namespace. For example, the namespace of the current version of CPE
    is
    http://cpe.mitre.org/dictionary/2.0
    and the body of this element
    would hold a specific CPE identifier. References to other information
    (documents, web pages, etc.) are also permitted.

    :ivar href: The href attribute holds the URI of an external
        reference. This may be the namespace associated with the
        information in the body or a web URL containing relevant
        information.
    :ivar content:
    """

    class Meta:
        name = "ReferenceType"

    href: Optional[str] = field(
        default=None,
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
        },
    )
