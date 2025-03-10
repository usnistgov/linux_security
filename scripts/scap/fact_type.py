from dataclasses import dataclass, field
from typing import Optional

from scap.value_type_type import ValueTypeType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class FactType:
    """Data type for an &lt;xccdf:fact&gt; element, which
    holds information about a target system: a name-value pair with a type. The content
    of the element is the value, and the @name attribute indicates the name. The @name
    is in the form of a URI that indicates the nature of the fact. A table of defined
    fact URIs appears in section 6.6.3 of the XCCDF specification. Additional URIs may
    be defined by authors to indicate additional kinds of facts.

    :ivar value:
    :ivar name: A URI that indicates the name of the fact.
    :ivar type_value: The data type of the fact value.
    """

    class Meta:
        name = "factType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: ValueTypeType = field(
        default=ValueTypeType.BOOLEAN,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
