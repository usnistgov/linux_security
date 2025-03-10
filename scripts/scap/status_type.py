from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class StatusType(Enum):
    """
    The statusType represents the possible levels of maturity or consensus level
    for its parent element as recorded by an &lt;xccdf:status&gt; element.

    :cvar ACCEPTED: Released as final
    :cvar DEPRECATED: No longer needed
    :cvar DRAFT: Released in draft state
    :cvar INCOMPLETE: Under initial development
    :cvar INTERIM: Revised and in the process of being finalized
    """

    ACCEPTED = "accepted"
    DEPRECATED = "deprecated"
    DRAFT = "draft"
    INCOMPLETE = "incomplete"
    INTERIM = "interim"
