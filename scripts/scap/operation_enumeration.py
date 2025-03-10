from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class OperationEnumeration(Enum):
    """The OperationEnumeration simple type defines acceptable operations.

    Each operation defines how to compare entities against their actual
    values.

    :cvar EQUALS: The 'equals' operation returns true if the actual
        value on the system is equal to the stated entity.  When the
        specified datatype is a string, this results in a case-sensitive
        comparison.
    :cvar NOT_EQUAL: The 'not equal' operation returns true if the
        actual value on the system is not equal to the stated entity.
        When the specified datatype is a string, this results in a case-
        sensitive comparison.
    :cvar CASE_INSENSITIVE_EQUALS: The 'case insensitive equals'
        operation is meant for string data and returns true if the
        actual value on the system is equal (using a case insensitive
        comparison) to the stated entity.
    :cvar CASE_INSENSITIVE_NOT_EQUAL: The 'case insensitive not equal'
        operation is meant for string data and returns true if the
        actual value on the system is not equal (using a case
        insensitive comparison) to the stated entity.
    :cvar GREATER_THAN: The 'greater than' operation returns true if the
        actual value on the system is greater than the stated entity.
    :cvar LESS_THAN: The 'less than' operation returns true if the
        actual value on the system is less than the stated entity.
    :cvar GREATER_THAN_OR_EQUAL: The 'greater than or equal' operation
        returns true if the actual value on the system is greater than
        or equal to the stated entity.
    :cvar LESS_THAN_OR_EQUAL: The 'less than or equal' operation returns
        true if the actual value on the system is less than or equal to
        the stated entity.
    :cvar BITWISE_AND: The 'bitwise and' operation is used to determine
        if a specific bit is set. It returns true if performing a
        BITWISE AND with the binary representation of the stated entity
        against the binary representation of the actual value on the
        system results in a binary value that is equal to the binary
        representation of the stated entity. For example, assuming a
        datatype of 'int', if the actual integer value of the setting on
        your machine is 6 (same as 0110 in binary), then performing a
        'bitwise and' with the stated integer 4 (0100) returns 4 (0100).
        Since the result is the same as the state mask, then the test
        returns true. If the actual value on your machine is 1 (0001),
        then the 'bitwise and' with the stated integer 4 (0100) returns
        0 (0000). Since the result is not the same as the stated mask,
        then the test fails.
    :cvar BITWISE_OR: The 'bitwise or' operation is used to determine if
        a specific bit is not set. It returns true if performing a
        BITWISE OR with the binary representation of the stated entity
        against the binary representation of the actual value on the
        system results in a binary value that is equal to the binary
        representation of the stated entity. For example, assuming a
        datatype of 'int', if the actual integer value of the setting on
        your machine is 6 (same as 0110 in binary), then performing a
        'bitwise or' with the stated integer 14 (1110) returns 14
        (1110). Since the result is the same as the state mask, then the
        test returns true. If the actual value on your machine is 1
        (0001), then the 'bitwise or' with the stated integer 14 (1110)
        returns 15 (1111). Since the result is not the same as the
        stated mask, then the test fails.
    :cvar PATTERN_MATCH: The 'pattern match' operation allows an item to
        be tested against a regular expression. When used by an entity
        in an OVAL Object, the regular expression represents the unique
        set of matching items on the system.  OVAL supports a common
        subset of the regular expression character classes, operations,
        expressions and other lexical tokens defined within Perl 5's
        regular expression specification. For more information on the
        supported regular expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html
    :cvar SUBSET_OF: The 'subset of' operation returns true if the
        actual set on the system is a subset of the set defined by the
        stated entity.
    :cvar SUPERSET_OF: The 'superset of' operation returns true if the
        actual set on the system is a superset of the set defined by the
        stated entity.
    """

    EQUALS = "equals"
    NOT_EQUAL = "not equal"
    CASE_INSENSITIVE_EQUALS = "case insensitive equals"
    CASE_INSENSITIVE_NOT_EQUAL = "case insensitive not equal"
    GREATER_THAN = "greater than"
    LESS_THAN = "less than"
    GREATER_THAN_OR_EQUAL = "greater than or equal"
    LESS_THAN_OR_EQUAL = "less than or equal"
    BITWISE_AND = "bitwise and"
    BITWISE_OR = "bitwise or"
    PATTERN_MATCH = "pattern match"
    SUBSET_OF = "subset of"
    SUPERSET_OF = "superset of"
