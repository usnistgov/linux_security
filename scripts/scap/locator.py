from dataclasses import dataclass

from scap.locator_type import LocatorType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Locator(LocatorType):
    class Meta:
        name = "locator"
        namespace = "http://www.w3.org/1999/xlink"
