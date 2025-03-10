from dataclasses import dataclass

from scap.platform_specification_type import PlatformSpecificationType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class PlatformSpecification(PlatformSpecificationType):
    """
    This element is the root element of a CPE Applicability Language XML document
    and therefore acts as a container for child platform definitions.
    """

    class Meta:
        name = "platform-specification"
        namespace = "http://cpe.mitre.org/language/2.0"
