from dataclasses import dataclass

from scap.variable_type_2 import VariableType2

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ExternalVariableType(VariableType2):
    """
    The ExternalVariableType type defines structures containing a value defined
    elsewhere or some external source.
    """
