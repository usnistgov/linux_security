from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class MessageLevelEnumeration(Enum):
    """The MessageLevelEnumeration simple type defines the different levels
    associated with a message.

    There is no specific criteria about which messages get assigned
    which level. This is completely arbitrary and up to the content
    producer to decide what is an error message and what is a debug
    message.

    :cvar DEBUG: Debug messages should only be displayed by a tool when
        run in some sort of verbose mode.
    :cvar ERROR: Error messages should be recorded when there was an
        error that did not allow the collection of specific data.
    :cvar FATAL: A fatal message should be recorded when an error causes
        the failure of more than just a single piece of data.
    :cvar INFO: Info messages are used to pass useful information about
        the data collection to a user.
    :cvar WARNING: A warning message reports something that might not
        correct but information was still collected.
    """

    DEBUG = "debug"
    ERROR = "error"
    FATAL = "fatal"
    INFO = "info"
    WARNING = "warning"
