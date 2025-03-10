from dataclasses import dataclass, field
from typing import Optional

from scap.dc_status_type import DcStatusType
from scap.html_text_with_sub_type import HtmlTextWithSubType
from scap.metadata_type_2 import MetadataType2
from scap.overrideable_cpe2idref_type import OverrideableCpe2IdrefType
from scap.profile_refine_rule_type import ProfileRefineRuleType
from scap.profile_refine_value_type import ProfileRefineValueType
from scap.profile_select_type import ProfileSelectType
from scap.profile_set_complex_value_type import ProfileSetComplexValueType
from scap.profile_set_value_type import ProfileSetValueType
from scap.reference_type_4 import ReferenceType4
from scap.signature_type_2 import SignatureType2
from scap.status import Status
from scap.text_with_sub_type import TextWithSubType
from scap.version_type import VersionType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileType:
    """Data type for the &lt;xccdf:Profile&gt; element, which holds a specific
    tailoring of the &lt;xccdf:Benchmark&gt;.

    The main part of an &lt;xccdf:Profile&gt; is the selectors:
    &lt;xccdf:select&gt;, &lt;xccdf:set-value&gt;, &lt;xccdf:set-
    complex-value&gt;, &lt;xccdf:refine-rule&gt;, and &lt;xccdf:refine-
    value&gt;. An &lt;xccdf:Profile&gt; may also be signed with an XML-
    Signature.

    :ivar status: Status of the &lt;xccdf:Profile&gt; and date at which
        it attained that status. Authors may use this element to record
        the maturity or consensus level of an &lt;xccdf:Profile&gt;. If
        the &lt;xccdf:status&gt; is not given explicitly, then the
        &lt;xccdf:Profile&gt; is taken to have the same status as its
        parent &lt;xccdf:Benchmark&gt;.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar version: Version information about this &lt;xccdf:Profile&gt;.
    :ivar title: Title of the &lt;xccdf:Profile&gt;.
    :ivar description: Text that describes the &lt;xccdf:Profile&gt;.
    :ivar reference: A reference where the user can learn more about the
        subject of this &lt;xccdf:Profile&gt;.
    :ivar platform: A target platform for this &lt;xccdf:Profile&gt;.
    :ivar select: Select or deselect &lt;xccdf:Group&gt; and
        &lt;xccdf:Rule&gt; elements.
    :ivar set_complex_value: Set the value of an &lt;xccdf:Value&gt; to
        a list.
    :ivar set_value: Set the value of an &lt;xccdf:Value&gt; to a simple
        data value.
    :ivar refine_value: Customize the properties of an
        &lt;xccdf:Value&gt;.
    :ivar refine_rule: Customize the properties of an &lt;xccdf:Rule&gt;
        or &lt;xccdf:Group&gt;.
    :ivar metadata: Metadata associated with this &lt;xccdf:Profile&gt;.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:Profile&gt;.
    :ivar id: Unique identifier for this &lt;xccdf:Profile&gt;.
    :ivar prohibit_changes: Whether or not products should prohibit
        changes to this &lt;xccdf:Profile&gt;.
    :ivar abstract: If true, then this &lt;xccdf:Profile&gt; exists
        solely to be extended by other &lt;xccdf:Profile&gt; elements.
    :ivar note_tag: Tag identifier to specify which &lt;xccdf:profile-
        note&gt; element from an &lt;xccdf:Rule&gt; should be associated
        with this &lt;xccdf:Profile&gt;.
    :ivar extends: The id of an &lt;xccdf:Profile&gt; on which to base
        this &lt;xccdf:Profile&gt;.
    :ivar base:
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    """

    class Meta:
        name = "profileType"

    status: list[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        },
    )
    dc_status: list[DcStatusType] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
            
        },
    )
    version: Optional[VersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    title: list[TextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )
    description: list[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    reference: list[ReferenceType4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    platform: list[OverrideableCpe2IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    select: list[ProfileSelectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    set_complex_value: list[ProfileSetComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-complex-value",
            "type": "Element",
            
        },
    )
    set_value: list[ProfileSetValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-value",
            "type": "Element",
            
        },
    )
    refine_value: list[ProfileRefineValueType] = field(
        default_factory=list,
        metadata={
            "name": "refine-value",
            "type": "Element",
            
        },
    )
    refine_rule: list[ProfileRefineRuleType] = field(
        default_factory=list,
        metadata={
            "name": "refine-rule",
            "type": "Element",
            
        },
    )
    metadata: list[MetadataType2] = field(
        default_factory=list,
        metadata={
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
            "pattern": r"xccdf_[^_]+_profile_.+",
        },
    )
    prohibit_changes: bool = field(
        default=False,
        metadata={
            "name": "prohibitChanges",
            "type": "Attribute",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    note_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "note-tag",
            "type": "Attribute",
        },
    )
    extends: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
