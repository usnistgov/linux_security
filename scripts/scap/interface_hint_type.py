from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class InterfaceHintType(Enum):
    """Allowed interface hint values.

    &lt;xccdf:Value&gt; elements may contain a hint or recommendation to
    a benchmark consumer or producer about how the user might select or
    adjust the &lt;xccdf:Value&gt;. This type enumerates the possible
    values of this hint.

    :cvar CHOICE: Multiple choice
    :cvar TEXTLINE: Multiple lines of text
    :cvar TEXT: Single line of text
    :cvar DATE: Date
    :cvar DATETIME: Date and time
    """

    CHOICE = "choice"
    TEXTLINE = "textline"
    TEXT = "text"
    DATE = "date"
    DATETIME = "datetime"
