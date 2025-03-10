from dataclasses import dataclass, field

from scap.complex_value_type import ComplexValueType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class SelComplexValueType(ComplexValueType):
    """
    Data type that supports values that are lists of simple types with an
    associated @selector attribute used in tailoring.

    :ivar selector: This may be referenced from &lt;xccdf:Profile&gt;
        selection elements or used during manual tailoring to refine the
        application of this property. If no selectors are specified for
        a given item by &lt;xccdf:Profile&gt; elements or manual
        tailoring, properties with empty or non-existent @selector
        attributes are activated. If a selector is applied that does not
        match the @selector attribute of any of a given type of
        property, then no &lt;xccdf:choices&gt; element is considered
        activated. The only exception is the &lt;xccdf:value&gt; and
        &lt;xccdf:complex-value&gt; properties of an &lt;xccdf:Value&gt;
        element - if there is no &lt;xccdf:value&gt; or
        &lt;xccdf:complex-value&gt; property with a matching @selector
        value then the &lt;xccdf:value&gt;/&lt;xccdf:complex-value&gt;
        property with an empty or absent @selector attribute becomes
        active. If there is no such &lt;xccdf:value&gt; or
        &lt;xccdf:complex-value&gt;, then the first &lt;xccdf:value&gt;
        or &lt;xccdf:complex-value&gt; listed becomes active. This
        reflects the fact that all &lt;xccdf:Value&gt; elements require
        an active value property at all times.
    """

    class Meta:
        name = "selComplexValueType"

    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
