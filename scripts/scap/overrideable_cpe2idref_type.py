from dataclasses import dataclass, field

from scap.cpe2idref_type import Cpe2IdrefType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class OverrideableCpe2IdrefType(Cpe2IdrefType):
    """Data type for &lt;xccdf:platform&gt; elements that need
    @override attributes. (I.e., &lt;xccdf:platform&gt; elements that are in structures
    that can be extended, such as Items and &lt;xccdf:Profile&gt; elements.) This is
    used to identify the applicable target platform for its respective parent elements.

    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "overrideableCPE2idrefType"

    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
