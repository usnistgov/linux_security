from dataclasses import dataclass, field
from typing import Optional

from scap.operator_enumeration_1 import OperatorEnumeration1
from scap.restriction_type import RestrictionType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class PossibleRestrictionType:
    """The PossibleRestrictionType complex type outlines a range of possible
    expected value of an external variable.

    Each possible_restriction element contains an unbounded list of
    child restriction elements that each specify a range that an actual
    value may fall in. For example, a restriction element may specify
    that a value must be less than 10. When multiple restriction
    elements are present, a valid possible value's evaluation is based
    on the operator attribute. The operator attribute is set to AND by
    default. Other valid operation values are explained in the
    description of the OperatorEnumeration simple type. One can think of
    the possible_value and possible_restriction elements as an OR'd list
    of possible values, with the restriction elements as using the
    selected operation to evaluate its own list of value descriptions.
    Please refer to the description of the RestrictionType complex type
    for more information. The required hint attribute gives a short
    description of what the value means or represents.
    """

    restriction: list[RestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )
    operator: OperatorEnumeration1 = field(
        default=OperatorEnumeration1.AND,
        metadata={
            "type": "Attribute",
        },
    )
    hint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
