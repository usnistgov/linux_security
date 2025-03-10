from dataclasses import dataclass

from scap.value_type_2 import ValueType2

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Value(ValueType2):
    """
    The &lt;xccdf:Value&gt; element is a named parameter that can be substituted
    into properties of other elements within the &lt;xccdf:Benchmark&gt;, including
    the interior of structured check specifications and fix scripts.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
