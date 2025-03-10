from dataclasses import dataclass, field
from typing import Optional

from scap.text_type_4 import TextType4

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileSelectType:
    """Type for the &lt;xccdf:select&gt; element in an &lt;xccdf:Profile&gt;.

    This element designates an &lt;xccdf:Rule&gt;, &lt;xccdf:Group&gt;,
    or cluster of &lt;xccdf:Rule&gt; and &lt;xccdf:Group&gt; elements
    and overrides the @selected attribute on the designated items,
    providing a means for including or excluding &lt;xccdf:Rule&gt;
    elements from an assessment.

    :ivar remark: Explanatory material or other prose.
    :ivar idref: The @id value of an &lt;xccdf:Rule&gt; or
        &lt;xccdf:Group&gt;, or the @cluster-id value of one or more
        &lt;xccdf:Rule&gt; or &lt;xccdf:Group&gt; elements.
    :ivar selected: The new value for the indicated item's @selected
        property.
    """

    class Meta:
        name = "profileSelectType"

    remark: list[TextType4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
