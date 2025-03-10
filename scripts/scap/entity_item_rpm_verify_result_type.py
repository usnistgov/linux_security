from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


class EntityItemRpmVerifyResultType(Enum):
    """The EntityItemRpmVerifyResultType complex type restricts a string value to
    the set of possible outcomes of checking an attribute of a file included in an
    RPM against the actual value of that attribute in the RPM database.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar PASS: 'pass' indicates that the test passed and is equivalent
        to the '.' value reported by the rpm -V command.
    :cvar FAIL: 'fail' indicates that the test failed and is equivalent
        to a bold charcter in the test result string reported by the rpm
        -V command.
    :cvar NOT_PERFORMED: 'not performed' indicates that the test could
        not be performed and is equivalent to the '?' value reported by
        the rpm -V command.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    PASS = "pass"
    FAIL = "fail"
    NOT_PERFORMED = "not performed"
    VALUE = ""
