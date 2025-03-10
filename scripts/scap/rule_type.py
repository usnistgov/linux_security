from dataclasses import dataclass, field
from typing import Optional

from scap.check_type_2 import CheckType2
from scap.complex_check_type import ComplexCheckType
from scap.fix_text_type import FixTextType
from scap.fix_type import FixType
from scap.ident_type import IdentType
from scap.profile_note_type import ProfileNoteType
from scap.role_enum_type import RoleEnumType
from scap.selectable_item_type import SelectableItemType
from scap.severity_enum_type import SeverityEnumType
from scap.signature_type_2 import SignatureType2

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class RuleType(SelectableItemType):
    """
    Data type for the &lt;xccdf:Rule&gt; element that represents a specific
    &lt;xccdf:Benchmark&gt; test.

    :ivar ident: A globally meaningful identifier for this
        &lt;xccdf:Rule&gt;. This may be the name or identifier of a
        security configuration issue or vulnerability that the
        &lt;xccdf:Rule&gt; assesses.
    :ivar impact_metric: The potential impact of failure to conform to
        the &lt;xccdf:Rule&gt;, expressed as a CVSS 2.0 base vector.
    :ivar profile_note: Text that describes special aspects of the
        &lt;xccdf:Rule&gt; related to one or more &lt;xccdf:Profile&gt;
        elements. This allows an author to document things within
        &lt;xccdf:Rule&gt; elements that are specific to a given
        &lt;xccdf:Profile&gt;, and then select the appropriate text
        based on the selected &lt;xccdf:Profile&gt; and display it to
        the reader.
    :ivar fixtext: Data that describes how to bring a target system into
        compliance with this &lt;xccdf:Rule&gt;.
    :ivar fix: A command string, script, or other system modification
        statement that, if executed on the target system, can bring it
        into full, or at least better, compliance with this
        &lt;xccdf:Rule&gt;.
    :ivar check: The definition of, or a reference to, the target system
        check needed to test compliance with this &lt;xccdf:Rule&gt;.
        Sibling &lt;xccdf:check&gt; elements must have different values
        for the combination of their @selector and @system attributes,
        and must have different values for their @id attribute (if any).
    :ivar complex_check: A boolean expression composed of operators
        (and, or, not) and individual checks.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:Rule&gt;.
    :ivar id: Unique element identifier used by other elements to refer
        to this element.
    :ivar role: The &lt;xccdf:Rule&gt; element’s role in scoring and
        reporting.
    :ivar severity: Severity level code to be used for metrics and
        tracking.
    :ivar multiple: Applicable in cases where there are multiple
        instances of a target. For example, an &lt;xccdf:Rule&gt; may
        provide a recommendation about the configuration of application
        user accounts, but an application may have many user accounts.
        Each account would be considered an instance of the broader
        assessment target of user accounts. If the @multiple attribute
        is set to true, each instance of the target to which the
        &lt;xccdf:Rule&gt; can apply should be tested separately and the
        results should be recorded separately. If @multiple is set to
        false, the test results of such instances should be combined. If
        the checking system does not combine these results
        automatically, the results of each instance should be ANDed
        together to produce a single result. If the benchmark consumer
        cannot perform multiple instantiation, or if multiple
        instantiation of the &lt;xccdf:Rule&gt; is not applicable for
        the target system, then the benchmark consumer may ignore this
        attribute.
    """

    class Meta:
        name = "ruleType"

    ident: list[IdentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    impact_metric: Optional[str] = field(
        default=None,
        metadata={
            "name": "impact-metric",
            "type": "Element",
            
        },
    )
    profile_note: list[ProfileNoteType] = field(
        default_factory=list,
        metadata={
            "name": "profile-note",
            "type": "Element",
            
        },
    )
    fixtext: list[FixTextType] = field(
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
    signature: Optional[SignatureType2] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_rule_.+",
        },
    )
    role: RoleEnumType = field(
        default=RoleEnumType.FULL,
        metadata={
            "type": "Attribute",
        },
    )
    severity: SeverityEnumType = field(
        default=SeverityEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
    multiple: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
