from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class RoleEnumType(Enum):
    """
    Allowed checking and scoring roles for an &lt;xccdf:Rule&gt;.

    :cvar FULL: If the &lt;xccdf:Rule&gt; is selected, then check it and
        let the result contribute to the score and appear in reports
        (default).
    :cvar UNSCORED: If the &lt;xccdf:Rule&gt; is selected, then check it
        and include it in the test report, but give the result a status
        of informational and do not use the result in score
        computations.
    :cvar UNCHECKED: Do not check the &lt;xccdf:Rule&gt;; just force the
        result status to notchecked.
    """

    FULL = "full"
    UNSCORED = "unscored"
    UNCHECKED = "unchecked"
