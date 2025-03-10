from dataclasses import dataclass

from scap.variable_type_1 import VariableType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Variable1(VariableType1):
    """The variable element is an abstract element that is meant to be extended
    (via substitution groups) by the different types of variables.

    An actual variable element is not valid. The different variable
    types describe different sources for obtaining a value(s) for the
    variable. There are currently three types of variables; local,
    external, and constant. Please refer to the description of each one
    for more specific information. The value(s) of a variable is treated
    as if it were inserted where referenced. One of the main benefits of
    variables is that they allow tests to evaluate user-defined policy.
    For example, an OVAL Test might check to see if a password is at
    least a certain number of characters long, but this number depends
    upon the individual policy of the user. To solve this, the test for
    password length can be written to refer to a variable element that
    defines the length. If a variable defines a collection of values,
    any entity that references the variable will evaluate to true
    depending on the value of the var_check attribute. For example, if
    an entity 'size' with an operation of 'less than' references a
    variable that returns five different integers, and the var_check
    attribute has a value of 'all', then the 'size' entity returns true
    only if the actual size is less than each of the five integers
    defined by the variable. If a variable does not return any value,
    then an error should be reported during OVAL analysis.
    """

    class Meta:
        name = "variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"
