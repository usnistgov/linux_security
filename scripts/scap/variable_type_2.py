from dataclasses import dataclass, field
from typing import Optional

from scap.item_base_type import ItemBaseType
from scap.text_type_3 import TextType3
from scap.variable_data_type import VariableDataType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class VariableType2(ItemBaseType):
    """
    The VariableType type defines structures used to hold a single value.

    :ivar description: The description element holds information that
        describes the value stored on the variable.
    :ivar id: Each item is required to have a unique identifier that
        conforms to the definition of NCName in the Recommendation
        "Namespaces in XML 1.0", i.e., all XML 1.0 names that do not
        contain colons.
    :ivar datatype: The datatype attribute specifies how to treat the
        variable's value. It can be TEXT or NUMERIC.
    """

    class Meta:
        name = "VariableType"

    description: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        },
    )
    datatype: Optional[VariableDataType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
