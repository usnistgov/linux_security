from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class SignatureType2:
    """
    The type of an &lt;XMLDSig:signature&gt; element, which holds an enveloped
    digital signature asserting authorship and allowing verification of the
    integrity of associated data (e.g., its parent element, other documents,
    portions of other documents).
    """

    class Meta:
        name = "signatureType"

    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "process_contents": "skip",
        },
    )
