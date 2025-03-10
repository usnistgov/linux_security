from dataclasses import dataclass, field
from typing import Optional

from scap.complex_value_type import ComplexValueType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class SelChoicesType:
    """
    The type of the &lt;xccdf:choice&gt; element, which specifies a list of legal
    or suggested choices for an &lt;xccdf:Value&gt; object.

    :ivar choice: A single choice holding a simple type. (I.e., number,
        string, or boolean.)
    :ivar complex_choice: A single choice holding a list of simple
        types.
    :ivar must_match: True if the listed choices are the only
        permissible settings for the given &lt;xccdf:Value&gt;. False if
        choices not specified in this &lt;xccdf:choices&gt; element are
        acceptable settings for this &lt;xccdf:Value&gt;.
    :ivar selector: This may be referenced from &lt;xccdf:Profile&gt;
        selection elements or used during manual tailoring to refine the
        application of the &lt;xccdf:Rule&gt;. If no selectors are
        specified for a given &lt;xccdf:Value&gt; by
        &lt;xccdf:Profile&gt; elements or manual tailoring, an
        &lt;xccdf:choice&gt; element with an empty or non-existent
        @selector attribute is activated. If a selector is applied that
        does not match the @selector attribute of any
        &lt;xccdf:choices&gt; element, then no &lt;xccdf:choices&gt;
        element is considered activated.
    """

    class Meta:
        name = "selChoicesType"

    choice: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    complex_choice: list[ComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "complex-choice",
            "type": "Element",
            
        },
    )
    must_match: Optional[bool] = field(
        default=None,
        metadata={
            "name": "mustMatch",
            "type": "Attribute",
        },
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
