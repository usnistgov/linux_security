from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ParamType:
    """Type for a parameter used in the &lt;xccdf:model&gt; element, which records
    scoring model information.

    The contents of this type represent a name-value pair, where the
    name is recorded in the @name attribute and the value appears in the
    element body. &lt;xccdf:param&gt; elements with equal values for the
    @name attribute may not appear as children of the same
    &lt;xccdf:model&gt; element.

    :ivar value:
    :ivar name: The name associated with the contained value.
    """

    class Meta:
        name = "paramType"

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
