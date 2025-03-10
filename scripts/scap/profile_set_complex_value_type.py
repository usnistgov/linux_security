from dataclasses import dataclass, field
from typing import Optional

from scap.complex_value_type import ComplexValueType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileSetComplexValueType(ComplexValueType):
    """Type for the &lt;xccdf:set-complex-value&gt; element in an
    &lt;xccdf:Profile&gt;.

    This element supports the direct specification of complex value
    types such as lists. Zero or more &lt;xccdf:item&gt; elements may
    appear as children of this element; if no child elements are
    present, this element represents an empty list. This overrides the
    &lt;xccdf:value&gt; and &lt;xccdf:complex-value&gt; element(s) of an
    &lt;xccdf:Value&gt; element.

    :ivar idref: The @id value of an &lt;xccdf:Value&gt; or the
        @cluster-id value of one or more &lt;xccdf:Value&gt; elements
    """

    class Meta:
        name = "profileSetComplexValueType"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
