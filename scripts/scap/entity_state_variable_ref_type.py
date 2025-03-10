from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityStateVariableRefType(EntityStateStringType):
    """The EntityStateVariableRefType complex type defines a string state entity
    that has a valid OVAL variable id as the value.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """
