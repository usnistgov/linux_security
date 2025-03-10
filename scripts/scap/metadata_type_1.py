from dataclasses import dataclass, field
from typing import Optional

from scap.affected_type import AffectedType
from scap.reference_type_2 import ReferenceType2

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class MetadataType1:
    """The MetadataType complex type contains all the metadata available to an OVAL
    Definition.

    This metadata is for informational purposes only and is not part of
    the criteria used to evaluate machine state. The required title
    child element holds a short string that is used to quickly identify
    the definition to a human user. The affected metadata item contains
    information about the system(s) for which the definition has been
    written. Remember that this is just metadata and not part of the
    criteria. Please refer to the AffectedType description for more
    information. The required description element contains a textual
    description of the configuration state being addressed by the OVAL
    Definition. In the case of a definition from the vulnerability
    class, the reference is usually the Common Vulnerability and
    Exposures (CVE) Identifier, and this description field corresponds
    with the CVE description. Additional metadata is also allowed
    although it is not part of the official OVAL Schema. Individual
    organizations can place metadata items that they feel are important
    and these will be skipped during the validation. All OVAL really
    cares about is that the stated metadata items are there.
    """

    class Meta:
        name = "MetadataType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    affected: list[AffectedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    reference: list[ReferenceType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
