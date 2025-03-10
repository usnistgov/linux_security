from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class IdentType:
    """Data type for the &lt;xccdf:ident&gt; element, a globally meaningful
    identifier for an &lt;xccdf:Rule&gt;.

    The body of &lt;xccdf:ident&gt; element is the name or identifier of
    a security configuration issue or vulnerability that the
    &lt;xccdf:Rule&gt; addresses. It has an associated URI that denotes
    the organization or naming scheme that assigned the name. By setting
    an &lt;xccdf:ident&gt; element on an &lt;xccdf:Rule&gt;, the
    &lt;xccdf:Benchmark&gt; author effectively declares that the
    &lt;xccdf:Rule&gt; instantiates, implements, or remediates the issue
    for which the name was assigned.

    :ivar value:
    :ivar system: Denotes the organization or naming scheme that
        assigned the identifier.
    :ivar other_attributes: May also have other attributes from other
        namespaces in order to provide additional metadata for the given
        identifier.
    """

    class Meta:
        name = "identType"

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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
