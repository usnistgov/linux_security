from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class RatingEnumType(Enum):
    """
    This type enumerates allowed rating values the disruption and complexity
    properties of an &lt;xccdf:Rule&gt; element's &lt;xccdf:fix&gt; or
    &lt;xccdf:fixtext&gt; elements.

    :cvar UNKNOWN: Rating unknown or impossible to estimate (default)
    :cvar LOW: Little or no potential for disruption, very modest
        complexity
    :cvar MEDIUM: Some chance of minor disruption, substantial
        complexity
    :cvar HIGH: Likely to cause serious disruption, very complex
    """

    UNKNOWN = "unknown"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
