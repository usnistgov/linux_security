from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SetExpressionBaseType:
    """The SetExpressionBaseType type is the base type of all set expressions.

    It defines the value to use if the expression evaluates to TRUE.

    :ivar value: The value element contains the data to be stored on the
        variable if the expression evaluates to TRUE.
    """

    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
