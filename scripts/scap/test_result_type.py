from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.benchmark_reference_type import BenchmarkReferenceType
from scap.cpe2idref_type import Cpe2IdrefType
from scap.identity_type import IdentityType
from scap.idref_type import IdrefType
from scap.metadata_type_2 import MetadataType2
from scap.profile_set_complex_value_type import ProfileSetComplexValueType
from scap.profile_set_value_type import ProfileSetValueType
from scap.rule_result_type import RuleResultType
from scap.score_type import ScoreType
from scap.signature_type_2 import SignatureType2
from scap.tailoring_reference_type import TailoringReferenceType
from scap.target_facts_type import TargetFactsType
from scap.target_id_ref_type import TargetIdRefType
from scap.text_type_4 import TextType4

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TestResultType:
    """Data type for the &lt;xccdf:TestResult&gt; element, which holds the results
    of one application of the &lt;xccdf:Benchmark&gt;.

    The &lt;xccdf:TestResult&gt; element normally appears as the child
    of the &lt;xccdf:Benchmark&gt; element, although it may also appear
    as the top-level element of an XCCDF results document. XCCDF is not
    intended to be a database format for detailed results; the
    &lt;xccdf:TestResult&gt; element offers a way to store the results
    of individual tests in modest detail, with the ability to reference
    lower-level testing data. Although several of the child elements of
    this type technically support the @override attribute, the
    &lt;xccdf:TestResult&gt; element cannot be extended. Therefore,
    @override has no meaning within an &lt;xccdf:TestResult&gt; element
    and its children, and should not be used for them.

    :ivar benchmark: Reference to the &lt;xccdf:Benchmark&gt; for which
        the &lt;xccdf:TestResult&gt; records results. This property is
        required if this &lt;xccdf:TestResult&gt; element is the top-
        level element and optional otherwise.
    :ivar tailoring_file: The tailoring file element contains attributes
        used to identify an &lt;xccdf:Tailoring&gt; element used to
        guide the assessment reported on in this
        &lt;xccdf:TestResult&gt;. The tailoring element is required in
        an &lt;xccdf:TestResult&gt; if and only if an
        &lt;xccdf:Tailoring&gt; element guided the assessment recorded
        in the &lt;xccdf:TestResult&gt; or if the
        &lt;xccdf:Tailoring&gt; element records manual tailoring actions
        applied to this assessment.
    :ivar title: Title of the test.
    :ivar remark: A remark about the test, possibly supplied by the
        person administering the &lt;xccdf:Benchmark&gt; assessment
    :ivar organization: The name of the organization or other entity
        responsible for applying this &lt;xccdf:Benchmark&gt; and
        generating this result. When multiple &lt;xccdf:organization&gt;
        elements are used to indicate multiple organization names in a
        hierarchical organization, the highest-level organization should
        appear first.
    :ivar identity: Information about the system identity or user
        employed during application of the &lt;xccdf:Benchmark&gt;. If
        used, specifies the name of the authenticated identity.
    :ivar profile: The &lt;xccdf:profile&gt; element holds the value of
        the @id attribute value of the &lt;xccdf:Profile&gt; selected to
        be used in the assessment reported on by this
        &lt;xccdf:TestResult&gt;. This &lt;xccdf:Profile&gt; might be
        from the &lt;xccdf:Benchmark&gt; or from an
        &lt;xccdf:Tailoring&gt; file, if used. This element should
        appear if and only if an &lt;xccdf:Profile&gt; was selected to
        guide the assessment.
    :ivar target: Name or description of the target system whose test
        results are recorded in the &lt;xccdf:TestResult&gt; element
        (the system to which an &lt;xccdf:Benchmark&gt; test was
        applied). Each appearance of the element supplies a name by
        which the target host or device was identified at the time the
        test was run. The name may be any string, but applications
        should include the fully qualified DNS name whenever possible.
    :ivar target_address: Network address of the target system to which
        an &lt;xccdf:Benchmark&gt; test was applied. Typical forms for
        the address include IP version 4 (IPv4), IP version 6 (IPv6),
        and Ethernet media access control (MAC).
    :ivar target_facts: A list of named facts about the target system or
        platform.
    :ivar target_id_ref: References to external structures with
        identifying information about the target of this assessment.
    :ivar other_element: Identifying information expressed in other XML
        formats can be included here.
    :ivar platform: A platform on the target system. There should be one
        instance of this property for every platform that the target
        system was found to meet.
    :ivar set_value: Specific setting for a single &lt;xccdf:Value&gt;
        element used during the test.
    :ivar set_complex_value: Specific setting for a single
        &lt;xccdf:Value&gt; element used during the test when the given
        value is set to a complex type, such as a list.
    :ivar rule_result: The result of a single instance of an
        &lt;xccdf:Rule&gt; application against the target. The
        &lt;xccdf:TestResult&gt; must include at least one
        &lt;xccdf:rule-result&gt; record for each &lt;xccdf:Rule&gt;
        that was selected in the resolved &lt;xccdf:Benchmark&gt;.
    :ivar score: An overall score for this &lt;xccdf:Benchmark&gt; test.
    :ivar metadata: XML metadata associated with this
        &lt;xccdf:TestResult&gt;.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:TestResult&gt;.
    :ivar id: Unique identifier for this element.
    :ivar start_time: Time when testing began.
    :ivar end_time: Time when testing was completed and the results
        recorded.
    :ivar test_system: Name of the benchmark consumer program that
        generated this &lt;xccdf:TestResult&gt; element; should be
        either a CPE name or a CPE applicability language expression.
    :ivar version: The version number string copied from the
        &lt;xccdf:Benchmark&gt; used to direct this assessment.
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    """

    class Meta:
        name = "testResultType"

    benchmark: Optional[BenchmarkReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    tailoring_file: Optional[TailoringReferenceType] = field(
        default=None,
        metadata={
            "name": "tailoring-file",
            "type": "Element",
            
        },
    )
    title: list[TextType4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    remark: list[TextType4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    organization: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    identity: Optional[IdentityType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    profile: Optional[IdrefType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    target: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )
    target_address: list[str] = field(
        default_factory=list,
        metadata={
            "name": "target-address",
            "type": "Element",
            
        },
    )
    target_facts: Optional[TargetFactsType] = field(
        default=None,
        metadata={
            "name": "target-facts",
            "type": "Element",
            
        },
    )
    target_id_ref: list[TargetIdRefType] = field(
        default_factory=list,
        metadata={
            "name": "target-id-ref",
            "type": "Element",
            
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    platform: list[Cpe2IdrefType] = field(
        default_factory=list,
        metadata={
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
    set_complex_value: list[ProfileSetComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-complex-value",
            "type": "Element",
            
        },
    )
    rule_result: list[RuleResultType] = field(
        default_factory=list,
        metadata={
            "name": "rule-result",
            "type": "Element",
            
        },
    )
    score: list[ScoreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
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
            "pattern": r"xccdf_[^_]+_testresult_.+",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "start-time",
            "type": "Attribute",
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "end-time",
            "type": "Attribute",
            "required": True,
        },
    )
    test_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "test-system",
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
