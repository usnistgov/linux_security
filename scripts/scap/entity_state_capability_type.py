from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class EntityStateCapabilityType(EntityStateStringType):
    """The EntityStateCapabilityType complex type restricts a string value to a
    specific set of values that describe POSIX capability types associated with a
    process service.

    This list is based off the values defined in
    linux/include/linux/capability.h. Documentation on each allowed
    value can be found in capability.h. The empty string is also allowed
    to support empty elements associated with variable references. Note
    that when using pattern matches and variables care must be taken to
    ensure that the regular expression and variable values align with
    the enumerated values.
    """
