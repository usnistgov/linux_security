from dataclasses import dataclass, field

from scap.possible_restriction_type import PossibleRestrictionType
from scap.possible_value_type import PossibleValueType
from scap.variable_type_1 import VariableType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ExternalVariable1(VariableType1):
    """The external_variable element extends the VariableType and defines a
    variable with some external source.

    The actual value(s) for the variable is not provided within the OVAL
    file, but rather it is retrieved during the evaluation of the OVAL
    Definition from an external source. An unbounded set of possible-
    value and possible_restriction child elements can be specified that
    together specify the list of all possible values that an external
    source is allowed to supply for the external variable. In other
    words, the value assigned by an external source must match one of
    the possible_value or possible_restriction elements specified. Each
    possible_value element contains a single value that could be
    assigned to the given external_variable while each
    possible_restriction element outlines a range of possible values.
    Note that it is not necessary to declare a variable's possible
    values, but the option is available if desired. If no possible child
    elements are specified, then the valid values are only bound to the
    specified datatype of the external variable. Please refer to the
    description of the PossibleValueType and PossibleRestrictionType
    complex types for more information.
    """

    class Meta:
        name = "external_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    possible_value: list[PossibleValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    possible_restriction: list[PossibleRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
