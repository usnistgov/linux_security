from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityStateLdaptypeType(EntityStateStringType):
    """The EntityStateLdaptypeType complex type restricts a string value to a
    specific set of values that specify the different types of information that an
    ldap attribute can represent.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """
