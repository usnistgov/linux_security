from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityStateEngineType(EntityStateStringType):
    """The EntityStateEngineType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a valid database engine. The empty string
    is also allowed to support empty elements associated with variable
    references.
    """
