from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


class UserResponseType(Enum):
    """The UserResponseType type defines structures containing the type of
    response.

    The question could have been answered or an exceptional condition
    may have occurred.

    :cvar UNKNOWN: An UNKNOWN value indicates that the result of a test
        cannot be determined.
    :cvar ERROR: An ERROR value indicates that an error occured while
        processing the check. Among other causes, this can indicate an
        unexpected response.
    :cvar NOT_TESTED: A NOT_TESTED value indicates that the check has
        not been tested yet.
    :cvar NOT_APPLICABLE: A NOT_APPLICABLE value indicates that the
        check is not relevant and can be skipped.
    :cvar ANSWERED: Indicates that the question was answered.
    """

    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
    NOT_TESTED = "NOT_TESTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    ANSWERED = "ANSWERED"
