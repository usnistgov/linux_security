from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class VersionType:
    """
    Type for most &lt;xccdf:version&gt; elements.

    :ivar value:
    :ivar time: The time that this version of the associated element was
        completed.
    :ivar update: A URI indicating a location where updates to the
        associated element may be obtained.
    """

    class Meta:
        name = "versionType"

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
        },
    )
    update: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
