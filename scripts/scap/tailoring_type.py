from dataclasses import dataclass, field
from typing import Optional

from scap.dc_status_type import DcStatusType
from scap.metadata_type_2 import MetadataType2
from scap.profile import Profile
from scap.signature_type_2 import SignatureType2
from scap.status import Status
from scap.tailoring_benchmark_reference_type import (
    TailoringBenchmarkReferenceType,
)
from scap.tailoring_version_type import TailoringVersionType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TailoringType:
    """Data type for the &lt;xccdf:Tailoring&gt; element.

    The &lt;xccdf:Tailoring&gt; element allows named tailorings (i.e.,
    &lt;xccdf:Profile&gt; elements) of an &lt;xccdf:Benchmark&gt; to be
    defined separately from the &lt;xccdf:Benchmark&gt; itself. The
    &lt;xccdf:Profile&gt; elements in an &lt;xccdf:Tailoring&gt; element
    can be used in two ways: First, an organization might wish to pre-
    define a set of tailoring actions to be applied on top of or instead
    of the tailoring performed by an &lt;xccdf:Benchmark&gt; element's
    &lt;xccdf:Profile&gt; elements. Second, an &lt;xccdf:Tailoring&gt;
    element can be used to record manual tailoring actions performed
    during the course of an assessment.

    :ivar benchmark: Identifies the &lt;xccdf:Benchmark&gt; to which
        this tailoring applies. A &lt;xccdf:Tailoring&gt; document is
        only applicable to a single &lt;xccdf:Benchmark&gt;. Note,
        however, that this is a purely informative field.
    :ivar status: Status of the tailoring and date at which it attained
        that status. Authors may use this element to record the maturity
        or consensus level of an &lt;xccdf:Tailoring&gt; element.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar version: The version of this &lt;xccdf:Tailoring&gt; element,
        with a required @time attribute that records when the
        &lt;xccdf:Tailoring&gt; element was created. This timestamp is
        necessary because, under some circumstances, a copy of an
        &lt;xccdf:Tailoring&gt; document might be automatically
        generated. Without the version and timestamp, tracking of these
        automatically created &lt;xccdf:Tailoring&gt; documents could
        become problematic.
    :ivar metadata: XML metadata for the &lt;xccdf:Tailoring&gt;
        element.
    :ivar profile: &lt;xccdf:Profile&gt; elements that reference and
        customize sets of items in an &lt;xccdf:Benchmark&gt;.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:Tailoring&gt;.
    :ivar id: Unique identifier for this element.
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    """

    class Meta:
        name = "tailoringType"

    benchmark: Optional[TailoringBenchmarkReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
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
    version: Optional[TailoringVersionType] = field(
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
    profile: list[Profile] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
            "min_occurs": 1,
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
            "pattern": r"xccdf_[^_]+_tailoring_.+",
        },
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
