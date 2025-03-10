from dataclasses import dataclass, field

from scap.value_type_1 import ValueType1
from scap.variable_type_1 import VariableType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ConstantVariable1(VariableType1):
    """The constant_variable element extends the VariableType and defines a
    variable with a constant value(s).

    Each constant_variable defines either a single value or a collection
    of values to be used throughout the evaluation of the OVAL
    Definition File in which it has been defined. Constant variables
    cannot be over-ridden by an external source. The actual value of a
    constant variable is defined by the required value child element. A
    collection of values can be specified by including multiple
    instances of the value element. Please refer to the description of
    the ValueType complex type for more information.
    """

    class Meta:
        name = "constant_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    value: list[ValueType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )
