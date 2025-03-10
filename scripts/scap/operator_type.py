from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


class OperatorType(Enum):
    """
    The OperatorType simple type provides a list of possible operator values that
    operate on a set of test_action elements.

    :cvar AND: The AND operator produces a true result if every argument
        is true. If one or more arguments are false, the result of the
        AND is false. See the truth table provided in the ResultType
        type for a complete list of how the various result types are
        combined by an AND operation.
    :cvar OR: The OR operator produces a true result if one or more
        arguments is true. If every argument is false, the result of the
        OR is false. See the truth table provided in the ResultType type
        for a complete list of how the various result types are combined
        by an OR operation.
    """

    AND = "AND"
    OR = "OR"
