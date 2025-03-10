from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ReferenceType4:
    """This element provides supplementary descriptive text for a XCCDF elements.

    When used, it has either a simple string value or a value consisting
    of simple Dublin Core elements. If a bare string appears, then it is
    taken to be the string content for a Dublin Core title element.
    Multiple &lt;xccdf:reference&gt; elements may appear; a document
    generation processing tool may concatenate them, or put them into a
    reference list, and may choose to number them.

    :ivar href: A URL pointing to the referenced resource.
    :ivar override: Used to manage inheritance processing.
    :ivar content:
    """

    class Meta:
        name = "referenceType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    override: Optional[bool] = field(
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
