from dataclasses import dataclass, field
from typing import Optional

from scap.variable_type_2 import VariableType2

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ConstantVariableType(VariableType2):
    """
    The ConstantVariableType type defines structures containing a value defined by
    the author of the document.

    :ivar value: The value element holds the data stored on the
        variable.
    """

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
