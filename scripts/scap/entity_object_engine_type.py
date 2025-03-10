from dataclasses import dataclass

from scap.entity_object_string_type import EntityObjectStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityObjectEngineType(EntityObjectStringType):
    """The EntityObjectEngineType complex type defines a string entity value that
    is restricted to a set of enumerations.

    Each valid enumeration is a valid database engine. The empty string
    is also allowed to support empty elements associated with variable
    references.
    """
