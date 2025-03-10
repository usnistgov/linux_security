from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from scap.role_enum_type import RoleEnumType
from scap.severity_enum_type import SeverityEnumType
from scap.text_type_4 import TextType4

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileRefineRuleType:
    """Type for the &lt;xccdf:refine-rule&gt; element in an &lt;xccdf:Profile&gt;.

    A &lt;xccdf:refine-rule&gt; element allows the author to select
    &lt;xccdf:check&gt; statements and override the @weight, @severity,
    and @role of an &lt;xccdf:Rule&gt;, &lt;xccdf:Group&gt;, or cluster
    of &lt;xccdf:Rule&gt; and &lt;xccdf:Group&gt; elements. Despite the
    name, this selector does apply for &lt;xccdf:Group&gt; elements and
    for clusters that include &lt;xccdf:Group&gt; elements, but it only
    affects their @weight attribute.

    :ivar remark: Explanatory material or other prose.
    :ivar idref: The @id value of an &lt;xccdf:Rule&gt; or
        &lt;xccdf:Group&gt;, or the @cluster-id value of one or more
        &lt;xccdf:Rule&gt; or &lt;xccdf:Group&gt; elements.
    :ivar weight: The new value for the identified element's @weight
        property.
    :ivar selector: Holds a selector value corresponding to the value of
        a @selector property in an &lt;xccdf:Rule&gt; element's
        &lt;xccdf:check&gt; element. If the selector specified does not
        match any of the @selector attributes specified on any of the
        &lt;xccdf:check&gt; children of an &lt;xccdf:Rule&gt;, then the
        &lt;xccdf:check&gt; child element without a @selector attribute
        is used. If there is no child without a @selector attribute,
        then that Rule would have no effective &lt;xccdf:check&gt;
        element.
    :ivar severity: The new value for the identified &lt;xccdf:Rule&gt;
        element's @severity property.
    :ivar role: The new value for the identified &lt;xccdf:Rule&gt;
        element's @role property.
    """

    class Meta:
        name = "profileRefineRuleType"

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
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "total_digits": 3,
        },
    )
    selector: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    severity: Optional[SeverityEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    role: Optional[RoleEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
