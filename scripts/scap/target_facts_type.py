from dataclasses import dataclass, field

from scap.fact_type import FactType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TargetFactsType:
    """Data type for the &lt;xccdf:target-facts&gt; elements in
    &lt;xccdf:TestResult&gt; elements.

    A &lt;xccdf:target-facts&gt; element holds a list of named facts
    about the target system or platform. Each fact is an element of type
    factType. Each &lt;xccdf:fact&gt; must have a name, but duplicate
    names are allowed. (For example, if you had a fact about MAC
    addresses, and the target system had three NICs, then you'd need
    three instances of the "urn:xccdf:fact:ethernet:MAC" fact.)

    :ivar fact: A named fact about the target system or platform.
    """

    class Meta:
        name = "targetFactsType"

    fact: list[FactType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
