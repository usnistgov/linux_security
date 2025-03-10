from dataclasses import dataclass, field
from typing import Optional

from scap.text_type_4 import TextType4
from scap.value_operator_type import ValueOperatorType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileRefineValueType:
    """Type for the &lt;xccdf:refine-value&gt; element in an &lt;xccdf:Profile&gt;.

    This element designates the &lt;xccdf:Value&gt; constraints to be
    applied during tailoring for an &lt;xccdf:Value&gt; element or the
    &lt;xccdf:Value&gt; members of a cluster.

    :ivar remark: Explanatory material or other prose.
    :ivar idref: The @id value of an &lt;xccdf:Value&gt; or the
        @cluster-id value of one or more &lt;xccdf:Value&gt; elements
    :ivar selector: Holds a selector value corresponding to the value of
        a @selector property in an &lt;xccdf:Value&gt; element's child
        properties. Properties with a matching @selector are considered
        active and all other properties are inactive. This may mean
        that, after selector application, some classes of
        &lt;xccdf:Value&gt; properties will be completely inactive
        because none of those properties had a matching @selector. The
        only exception is the &lt;xccdf:value&gt; and &lt;xccdf:complex-
        value&gt; properties of an &lt;xccdf:Value&gt; element - if
        there is no &lt;xccdf:value&gt; or &lt;xccdf:complex-value&gt;
        property with a matching @selector value then the
        &lt;xccdf:value&gt;/&lt;xccdf:complex-value&gt; property with an
        empty or absent @selector attribute becomes active. If there is
        no such &lt;xccdf:value&gt; or &lt;xccdf:complex-value&gt;, then
        the first &lt;xccdf:value&gt; or &lt;xccdf:complex-value&gt;
        listed in the XML becomes active. This reflects the fact that
        all &lt;xccdf:Value&gt; elements require an active value
        property at all times.
    :ivar operator: The new value for the identified &lt;xccdf:Value&gt;
        element's @operator property.
    """

    class Meta:
        name = "profileRefineValueType"

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
    selector: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operator: Optional[ValueOperatorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
