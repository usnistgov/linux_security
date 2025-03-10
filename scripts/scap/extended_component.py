from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class ExtendedComponent:
    """
    A component that holds non-standard SCAP content.

    :ivar other_element:
    :ivar id: This MUST be a globally unique ID.
    :ivar timestamp: The time when the component was created or last
        modified.
    """

    class Meta:
        name = "extended-component"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"scap_[^_]+_ecomp_.+",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
