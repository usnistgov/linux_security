from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class PlainTextType:
    """The data type for an &lt;xccdf:plain-text&gt; element, which is a reusable
    text block for reference by the &lt;xccdf:sub&gt; element.

    This allows text to be defined once and then reused multiple times.
    Each &lt;xccdf:plain-text&gt; element mush have a unique id.

    :ivar value:
    :ivar id: The unique identifier for this &lt;xccdf:plain-text&gt;
        element.
    """

    class Meta:
        name = "plainTextType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
