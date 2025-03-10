from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TailoringVersionType:
    """
    Type for version information about an &lt;xccdf:Tailoring&gt; element.

    :ivar value:
    :ivar time: The time when this version of the
        &lt;xccdf:Tailoring&gt; document was completed.
    """

    class Meta:
        name = "tailoringVersionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
