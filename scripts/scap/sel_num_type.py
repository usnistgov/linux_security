from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class SelNumType:
    """
    This type is for an element that has numeric content and a @selector attribute
    for use during tailoring.

    :ivar value:
    :ivar selector: This may be referenced from &lt;xccdf:Profile&gt;
        selection elements or used during manual tailoring to refine the
        application of this property. If no selectors are specified for
        a given property by &lt;xccdf:Profile&gt; elements or manual
        tailoring, properties with empty or non-existent @selector
        attributes are activated. If a selector is applied that does not
        match the @selector attribute of any of a given type of
        property, then no property of that type considered activated.
    """

    class Meta:
        name = "selNumType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
