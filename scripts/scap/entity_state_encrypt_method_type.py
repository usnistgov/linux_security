from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class EntityStateEncryptMethodType(EntityStateStringType):
    """The EntityStateEncryptMethodType complex type restricts a string value to a
    set that corresponds to the allowed encrypt methods used for protected
    passwords in a shadow file.

    The empty string is also allowed to support empty element associated
    with variable references.  Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.
    """
