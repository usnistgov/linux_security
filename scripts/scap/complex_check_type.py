from dataclasses import dataclass, field
from typing import Optional

from scap.cc_operator_enum_type import CcOperatorEnumType
from scap.check_type_2 import CheckType2

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ComplexCheckType:
    """The type for an element that contains a boolean combination of
    &lt;xccdf:checks&gt;.

    This element can have only &lt;xccdf:complex-check&gt; and
    &lt;xccdf:check&gt; elements as children. Child elements may appear
    in any order but at least one child element must be present. It has
    two attributes, @operator and @negate, which dictate how
    &lt;xccdf:check&gt; or &lt;xccdf:complex-check&gt; child elements
    are to be combined. Truth tables for these operations appear below.

    :ivar check: Instructions for a single test.
    :ivar complex_check: A child &lt;xccdf:complex-check&gt;, allowing
        another level of logic in combining component checks.
    :ivar operator: Indicates whether the child &lt;xccdf:check&gt;
        and/or &lt;xccdf:complex-check&gt; elements of this
        &lt;xccdf:complex-check&gt; should be combined using an AND or
        OR operation
    :ivar negate: If true, negate the final result of this
        &lt;xccdf:complex-check&gt; after the child elements are
        combined using the identified operator.
    """

    class Meta:
        name = "complexCheckType"

    check: list[CheckType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    complex_check: list["ComplexCheckType"] = field(
        default_factory=list,
        metadata={
            "name": "complex-check",
            "type": "Element",
            
        },
    )
    operator: Optional[CcOperatorEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
