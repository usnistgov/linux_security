from dataclasses import dataclass, field
from typing import Optional

from scap.arithmetic_enumeration import ArithmeticEnumeration
from scap.date_time_format_enumeration import DateTimeFormatEnumeration
from scap.literal_component_type import LiteralComponentType
from scap.object_component_type import ObjectComponentType
from scap.variable_component_type import VariableComponentType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

@dataclass
class FunctionType:

    def evaluate_function(self,data):
        print("Base evaluation should not occur!")

@dataclass
class ArithmeticFunctionType(FunctionType):
    """The arithmetic function takes two or more integer or float components and
    performs a basic mathematical function on them.

    The result of this function is a single integer or float unless one
    of the components returns a collection of values. In this case the
    specified arithmetic function would be performed multiple times and
    the end result would also be a collection of values for the local
    variable. For example assume a local_variable specifies the
    arithmetic function with an arithmetic_operation of "add" and has
    two sub-components under this function: the first component returns
    "1" and "2", and the second component returns "3" and "4" and "5".
    The local_variable element would be evaluated to be a collection of
    six values: 1+3, 1+4, 1+5, 2+3, 2+4, and 2+5. Note that if both an
    integer and float components are used then the result is a float.
    """

    def evaluate_function(self, data):
        print("Evaluating arithmetic...")
        # First, enumerate recursively..
        if self.object_component:
            # Toy example reference, needs iteration
            data["objects"][self.object_component[0].object_ref].evaluate_object(data)

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    arithmetic: list["ArithmeticFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    begin: list["BeginFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    concat: list["ConcatFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    end: list["EndFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    escape_regex: list["EscapeRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    split: list["SplitFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    substring: list["SubstringFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    time_difference: list["TimeDifferenceFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    regex_capture: list["RegexCaptureFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    arithmetic_operation: Optional[ArithmeticEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BeginFunctionType(FunctionType):
    """The begin function takes a single string component and defines a character
    (or string) that the component string should start with.

    The character attribute defines the specific character (or string).
    The character (or string) is only added to the component string if
    the component string does not already start with the specified
    character (or string). If the component string does not start with
    the specified character (or string) the entire character (or string)
    will be prepended to the component string..
    """

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
    begin: Optional["BeginFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    concat: Optional["ConcatFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    end: Optional["EndFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    escape_regex: Optional["EscapeRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    character: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ConcatFunctionType(FunctionType):
    """The concat function takes two or more components and concatenates them
    together to form a single string.

    The first component makes up the beginning of the resulting string
    and any following components are added to the end it. If one of the
    components returns multiple values then the concat function would be
    performed multiple times and the end result would be a collection of
    values for the local variable. For example assume a local variable
    has two sub-components: a basic component element returns the values
    "abc" and "def", and a literal component element that has a value of
    "xyz". The local_variable element would evaluate to a collection of
    two values, "abcxyz" and "defxyz". If one of the components does not
    exist, then the result of the concat operation should be does not
    exist.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    concat: list["ConcatFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    end: list["EndFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    escape_regex: list["EscapeRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    split: list["SplitFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    substring: list["SubstringFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    time_difference: list["TimeDifferenceFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    regex_capture: list["RegexCaptureFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )


@dataclass
class EndFunctionType(FunctionType):
    """The end function takes a single string component and defines a character (or
    string) that the component string should end with.

    The character attribute defines the specific character (or string).
    The character (or string) is only added to the component string if
    the component string does not already end with the specified
    character (or string). If the desired end character is a string,
    then the entire end string must exist at the end if the component
    string. If the entire end string is not present then the entire end
    string is appended to the component string.
    """

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
    end: Optional["EndFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    escape_regex: Optional["EscapeRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    character: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EscapeRegexFunctionType(FunctionType):
    """The escape_regex function takes a single string component and escapes all of
    the regular expression characters.

    If the string sub-component contains multiple values, then the
    escape_regex function will be applied to each individual value and
    return a multiple-valued result. For example, the string
    '(\\.test_string*)?' will evaluate to
    '\\(\\\\\\.test_string\\*\\)\\?'. The purpose for this is that many
    times, a component used in pattern match needs to be treated as a
    literal string and not a regular expression. For example, assume a
    basic component element that identifies a file path that is held in
    the Windows registry. This path is a string that might contain
    regular expression characters. These characters are likely not
    intended to be treated as regular expression characters and need to
    be escaped. This function allows a definition writer to mark convert
    the values of components to regular expression format. Note that
    when using regular expressions, OVAL supports a common subset of the
    regular expression character classes, operations, expressions and
    other lexical tokens defined within Perl 5's regular expression
    specification. The set of Perl metacharacters which must be escaped
    by this function is as follows, enclosed by single quotes:
    '^$\\.[](){}*+?|'. For more information on the supported regular
    expression syntax in OVAL see:
    http://oval.mitre.org/language/about/re_support_5.6.html.
    """

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
    escape_regex: Optional["EscapeRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )


@dataclass
class SplitFunctionType(FunctionType):
    """The split function takes a single string component and turns it into a
    collection of values based on a delimiter string.

    For example, assume that a basic component element returns the value
    "a-b-c-d" to the split function with the delimiter set to "-". The
    local_variable element would be evaluated to have four values "a",
    "b", "c", and "d". If the basic component returns a value that
    begins, or ends, with a delimiter, the local_variable element would
    contain empty string values at the beginning, or end, of the
    collection of values returned for that string component. For
    example, if the delimiter is "-", and the basic component element
    returns the value "-a-a-", the local_variable element would evaluate
    to a collection of four values "", "a", "a", and "". Likewise, if
    the basic component element returns a value that contains adjacent
    delimiters such as "---", the local_variable element would evaluate
    to a collection of four values "", "", "", and "". Lastly, if the
    basic component element used by the split function returnsa
    collection of values, then the split function is performed multiple
    times, and all of the results, from each of the split functions, are
    returned.
    """

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
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    delimiter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SubstringFunctionType(FunctionType):
    """The substring function takes a single string component and produces a single
    value that contains a portion of the original string.

    The substring_start attribute defines the starting position in the
    original string. To include the first character of the string, the
    start position would be 1. A value less than 1 also means that the
    start position would be 1. If the substring_start attribute has
    value greater than the length of the original string an error should
    be reported. The substring_length attribute defines how many
    characters after, and including, the starting character to include.
    A substring_length value greater than the actual length of the
    string, or a negative value, means to include all of the characters
    after the starting character. For example, assume a basic component
    element that returns the value "abcdefg" with a substring_start
    value of 3 and a substring_length value of 2. The local_variable
    element would evaluate to have a single value of "cd". If the string
    component used by the substring function returns a collection of
    values, then the substring operation is performed multiple times and
    results in a collection of values for the component.
    """

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
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    substring_start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    substring_length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TimeDifferenceFunctionType(FunctionType):
    """The time_difference function calculates the difference in seconds between
    date-time values.

    If one component is specified, the values of that component are subtracted from the current time (UTC). The current time is the time at which the function is evaluated. If two components are specified, the value of the second component is subtracted from the value of the first component. If the component(s) contain a collection of values, the operation is performed multiple times on the Cartesian product of the component(s) and the result is also a collection of time difference values. For example, assume a local_variable specifies the time_difference function and has two sub-components under this function: the first component returns "04/02/2009" and "04/03/2009", and the second component returns "02/02/2005" and "02/03/2005" and "02/04/2005". The local_variable element would evaluate to a collection of six values: (ToSeconds("04/02/2009") - ToSeconds("02/02/2005")), (ToSeconds("04/02/2009") - ToSeconds("02/03/2005")),
    (ToSeconds("04/02/2009") - ToSeconds("02/04/2005")), (ToSeconds("04/03/2009") - ToSeconds("02/02/2005")), (ToSeconds("04/03/2009") - ToSeconds("02/03/2005")), and (ToSeconds("04/03/2009") - ToSeconds("02/04/2005")).
    The date-time format of each component is determined by the two format attributes. The format1 attribute applies to the first component, and the format2 attribute applies to the second component. Valid values for the attributes are 'win_filetime', 'seconds_since_epoch', 'day_month_year', 'year_month_day', and 'month_day_year'. Please see the DateTimeFormatEnumeration for more information about each of these values. If an input value is not understood, the result is an error. If only one input is specified, specify the format with the format2 attribute, as the first input is considered to be the implied 'current time' input.
    Note that the datatype associated with the components should be 'string' or 'int' depending on which date time format is specified.  The result of this function though is always an integer.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    time_difference: list["TimeDifferenceFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    regex_capture: list["RegexCaptureFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    format_1: DateTimeFormatEnumeration = field(
        default=DateTimeFormatEnumeration.YEAR_MONTH_DAY,
        metadata={
            "type": "Attribute",
        },
    )
    format_2: DateTimeFormatEnumeration = field(
        default=DateTimeFormatEnumeration.YEAR_MONTH_DAY,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegexCaptureFunctionType(FunctionType):
    """The regex_capture function captures a single substring from a single string
    component.

    If the string sub-component contains multiple values, then the
    regex_capture function will extract a substring from each value. The
    'pattern' attribute provides a regular expression that should
    contain a single subexpression (using parentheses). For example, the
    pattern ^abc(.*)xyz$ would capture a substring from each of the
    string component's values if the value starts with abc and ends with
    xyz. In this case the subexpression would be all the characters that
    exist in between the abc and the xyz. Note that subexpressions match
    the longest possible substrings. If the regular expression contains
    multiple capturing sub-patterns, only the first capture is used. If
    there are no capturing sub-patterns, the result for each target
    string must be the empty string. Otherwise, if the regular
    expression could match the target string in more than one place,
    only the first match (and its first capture) is used. If no matches
    are found in a target string, the result for that target must be the
    empty string. Note that a quantified capturing sub-pattern does not
    produce multiple substrings. Standard regular expression semantics
    are such that if a capturing sub-pattern is required to match
    multiple times in order for the overall regular expression to match,
    the capture produced is the last substring to have matched the sub-
    pattern. Note that when using regular expressions, OVAL supports a
    common subset of the regular expression character classes,
    operations, expressions and other lexical tokens defined within Perl
    5's regular expression specification. If any of the Perl
    metacharacters are to be used literally, then they must be escaped.
    The set of metacharacters which must be escaped for this purpose is
    as follows, enclosed by single quotes: '^$\\.[](){}*+?|'. For more
    information on the supported regular expression syntax in OVAL see:
    http://oval.mitre.org/language/about/re_support_5.6.html.
    """

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
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UniqueFunctionType(FunctionType):
    """The unique function takes one or more components and removes any duplicate
    value from the set of components.

    All components used in the unique function will be treated as
    strings. For example, assume that three components exist, one that
    contains a string value of 'foo', and two of which both resolve to
    the string value 'bar'. Applying the unique function to these three
    components resolves to a local_variable with two string values,
    'foo' and 'bar'. Additionally, if any of the components referenced
    by the unique function evaluate to a collection of values, then
    those values are used in the unique calculation. For example, assume
    that there are two components, one of which resolves to a single
    string value, 'foo', the other of which resolves to two string
    values, 'foo' and 'bar'. If the unique function is used to remove
    duplicates from these two components, the function will resolve to a
    local_variable that is a collection of two string values, 'foo' and
    'bar'.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    time_difference: list[TimeDifferenceFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    regex_capture: list[RegexCaptureFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )


@dataclass
class CountFunctionType(FunctionType):
    """The count function takes one or more components and returns the count of all
    of the values represented by the components.

    For example, assume that two variables exist, each with a single
    value. By applying the count function against two variable
    components that resolve to the two variables, the resulting
    local_variable would have a value of '2'. Additionally, if any of
    the components referenced by the count function evaluate to a
    collection of values, then those values are used in the count
    calculation. For example, assume that there are two components, one
    of which resolves to a single value, the other of which resolves to
    two values. If the count function is used to provide a count of
    these two components, the function will resolve to a local_variable
    with the values '3'.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    time_difference: list[TimeDifferenceFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    regex_capture: list[RegexCaptureFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    unique: list[UniqueFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "sequence": 1,
        },
    )


@dataclass
class GlobToRegexFunctionType:
    """The glob_to_regex function takes a single string component representing
    shell glob pattern and produces a single value that corresponds to result of a
    conversion of the original glob pattern into Perl 5's regular expression
    pattern. The glob_noescape attribute defines the way how the backslash ('\\')
    character should be interpreted. It defaults to 'false' meaning backslash
    should be interpreted as an escape character (backslash is allowed to be used
    as an escape character). If the glob_noescape attribute would be set to 'true'
    it instructs the glob_to_regex function to interpret the backslash ('\\')
    character as a literal, rather than as an escape character (backslash is *not*
    allowed to be used as an escape character). Refer to table with examples below
    to see the difference how a different boolean value of the 'glob_noescape'
    attribute will impact the output form of the resulting Perl 5's regular
    expression produced by glob_to_regex function. Please note the glob_to_regex
    function will fail to perform the conversion and return an error when the
    provided string argument (to represent glob pattern) does not represent a
    syntactically correct glob pattern. For example given the 'a*b?[' as the
    argument to be converted, glob_to_regex would return an error since there's
    missing the corresponding closing bracket in the provided glob pattern
    argument.

    Also, it is necessary to mention that the glob_to_regex function respects the default behaviour for the input glob pattern and output Perl 5's regular expression spaces. Namely this means that:
    - glob_to_regex will respect the UNIX glob behavior when processing forward slashes, forward slash should be treated as a path separator and * or ? shall not match it,
    - glob_to_regex will rule out matches having special meaning (for example '.' as a representation of the current working directory or '..' as a representation of the parent directory of the current working directory,
    - glob_to_regex will rule out files or folders starting with '.' character (e.g. dotfiles) unless the respective glob pattern part itself starts with the '.' character,
    - glob_to_regex will not perform case-sensitivity transformation (alphabetical characters will be copied from input glob pattern space to output Perl 5's regular expression pattern space intact). It is kept as a responsibility of the OVAL content author to provide input glob pattern argument in such case so the resulting Perl 5's regular expression pattern will match the expected pathname entries according to the case of preference,
    - glob_to_regex will not perform any possible brace expansion. Therefore glob patterns like '{pat,pat,pat}' would be converted into Perl 5's regular expression syntax in the original un-expanded form (kept for any potential subsequent expansion to be performed by Perl 5's regular expression engine in the moment of the use of that resulting regular expression),
    - glob_to_regex will not perform tilde ('~') character substitution to user name home directory pathname. The ('~') character will be passed to Perl 5's regular expression engine intact. If user name home directory pathname glob pattern behaviour is expected, the pathname of the user name home directory needs to be specified in the original input glob pattern already,
    - glob_to_regex function will not perform any custom changes wrt to the ordering of items (perform any additional sorting of set of pathnames represented by the provided glob pattern argument).
    """

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
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    glob_noescape: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
