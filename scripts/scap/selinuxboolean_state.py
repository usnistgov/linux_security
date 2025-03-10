from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_bool_type import EntityStateBoolType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class SelinuxbooleanState(StateType):
    """The selinuxboolean_state element defines the different information that can
    be used to evaluate the specified SELinux boolean.

    This includes SELinux boolean's current and pending status. Please
    refer to the individual elements in the schema for more details
    about what each represents.

    :ivar name: The name of the SELinux boolean.
    :ivar current_status: The current_status entity represents the
        current state of the specified SELinux boolean.
    :ivar pending_status: The pending_status entity represents the
        pending state of the specified SELinux boolean.
    """

    class Meta:
        name = "selinuxboolean_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    current_status: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pending_status: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
