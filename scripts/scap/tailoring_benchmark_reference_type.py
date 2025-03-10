from dataclasses import dataclass, field
from typing import Optional

from scap.benchmark_reference_type import BenchmarkReferenceType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TailoringBenchmarkReferenceType(BenchmarkReferenceType):
    """
    Identifies the &lt;xccdf:Benchmark&gt; to which an &lt;xccdf:Tailoring&gt;
    element applies.

    :ivar version: Identifies the version of the referenced
        &lt;xccdf:Benchmark&gt;.
    """

    class Meta:
        name = "tailoringBenchmarkReferenceType"

    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
