from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_bool_type import EntityStateBoolType
from scap.entity_state_gconf_type_type import EntityStateGconfTypeType
from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class GconfState(StateType):
    """The gconf_state element defines the different information that can be used
    to evaluate the specified GConf preference key.

    This includes the preference key, source, type, whether it's
    writable, the user who last modified it, the time it was last
    modified, whether it's the default value, as well as the preference
    key's value. Please refer to the individual elements in the schema
    for more details about what each represents.

    :ivar key: The preference key to check.
    :ivar source: The source used to look up the preference key.
    :ivar type_value: The type of the preference key.
    :ivar is_writable: Is the preference key writable? If true, the
        preference key is writable. If false, the preference key is not
        writable.
    :ivar mod_user: The user who last modified the preference key.
    :ivar mod_time: The time the preference key was last modified in
        seconds since the Unix epoch. The Unix epoch is the time
        00:00:00 UTC on January 1, 1970.
    :ivar is_default: Is the preference key value the default value. If
        true, the preference key value is the default value. If false,
        the preference key value is not the default value.
    :ivar value: The value of the preference key.
    """

    class Meta:
        name = "gconf_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    source: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[EntityStateGconfTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    is_writable: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    mod_user: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    mod_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    is_default: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
