from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ReferenceType2:
    """The ReferenceType complex type links the OVAL Definition to a definitive
    external reference.

    For example, CVE Identifiers are used for referencing
    vulnerabilities. The intended purpose for this reference is to link
    the definition to a variety of other sources that address the same
    issue being specified by the OVAL Definition. The required source
    attribute specifies where the reference is coming from. In other
    words, it identifies the reference repository being used. The
    required ref_id attribute is the external id of the reference. The
    optional ref_url attribute is the URL to the reference.
    """

    class Meta:
        name = "ReferenceType"

    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref_url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
