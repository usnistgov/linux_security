from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class EntityStateHashTypeType(EntityStateStringType):
    """The EntityStateHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """
