from dataclasses import dataclass, field
from typing import Optional

from scap.fix_strategy_enum_type import FixStrategyEnumType
from scap.instance_fix_type import InstanceFixType
from scap.rating_enum_type import RatingEnumType
from scap.sub_type import SubType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class FixType:
    """Data type for the &lt;xccdf:fix&gt; element.

    The body of this element contains a command string, script, or other
    system modification statement that, if executed on the target
    system, can bring it into full, or at least better, compliance with
    this &lt;xccdf:Rule&gt;.

    :ivar id: A local identifier for the element. It is optional for the
        @id to be unique; multiple &lt;xccdf:fix&gt; elements may have
        the same @id but different values for their other attributes. It
        is used primarily to allow &lt;xccdf:fixtext&gt; elements to be
        associated with one or more &lt;xccdf:fix&gt; elements
    :ivar reboot: True if a reboot is known to be required and false
        otherwise.
    :ivar strategy: The method or approach for making the described fix.
    :ivar disruption: An estimate of the potential for disruption or
        operational degradation that the application of this fix will
        impose on the target.
    :ivar complexity: The estimated complexity or difficulty of applying
        the fix to the target.
    :ivar system: A URI that identifies the scheme, language, engine, or
        process for which the fix contents are written. Table 17 in the
        XCCDF specification defines several general-purpose URNs that
        may be used for this, and tool vendors and system providers may
        define and use target-specific URNs.
    :ivar platform: In case different fix scripts or procedures are
        required for different target platform types (e.g., different
        patches for Windows Vista and Windows 7), this attribute allows
        a CPE name or CPE applicability language expression to be
        associated with an &lt;xccdf:fix&gt; element. This should appear
        on an &lt;xccdf:fix&gt; when the content applies to only one
        platform out of several to which the &lt;xccdf:Rule&gt; could
        apply.
    :ivar content:
    """

    class Meta:
        name = "fixType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reboot: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    strategy: FixStrategyEnumType = field(
        default=FixStrategyEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
    disruption: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
    complexity: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": SubType,
                    
                },
                {
                    "name": "instance",
                    "type": InstanceFixType,
                    
                },
            ),
        },
    )
