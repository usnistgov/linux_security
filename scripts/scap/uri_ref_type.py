from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class UriRefType:
    """
    Data type for elements that have no content and a single @uri attribute.

    :ivar uri: A URI.
    """

    class Meta:
        name = "uriRefType"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
