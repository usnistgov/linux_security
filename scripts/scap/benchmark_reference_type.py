from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class BenchmarkReferenceType:
    """
    Type for a reference to the &lt;xccdf:Benchmark&gt; document.

    :ivar href: The URI of the &lt;xccdf:Benchmark&gt; document.
    :ivar id: The value of that &lt;xccdf:Benchmark&gt; element's @id
        attribute.
    """

    class Meta:
        name = "benchmarkReferenceType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
