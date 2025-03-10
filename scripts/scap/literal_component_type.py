from dataclasses import dataclass, field
from typing import Optional

from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class LiteralComponentType:
    """The LiteralComponentType complex type defines a literal value to be used as
    a component.

    The optional datatype attribute defines the type of data expected.
    The default datatype is 'string'.
    """

    value: Optional[object] = field(default=None)
    datatype: SimpleDatatypeEnumeration = field(
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )
