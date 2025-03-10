from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileSetValueType:
    """Type for the &lt;xccdf:set-value&gt; element in an &lt;xccdf:Profile&gt;.

    This element upports the direct specification of simple value types
    such as numbers, strings, and boolean values. This overrides the
    &lt;xccdf:value&gt; and &lt;xccdf:complex-value&gt; element(s) of an
    &lt;xccdf:Value&gt; element.

    :ivar value:
    :ivar idref: The @id value of an &lt;xccdf:Value&gt; or the
        @cluster-id value of one or more &lt;xccdf:Value&gt; elements
    """

    class Meta:
        name = "profileSetValueType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
