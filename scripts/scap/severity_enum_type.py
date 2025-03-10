from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class SeverityEnumType(Enum):
    """Allowed severity values for the @severity attribute of an
    &lt;xccdf:Rule&gt;.

    The value of this attribute provides an indication of the importance
    of the &lt;xccdf:Rule&gt; element's recommendation. This information
    is informative only and does not affect scoring.

    :cvar UNKNOWN: Severity not defined (default).
    :cvar INFO: &lt;xccdf:Rule&gt; is informational and failure does not
        represent a problem.
    :cvar LOW: Not a serious problem.
    :cvar MEDIUM: Fairly serious problem.
    :cvar HIGH: A grave or critical problem.
    """

    UNKNOWN = "unknown"
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
