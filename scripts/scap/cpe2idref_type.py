from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Cpe2IdrefType:
    """Data type for &lt;xccdf:platform&gt; elements that do not need @override
    attributes.

    (I.e., &lt;xccdf:platform&gt; elements that are in structures that
    cannot be extended, such as &lt;xccdf:TestResult&gt; and
    &lt;xccdf:Benchmark&gt; elements.) This is used to identify the
    applicable target platform for its respective parent elements.

    :ivar idref: Should be a CPE 2.3 Applicability Language identifier
        using the Formatted String binding or the value of a
        &lt;cpe:platform-specification&gt; element's @id attribute, the
        latter acting as a reference to some expression defined using
        the CPE schema in the &lt;xccdf:Benchmark&gt; element's
        &lt;cpe:platform-specification&gt; element. The @idref may be a
        CPE Applicability Language identifier using the URI binding,
        although this is less preferred.
    """

    class Meta:
        name = "CPE2idrefType"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
