from dataclasses import dataclass, field

from scap.constant_variable_2 import ConstantVariable2
from scap.external_variable_2 import ExternalVariable2
from scap.local_variable_2 import LocalVariable2

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class VariablesType2:
    """
    The VariablesType type defines structures containing a set of variables.
    """

    class Meta:
        name = "VariablesType"

    external_variable: list[ExternalVariable2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    local_variable: list[LocalVariable2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    constant_variable: list[ConstantVariable2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
