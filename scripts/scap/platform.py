from dataclasses import dataclass

from scap.platform_type import PlatformType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class Platform(PlatformType):
    class Meta:
        name = "platform"
        namespace = "http://cpe.mitre.org/language/2.0"
