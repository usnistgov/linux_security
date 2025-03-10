from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class OperatorEnumeration1(Enum):
    """The OperatorEnumeration simple type defines acceptable operators.

    Each operator defines how to evaluate multiple arguments.

    :cvar AND: The AND operator produces a true result if every argument
        is true. If one or more arguments are false, the result of the
        AND is false. If one or more of the arguments are unknown, and
        if none of the arguments are false, then the AND operator
        produces a result of unknown.
    :cvar ONE: The ONE operator produces a true result if one and only
        one argument is true. If there are more than argument is true
        (or if there are no true arguments), the result of the ONE is
        false. If one or more of the arguments are unknown, then the ONE
        operator produces a result of unknown.
    :cvar OR: The OR operator produces a true result if one or more
        arguments is true. If every argument is false, the result of the
        OR is false. If one or more of the arguments are unknown and if
        none of arguments are true, then the OR operator produces a
        result of unknown.
    :cvar XOR: XOR is defined to be true if an odd number of its
        arguments are true, and false otherwise. If any of the arguments
        are unknown, then the XOR operator produces a result of unknown.
    """

    AND = "AND"
    ONE = "ONE"
    OR = "OR"
    XOR = "XOR"
