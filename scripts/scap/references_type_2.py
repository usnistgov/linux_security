from dataclasses import dataclass, field

from scap.reference_type_3 import ReferenceType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ReferencesType2:
    """
    The ReferencesType complex type contains a set of references.

    :ivar reference: The reference element contains information about
        any external references. Examples could include references to
        other standards such as CVE, CCE, or CPE.
    """

    class Meta:
        name = "ReferencesType"

    reference: list[ReferenceType3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
