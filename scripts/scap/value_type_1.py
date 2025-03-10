from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ValueType1:
    """The ValueType complex type holds the actual value of the variable when
    dealing with a constant variable.

    This value should be used by all tests that reference this variable.
    The value cannot be over-ridden by an external source.
    """

    class Meta:
        name = "ValueType"

    value: Optional[object] = field(default=None)
