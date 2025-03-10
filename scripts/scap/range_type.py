from dataclasses import dataclass, field
from typing import Optional

from scap.range_value_type import RangeValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class RangeType:
    """
    The RangeType type defines a structure that specifies a range against which a
    numeric response is to be compared.

    :ivar min: The min element contains a minimum value for the range.
    :ivar max: The max element contains a maximum value for teh range.
    """

    min: Optional[RangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    max: Optional[RangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
