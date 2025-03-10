from dataclasses import dataclass

from scap.platform_base_type import PlatformBaseType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class PlatformConfiguration(PlatformBaseType):
    class Meta:
        name = "platform-configuration"
        namespace = "http://cpe.mitre.org/language/2.0"
