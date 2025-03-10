from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class IdentityType:
    """Type for an &lt;xccdf:identity&gt; element in an &lt;xccdf:TestResult&gt;.

    It contains information about the system identity or user employed
    during application of the &lt;xccdf:Benchmark&gt;. If used, shall
    specify the name of the authenticated identity.

    :ivar value:
    :ivar authenticated: Whether the identity was authenticated with the
        target system during the application of the
        &lt;xccdf:Benchmark&gt;.
    :ivar privileged: Whether the identity was granted administrative or
        other special privileges beyond those of a normal user.
    """

    class Meta:
        name = "identityType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    authenticated: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    privileged: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
