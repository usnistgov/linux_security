from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_family_type import EntityStateFamilyType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class FamilyState(StateType):
    """The family_state element contains a single entity that is used to check the
    family associated with the system.

    The family is a high-level classification of system types.

    :ivar family: This element describes the high-level system OS type
        to test against. Please refer to the definition of the
        EntityFamilyType for more information about the possible
        values..
    """

    class Meta:
        name = "family_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    family: Optional[EntityStateFamilyType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
