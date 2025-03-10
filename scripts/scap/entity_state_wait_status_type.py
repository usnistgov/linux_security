from dataclasses import dataclass

from scap.entity_state_string_type import EntityStateStringType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class EntityStateWaitStatusType(EntityStateStringType):
    """The EntityStateWaitStatusType complex type restricts a string value to two
    values, either wait or nowait, that specify whether the server that is invoked
    by inetd will take over the listening socket associated with the service, and
    whether once launched, inetd will wait for that server to exit, if ever, before
    it resumes listening for new service requests.

    The empty string is also allowed to support empty elements
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """
