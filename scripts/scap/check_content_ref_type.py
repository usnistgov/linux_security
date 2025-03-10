from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class CheckContentRefType:
    """Data type for the &lt;xccdf:check-content-ref&gt; element, which points to
    the code for a detached check in another file.

    This element has no body, just a couple of attributes: @href and
    @name. The @name is optional, if it does not appear then this
    reference is to the entire document.

    :ivar href: Identifies the referenced document containing checking
        instructions.
    :ivar name: Identifies a particular part or element of the
        referenced check document.
    """

    class Meta:
        name = "checkContentRefType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
