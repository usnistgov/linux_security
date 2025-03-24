from dataclasses import dataclass, field
from typing import Optional

from scap.arithmetic_function_type import (
    ArithmeticFunctionType,
    BeginFunctionType,
    ConcatFunctionType,
    CountFunctionType,
    EndFunctionType,
    EscapeRegexFunctionType,
    GlobToRegexFunctionType,
    RegexCaptureFunctionType,
    SplitFunctionType,
    SubstringFunctionType,
    TimeDifferenceFunctionType,
    UniqueFunctionType,
)
from scap.literal_component_type import LiteralComponentType
from scap.object_component_type import ObjectComponentType
from scap.variable_component_type import VariableComponentType
from scap.variable_type_1 import VariableType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class LocalVariable1(VariableType1):
    """The local_variable element extends the VariableType and defines a variable
    with some local source.

    The actual value(s) for the variable is not provided in the OVAL
    Definition document but rather it is retrieved during the evaluation
    of the OVAL Definition. Each local variable is defined by either a
    single component or a complex function, meaning that a value can be
    as simple as a literal string or as complex as multiple registry
    keys concatenated together. Note that if an individual component is
    used and it returns a collection of values, then there will be
    multiple values associated with the local_variable. For example, if
    an object_component is used and it references a file object that
    identifies a set of 5 files, then the local variable would evaluate
    to a collection of those 5 values. Please refer to the description
    of the ComponentGroup for more information.
    """

    def evaluate_variable(self,data):
        print(self)
        # This may cause some issues because I'm expecting the variable checks to return a list, but
        # The object component's generation will definitely not be returning a list 
        if self.object_component:
            return data["objects"][self.object_component.object_ref].evaluate_object(data)
        if self.variable_component:
            return data["variables"][self.variable_component.var_ref].evaluate_variable(data)
        if self.literal_component:
            return self.literal_component.value

    class Meta:
        name = "local_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    escape_regex: Optional[EscapeRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    split: Optional[SplitFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    substring: Optional[SubstringFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    time_difference: Optional[TimeDifferenceFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    regex_capture: Optional[RegexCaptureFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional[UniqueFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional[CountFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional[GlobToRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
