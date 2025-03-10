from enum import Enum

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


class OperatorEnumeration2(Enum):
    """The OperatorEnumeration simple type defines acceptable operators.

    Each operator defines how to evaluate multiple arguments.
    """

    AND = "AND"
    OR = "OR"
