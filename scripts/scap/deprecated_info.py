from dataclasses import dataclass

from scap.deprecated_info_type import DeprecatedInfoType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class DeprecatedInfo(DeprecatedInfoType):
    """The deprecated_info element is used in documenting deprecation information
    for items in the OVAL Language.

    It is declared globally as it can be found in any of the OVAL
    schemas and is used as part of the appinfo documentation and
    therefore it is not an element that can be declared locally and
    based off a global type..
    """

    class Meta:
        name = "deprecated_info"
        namespace = "http://oval.mitre.org/XMLSchema/oval-common-5"
