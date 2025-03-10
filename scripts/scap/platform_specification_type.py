from dataclasses import dataclass, field

from scap.platform import Platform

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class PlatformSpecificationType:
    class Meta:
        name = "platformSpecificationType"

    platform: list[Platform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
            "min_occurs": 1,
        },
    )
