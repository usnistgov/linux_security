from dataclasses import dataclass, field
from typing import Optional, Union

from scap.cpe2idref_type import Cpe2IdrefType
from scap.dc_status_type import DcStatusType
from scap.group_type import Group
from scap.html_text_with_sub_type import HtmlTextWithSubType
from scap.lang_value import LangValue
from scap.metadata_type_2 import MetadataType2
from scap.model import Model
from scap.notice_type import NoticeType
from scap.plain_text_type import PlainTextType
from scap.platform_specification import PlatformSpecification
from scap.profile import Profile
from scap.reference_type_4 import ReferenceType4
from scap.rule import Rule
from scap.signature_type_2 import SignatureType2
from scap.status import Status
from scap.test_result import TestResult
from scap.text_type_4 import TextType4
from scap.value import Value
from scap.version_type import VersionType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Benchmark:
    """This is the root element of the XCCDF document; it must appear exactly once.

    It encloses the entire benchmark, and contains both descriptive
    information and structural information. Note that the order of
    &lt;xccdf:Group&gt; and &lt;xccdf:Rule&gt; child elements may matter
    for the appearance of a generated document. &lt;xccdf:Group&gt; and
    &lt;xccdf:Rule&gt; children may be freely intermingled, but they
    must appear after any &lt;xccdf:Value&gt; children. All the other
    children must appear in the order shown.

    :ivar status: Status of the &lt;xccdf:Benchmark&gt; indicating its
        level of maturity or consensus. If more than one
        &lt;xccdf:status&gt; element appears, the element's @date
        attribute should be included.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar title: Title of the &lt;xccdf:Benchmark&gt;; an
        &lt;xccdf:Benchmark&gt; should have an &lt;xccdf:title&gt;.
    :ivar description: Text that describes the &lt;xccdf:Benchmark&gt;;
        an &lt;xccdf:Benchmark&gt; should have an
        &lt;xccdf:description&gt;.
    :ivar notice: Legal notices (licensing information, terms of use,
        etc.), copyright statements, warnings, and other advisory
        notices about this &lt;xccdf:Benchmark&gt; and its use.
    :ivar front_matter: Introductory matter for the beginning of the
        &lt;xccdf:Benchmark&gt; document; intended for use during
        Document Generation.
    :ivar rear_matter: Concluding material for the end of the
        &lt;xccdf:Benchmark&gt; document; intended for use during
        Document Generation.
    :ivar reference: Supporting references for the
        &lt;xccdf:Benchmark&gt; document.
    :ivar plain_text: Definitions for reusable text blocks, each with a
        unique identifier.
    :ivar platform_specification: A list of identifiers for complex
        platform definitions, written in CPE applicability language
        format. Authors may define complex platforms within this
        element, and then use their locally unique identifiers anywhere
        in the &lt;xccdf:Benchmark&gt; element in place of a CPE name.
    :ivar platform: Applicable platforms for this
        &lt;xccdf:Benchmark&gt;. Authors should use the element to
        identify the systems or products to which the
        &lt;xccdf:Benchmark&gt; applies.
    :ivar version: Version number of the &lt;xccdf:Benchmark&gt;.
    :ivar metadata: XML metadata for the &lt;xccdf:Benchmark&gt;.
        Metadata allows many additional pieces of information, including
        authorship, publisher, support, and other similar details, to be
        embedded in an &lt;xccdf:Benchmark&gt;.
    :ivar model: URIs of suggested scoring models to be used when
        computing a score for this &lt;xccdf:Benchmark&gt;. A suggested
        list of scoring models and their URIs is provided in the XCCDF
        specification.
    :ivar profile: &lt;xccdf:Profile&gt; elements that reference and
        customize sets of items in the &lt;xccdf:Benchmark&gt;.
    :ivar value: Parameter &lt;xccdf:Value&gt; elements that support
        &lt;xccdf:Rule&gt; elements and descriptions in the
        &lt;xccdf:Benchmark&gt;.
    :ivar group: &lt;xccdf:Group&gt; elements that comprise the
        &lt;xccdf:Benchmark&gt;; each may contain additional
        &lt;xccdf:Value&gt;, &lt;xccdf:Rule&gt;, and other
        &lt;xccdf:Group&gt; elements.
    :ivar rule: &lt;xccdf:Rule&gt; elements that comprise the
        &lt;xccdf:Benchmark&gt;.
    :ivar test_result: &lt;xccdf:Benchmark&gt; test result records (one
        per &lt;xccdf:Benchmark&gt; run).
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:Benchmark&gt;.
    :ivar id: Unique &lt;xccdf:Benchmark&gt; identifier.
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    :ivar resolved: True if &lt;xccdf:Benchmark&gt; has already
        undergone the resolution process.
    :ivar style: Name of an &lt;xccdf:Benchmark&gt; authoring style or
        set of conventions or constraints to which this
        &lt;xccdf:Benchmark&gt; conforms (e.g., “SCAP 1.2”).
    :ivar style_href: URL of a supplementary stylesheet or schema
        extension that can be used to verify conformance to the named
        style.
    :ivar lang:
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    status: list[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    dc_status: list[DcStatusType] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
            
        },
    )
    title: list[TextType4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    description: list[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    notice: list[NoticeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    front_matter: list[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "name": "front-matter",
            "type": "Element",
            
        },
    )
    rear_matter: list[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "name": "rear-matter",
            "type": "Element",
            
        },
    )
    reference: list[ReferenceType4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    plain_text: list[PlainTextType] = field(
        default_factory=list,
        metadata={
            "name": "plain-text",
            "type": "Element",
            
        },
    )
    platform_specification: Optional[PlatformSpecification] = field(
        default=None,
        metadata={
            "name": "platform-specification",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
        },
    )
    platform: list[Cpe2IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional[VersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    metadata: list[MetadataType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    model: list[Model] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    profile: list[Profile] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
        },
    )
    value: list[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    group: list[Group] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        },
    )
    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
        },
    )
    test_result: list[TestResult] = field(
        default_factory=list,
        metadata={
            "name": "TestResult",
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
            "pattern": r"xccdf_[^_]+_benchmark_.+",
        },
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    resolved: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_href: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-href",
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
