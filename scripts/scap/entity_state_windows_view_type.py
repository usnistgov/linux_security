from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityStateWindowsViewType(EntityStateStringType):
    """The EntityStateWindowsViewType restricts a string value to a specific set of values: 32-bit and 64-bit. These values describe the different values possible for the windows view behavior."""
