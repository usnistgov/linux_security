from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


class VariableDataType(Enum):
    """
    The VariableDataType simple type defines how a variable data value should be
    treated or used.

    :cvar TEXT: The TEXT value specifies that the variable data value
        should be treated as text.
    :cvar NUMERIC: The NUMERIC value specifies that the variable data
        value should be treated as numeric.
    """

    TEXT = "TEXT"
    NUMERIC = "NUMERIC"
