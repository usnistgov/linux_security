from dataclasses import dataclass

from scap.tailoring_type import TailoringType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Tailoring(TailoringType):
    """The &lt;xccdf:Tailoring&gt; element holds one or more &lt;xccdf:Profile&gt;
    elements.

    These &lt;xccdf:Profile&gt; elements record additional tailoring
    activities that apply to a given &lt;xccdf:Benchmark&gt;.
    &lt;xccdf:Tailoring&gt; elements are separate from
    &lt;xccdf:Benchmark&gt; documents, but each &lt;xccdf:Tailoring&gt;
    element is associated with a specific &lt;xccdf:Benchmark&gt;
    document. By defining these tailoring actions separately from the
    &lt;xccdf:Benchmark&gt; document to which they apply, these actions
    can be recorded without affecting the integrity of the source
    itself.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
