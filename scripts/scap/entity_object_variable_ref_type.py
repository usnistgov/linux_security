from dataclasses import dataclass

from scap.entity_object_string_type import EntityObjectStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityObjectVariableRefType(EntityObjectStringType):
    """The EntityObjectVariableRefType complex type defines a string object entity
    that has a valid OVAL variable id as the value.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """
