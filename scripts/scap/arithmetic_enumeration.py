from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


class ArithmeticEnumeration(Enum):
    """The ArithmeticEnumeration simple type defines basic arithmetic operations.

    Currently add and multiply are defined.
    """

    ADD = "add"
    MULTIPLY = "multiply"
