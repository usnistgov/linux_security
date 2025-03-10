from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityStateFamilyType(EntityStateStringType):
    """The EntityStateFamilyType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a high-level family of system operating
    system. The empty string is also allowed to support empty elements
    associated with variable references.
    """
