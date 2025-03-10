from dataclasses import dataclass

from scap.arc_type import ArcType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Arc(ArcType):
    class Meta:
        name = "arc"
        namespace = "http://www.w3.org/1999/xlink"
