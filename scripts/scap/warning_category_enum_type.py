from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class WarningCategoryEnumType(Enum):
    """
    Allowed warning category keywords for the &lt;xccdf:warning&gt; element used in
    &lt;xccdf:Rule&gt; elements.

    :cvar GENERAL: Broad or general-purpose warning (default)
    :cvar FUNCTIONALITY: Warning about possible impacts to functionality
        or operational features
    :cvar PERFORMANCE: Warning about changes to target system
        performance or throughput
    :cvar HARDWARE: Warning about hardware restrictions or possible
        impacts to hardware
    :cvar LEGAL: Warning about legal implications
    :cvar REGULATORY: Warning about regulatory obligations or compliance
        implications
    :cvar MANAGEMENT: Warning about impacts to the management or
        administration of the target system
    :cvar AUDIT: Warning about impacts to audit or logging
    :cvar DEPENDENCY: Warning about dependencies between this element
        and other parts of the target system, or version dependencies
    """

    GENERAL = "general"
    FUNCTIONALITY = "functionality"
    PERFORMANCE = "performance"
    HARDWARE = "hardware"
    LEGAL = "legal"
    REGULATORY = "regulatory"
    MANAGEMENT = "management"
    AUDIT = "audit"
    DEPENDENCY = "dependency"
