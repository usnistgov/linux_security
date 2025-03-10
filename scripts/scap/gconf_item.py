from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_gconf_type_type import EntityItemGconfTypeType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class GconfItem:
    """The gconf_item holds information about an individual GConf preference key
    found on a system.

    Each gconf_item contains a preference key, source, type, whether
    it's writable, the user who last modified it, the time it was last
    modified, whether it's the default value, as well as the preference
    key's value. It extends the standard ItemType as defined in the
    oval-system-characteristics schema and one should refer to the
    ItemType description for more information.

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
        name = "gconf_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    type_value: Optional[EntityItemGconfTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    is_writable: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    mod_user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    mod_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    is_default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
