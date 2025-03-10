from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TailoringReferenceType:
    """Type for the &lt;xccdf:tailoring&gt; element within an
    &lt;xccdf:TestResult&gt;.

    This element is used to indicate the identity and location of an
    &lt;xccdf:Tailoring&gt; file that was used to create the assessment
    results.

    :ivar href: The URI of the &lt;xccdf:Tailoring&gt; file's location.
    :ivar id: The &lt;xccdf:Tailoring&gt; element's @id value.
    :ivar version: The value of the &lt;xccdf:Tailoring&gt; element's
        &lt;xccdf:version&gt; property.
    :ivar time: The value of the @time attribute in the
        &lt;xccdf:Tailoring&gt; element's &lt;xccdf:version&gt;
        property.
    """

    class Meta:
        name = "tailoringReferenceType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
