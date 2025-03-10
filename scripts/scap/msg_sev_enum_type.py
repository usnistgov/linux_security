from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class MsgSevEnumType(Enum):
    """Allowed values to indicate the severity of messages from the checking
    engine.

    These values don't affect scoring themselves but are present merely
    to convey diagnostic information from the checking engine. Benchmark
    consumers may choose to log these messages or display them to the
    user.

    :cvar ERROR: Denotes a serious problem identified; test did not run.
    :cvar WARNING: Denotes a possible issue; test may not have run.
    :cvar INFO: Denotes important information about the tests.
    """

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
