from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class FixStrategyEnumType(Enum):
    """Allowed @strategy keyword values for an &lt;xccdf:Rule&gt; element's
    &lt;xccdf:fix&gt; or &lt;xccdf:fixtext&gt; elements.

    The values indicate the method or approach for fixing non-compliance
    with a particular &lt;xccdf:Rule&gt;.

    :cvar UNKNOWN: Strategy not defined (default)
    :cvar CONFIGURE: Adjust target configuration/settings
    :cvar COMBINATION: Combination of two or more approaches
    :cvar DISABLE: Turn off or uninstall a target component
    :cvar ENABLE: Turn on or install a target component
    :cvar PATCH: Apply a patch, hotfix, update, etc.
    :cvar POLICY: Remediation requires out-of-band adjustments to
        policies or procedures
    :cvar RESTRICT: Adjust permissions, access rights, filters, or other
        access restrictions
    :cvar UPDATE: Install, upgrade or update the system
    """

    UNKNOWN = "unknown"
    CONFIGURE = "configure"
    COMBINATION = "combination"
    DISABLE = "disable"
    ENABLE = "enable"
    PATCH = "patch"
    POLICY = "policy"
    RESTRICT = "restrict"
    UPDATE = "update"
