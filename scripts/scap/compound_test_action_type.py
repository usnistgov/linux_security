from dataclasses import dataclass, field
from typing import Optional

from scap.item_base_type import ItemBaseType
from scap.operation_type import OperationType
from scap.references_type_2 import ReferencesType2
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class CompoundTestActionType(ItemBaseType):
    """
    The CompoundTestActionType type describes the structures used to combine
    multiple test_action elements into a single result.

    :ivar title: The title element contains a descriptive heading for
        the set of test_actions.
    :ivar description: The description element holds information
        describing the set of test_actions.
    :ivar references: The references element holds one or more reference
        elements. Examples could include references to other standards,
        including but not limited to CVE, CCE, or CPE.
    :ivar actions: The actions element holds one or more test_action
        elements along with the operators used to combine them into a
        single result.
    """

    title: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    description: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    references: Optional[ReferencesType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    actions: Optional[OperationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
