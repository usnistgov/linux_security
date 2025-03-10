from dataclasses import dataclass

from scap.rule_type import RuleType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Rule(RuleType):
    """The &lt;xccdf:Rule&gt; element contains the description for a single item of
    guidance or constraint.

    &lt;xccdf:Rule&gt; elements form the basis for testing a target
    platform for compliance with an &lt;xccdf:Benchmark&gt;, for
    scoring, and for conveying descriptive prose, identifiers,
    references, and remediation information.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
