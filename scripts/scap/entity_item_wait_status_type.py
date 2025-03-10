from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemWaitStatusType(Enum):
    """The EntityItemWaitStatusType complex type restricts a string value to two
    values, either wait or nowait, that specify whether the server that is invoked
    by inetd will take over the listening socket associated with the service, and
    whether once launched, inetd will wait for that server to exit, if ever, before
    it resumes listening for new service requests.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar WAIT: The value of 'wait' specifies that the server that is
        invoked by inetd will take over the listening socket associated
        with the service, and once launched, inetd will wait for that
        server to exit, if ever, before it resumes listening for new
        service requests.
    :cvar NOWAIT: The value of 'nowait' specifies that the server that
        is invoked by inetd will not wait for any existing server to
        finish before taking over the listening socket associated with
        the service.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    WAIT = "wait"
    NOWAIT = "nowait"
    VALUE = ""
