from dataclasses import dataclass

from scap.profile_type import ProfileType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Profile(ProfileType):
    """The &lt;xccdf:Profile&gt; element is a named tailoring for an
    &lt;xccdf:Benchmark&gt;.

    While an &lt;xccdf:Benchmark&gt; can be tailored in place by setting
    properties of various elements, &lt;xccdf:Profile&gt; elements allow
    one &lt;xccdf:Benchmark&gt; document to hold several independent
    tailorings.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
