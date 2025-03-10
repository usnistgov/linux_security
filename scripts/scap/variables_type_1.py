from dataclasses import dataclass, field

from scap.constant_variable_1 import ConstantVariable1
from scap.external_variable_1 import ExternalVariable1
from scap.local_variable_1 import LocalVariable1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class VariablesType1:
    """The VariablesType complex type is a container for one or more variable child
    elements.

    Each variable element is a way to define one or more values to be
    obtained at the time a definition is evaluated.
    """

    class Meta:
        name = "VariablesType"

    local_variable: list[LocalVariable1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    constant_variable: list[ConstantVariable1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    external_variable: list[ExternalVariable1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
