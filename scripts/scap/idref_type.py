from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class IdrefType:
    """
    Data type for elements that contain a reference to another XCCDF element.

    :ivar idref: The id value of another XCCDF element
    """

    class Meta:
        name = "idrefType"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
