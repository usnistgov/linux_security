from dataclasses import dataclass, field
from typing import Optional

from scap.interface_hint_type import InterfaceHintType
from scap.item_type_abstract import ItemTypeAbstract
from scap.sel_choices_type import SelChoicesType
from scap.sel_complex_value_type import SelComplexValueType
from scap.sel_num_type import SelNumType
from scap.sel_string_type import SelStringType
from scap.signature_type_2 import SignatureType2
from scap.uri_ref_type import UriRefType
from scap.value_operator_type import ValueOperatorType
from scap.value_type_type import ValueTypeType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ValueType2(ItemTypeAbstract):
    """
    Data type for the &lt;xccdf:Value&gt; element, which is a named parameter that
    can be substituted into properties of other elements within the
    &lt;xccdf:Benchmark&gt;, including the interior of structured check
    specifications and fix scripts.

    :ivar value: A simple (number, string, or boolean) value associated
        with this &lt;xccdf:Value&gt;. At any time an
        &lt;xccdf:Value&gt; has one active (simple or complex) value. If
        a selector value has been provided under &lt;xccdf:Profile&gt;
        selection or tailoring then the active
        &lt;xccdf:value&gt;/&lt;xccdf:complex-value&gt; is the one with
        a matching @selector. If there is no provided selector or if the
        provided selector does not match the @selector attribute of any
        &lt;xccdf:value&gt; or &lt;xccdf:complex-value&gt;, the active
        &lt;xccdf:value&gt;/&lt;xccdf:complex-value&gt; is the one with
        an empty or absent @selector or, failing that, the first
        &lt;xccdf:value&gt; or &lt;xccdf:complex-value&gt; in the XML.
        When an &lt;xccdf:Value&gt; is exported or used in text
        substitution, it is the currently active &lt;xccdf:value&gt; or
        &lt;xccdf:complex-value&gt; that is actually used. If there are
        multiple &lt;xccdf:value&gt; and/or &lt;xccdf:complex-value&gt;
        elements, only one may omit a @selector attribute and no two may
        have the same @selector value.
    :ivar complex_value: A complex (list) value associated with this
        &lt;xccdf:Value&gt;. See the description of the
        &lt;xccdf:value&gt; property for &lt;xccdf:Rule&gt; elements
        regarding activation of an &lt;xccdf:complex-value&gt;.
    :ivar default: The default value displayed to the user as a
        suggestion by benchmark producers during tailoring of this
        &lt;xccdf:Value&gt; element. (This is not the default value of
        an &lt;xccdf:Value&gt;; it is just the default display.) If
        there are multiple &lt;xccdf:default&gt; and/or
        &lt;xccdf:complex-default&gt; elements, only one may omit a
        @selector attribute and no two may have the same @selector
        value.
    :ivar complex_default: The default &lt;xccdf:complex-value&gt;
        displayed to the user as a suggestion by benchmark producers
        during tailoring of this &lt;xccdf:Value&gt; element. (This is
        not the default value of an &lt;xccdf:Value&gt;; it is just the
        default display.) If there are multiple &lt;xccdf:default&gt;
        and &lt;xccdf:complex-default&gt; elements, only one may omit a
        @selector attribute and no two may have the same @selector
        value.
    :ivar match: A Perl Compatible Regular Expression that a benchmark
        producer may apply during tailoring to validate a user’s input
        for the &lt;xccdf:Value&gt;. It uses implicit anchoring. It
        applies only when the @type property is “string” or “number” or
        a list of strings and/or numbers.
    :ivar lower_bound: Minimum legal value for this &lt;xccdf:Value&gt;.
        It is used to constrain value input during tailoring, when the
        @type property is “number”. Values supplied by the user for
        tailoring the &lt;xccdf:Benchmark&gt; must be equal to or
        greater than this number.
    :ivar upper_bound: Maximum legal value for this &lt;xccdf:Value&gt;.
        It is used to constrain value input during tailoring, when the
        @type is “number”. Values supplied by the user for tailoring the
        &lt;xccdf:Benchmark&gt; must be less than or equal to than this
        number.
    :ivar choices: A list of legal or suggested choices (values) for an
        &lt;xccdf:Value&gt; element, to be used during tailoring and
        document generation.
    :ivar source: URI indicating where the tool may acquire values,
        value bounds, or value choices for this &lt;xccdf:Value&gt;
        element. XCCDF does not attach any meaning to the URI; it may be
        an arbitrary community or tool-specific value, or a pointer
        directly to a resource. If several instances of the
        &lt;xccdf:source&gt; property appear, then they represent
        alternative means or locations for obtaining the value in
        descending order of preference (i.e., most preferred first).
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:Value&gt;.
    :ivar id: The unique identifier for this element.
    :ivar type_value: The data type of the &lt;xccdf:Value&gt;. A tool
        may choose any convenient form to store an &lt;xccdf:Value&gt;
        element’s &lt;xccdf:value&gt; element, but the @type attribute
        conveys how the &lt;xccdf:Value&gt; should be treated for user
        input validation purposes during tailoring processing. The @type
        attribute may also be used to give additional guidance to the
        user or to validate the user’s input. In the case of a list of
        values, the @type attribute, if present, applies to all elements
        of the list individually.
    :ivar operator: The operator to be used for comparing this
        &lt;xccdf:Value&gt; to some part of the test system’s
        configuration during &lt;xccdf:Rule&gt; checking.
    :ivar interactive: Whether tailoring for this &lt;xccdf:Value&gt;
        should be performed during &lt;xccdf:Benchmark&gt; application.
        The benchmark consumer may ignore the attribute if asking the
        user is not feasible or not supported.
    :ivar interface_hint: A hint or recommendation to a benchmark
        consumer or producer about how the user might select or adjust
        the &lt;xccdf:Value&gt;.
    """

    class Meta:
        name = "valueType"

    value: list[SelStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    complex_value: list[SelComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "complex-value",
            "type": "Element",
            
        },
    )
    default: list[SelStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    complex_default: list[SelComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "complex-default",
            "type": "Element",
            
        },
    )
    match: list[SelStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    lower_bound: list[SelNumType] = field(
        default_factory=list,
        metadata={
            "name": "lower-bound",
            "type": "Element",
            
        },
    )
    upper_bound: list[SelNumType] = field(
        default_factory=list,
        metadata={
            "name": "upper-bound",
            "type": "Element",
            
        },
    )
    choices: list[SelChoicesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    source: list[UriRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    signature: Optional[SignatureType2] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_value_.+",
        },
    )
    type_value: ValueTypeType = field(
        default=ValueTypeType.STRING,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    operator: ValueOperatorType = field(
        default=ValueOperatorType.EQUALS,
        metadata={
            "type": "Attribute",
        },
    )
    interactive: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    interface_hint: Optional[InterfaceHintType] = field(
        default=None,
        metadata={
            "name": "interfaceHint",
            "type": "Attribute",
        },
    )
