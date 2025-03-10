from dataclasses import dataclass, field
from typing import Optional

from scap.platform_base_type import PlatformBaseType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class PlatformType(PlatformBaseType):
    """
    :ivar id: A locally unique name for the platform. There is no
        defined format for this id; however, it must be unique within
        the containing CPE Applicability Language document.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
