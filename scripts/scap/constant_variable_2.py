from dataclasses import dataclass

from scap.constant_variable_type import ConstantVariableType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ConstantVariable2(ConstantVariableType):
    """
    A constant_variable element holds a value defined by the author of the
    document.
    """

    class Meta:
        name = "constant_variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
