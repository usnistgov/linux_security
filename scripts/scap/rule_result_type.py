from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.check_type_2 import CheckType2
from scap.complex_check_type import ComplexCheckType
from scap.fix_type import FixType
from scap.ident_type import IdentType
from scap.instance_result_type import InstanceResultType
from scap.message_type_2 import MessageType2
from scap.metadata_type_2 import MetadataType2
from scap.override_type import OverrideType
from scap.result_enum_type import ResultEnumType
from scap.role_enum_type import RoleEnumType
from scap.severity_enum_type import SeverityEnumType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class RuleResultType:
    """Type for the &lt;xccdf:rule-result&gt; element within an
    &lt;xccdf:TestResult&gt;.

    An &lt;xccdf:rule-result&gt; holds the result of applying an
    &lt;xccdf:Rule&gt; from the &lt;xccdf:Benchmark&gt; to a target
    system or component of a target system.

    :ivar result: Result of applying the referenced &lt;xccdf:Rule&gt;
        to a target or target component. (E.g., Pass, Fail, etc.)
    :ivar override: An XML block explaining how and why an auditor chose
        to override the result.
    :ivar ident: A long-term globally meaningful identifier for the
        issue, vulnerability, platform, etc. copied from the referenced
        &lt;xccdf:Rule&gt;.
    :ivar metadata: XML metadata associated with this &lt;xccdf:rule-
        result&gt;.
    :ivar message: Diagnostic messages from the checking engine. These
        elements do not affect scoring; they are present merely to
        convey diagnostic information from the checking engine.
    :ivar instance: Name of the target subsystem or component to which
        this result applies, for a multiply instantiated
        &lt;xccdf:Rule&gt;. The element is important for an
        &lt;xccdf:Rule&gt; that applies to components of the target
        system, especially when a target might have several such
        components, and where the @multiple attribute of the
        &lt;xccdf:Rule&gt; is set to true.
    :ivar fix: Fix script for this target platform, if available (would
        normally appear only for result values of “fail”). It is assumed
        to have been ‘instantiated’ by the testing tool and any
        substitutions or platform selections already made.
    :ivar check: Encapsulated or referenced results to detailed testing
        output from the checking engine (if any).
    :ivar complex_check: A copy of the &lt;xccdf:Rule&gt; element’s
        &lt;xccdf:complex-check&gt; element where each component
        &lt;xccdf:check&gt; element of the &lt;xccdf:complex-check&gt;
        element is an encapsulated or referenced results to detailed
        testing output from the checking engine (if any) as described in
        the &lt;xccdf:rule-result&gt; &lt;xccdf:check&gt; property.
    :ivar idref: The value of the @id property of an &lt;xccdf:Rule&gt;.
        This &lt;xccdf:rule-result&gt; reflects the result of applying
        this &lt;xccdf:Rule&gt; to a target or target component.
    :ivar role: The value of the @role property of the referenced
        &lt;xccdf:Rule&gt;.
    :ivar severity: The value of the @severity property of the
        referenced &lt;xccdf:Rule&gt;.
    :ivar time: Time when application of this instance of the referenced
        &lt;xccdf:Rule&gt; was completed.
    :ivar version: The value of the @version property of the referenced
        &lt;xccdf:Rule&gt;.
    :ivar weight: The value of the @weight property of the referenced
        &lt;xccdf:Rule&gt;.
    """

    class Meta:
        name = "ruleResultType"

    result: Optional[ResultEnumType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    override: list[OverrideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    ident: list[IdentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    metadata: list[MetadataType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    message: list[MessageType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    instance: list[InstanceResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    fix: list[FixType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    check: list[CheckType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    complex_check: Optional[ComplexCheckType] = field(
        default=None,
        metadata={
            "name": "complex-check",
            "type": "Element",
            
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    role: Optional[RoleEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    severity: Optional[SeverityEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "total_digits": 3,
        },
    )
