from dataclasses import dataclass

from scap.variable_type_2 import VariableType2

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Variable2(VariableType2):
    """
    A variable element holds information defined by the author, an answer value, or
    values from external sources.
    """

    class Meta:
        name = "variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
