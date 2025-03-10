from dataclasses import dataclass, field

from scap.system import System
from scap.user import User

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TargetsType:
    """
    The TargetsType type defines structures containing a set of target elements.
    """

    system: list[System] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
