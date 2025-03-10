from dataclasses import dataclass, field
from typing import Optional, Union

from scap.dc_status_type import DcStatusType
from scap.html_text_with_sub_type import HtmlTextWithSubType
from scap.lang_value import LangValue
from scap.metadata_type_2 import MetadataType2
from scap.reference_type_4 import ReferenceType4
from scap.status import Status
from scap.text_type_4 import TextType4
from scap.text_with_sub_type import TextWithSubType
from scap.version_type import VersionType
from scap.warning_type import WarningType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ItemTypeAbstract:
    """This abstract itemType represents the basic data shared by all
    &lt;xccdf:Group&gt;, &lt;xccdf:Rule&gt; and &lt;xccdf:Value&gt; elements.

    All elements in an itemType are optional, although each element that
    builds on the itemType may add its own elements, some of which will
    be required for that element.

    :ivar status: Status of the item and date at which it attained that
        status. &lt;xccdf:Benchmark&gt; authors may use this element to
        record the maturity or consensus level for elements in the
        &lt;xccdf:Benchmark&gt;. If an item does not have an explicit
        &lt;xccdf:status&gt; given, then its status is that of its
        parent.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar version: Version information about this item.
    :ivar title: Title of the item. Every item should have an
        &lt;xccdf:title&gt;, because this helps people understand the
        purpose of the item.
    :ivar description: Text that describes the item.
    :ivar warning: A note or caveat about the item intended to convey
        important cautionary information for the &lt;xccdf:Benchmark&gt;
        user (e.g., “Complying with this rule will cause the system to
        reject all IP packets”). If multiple &lt;xccdf:warning&gt;
        elements appear, benchmark consumers should concatenate them for
        generating reports or documents. Benchmark consumers may present
        this information in a special manner in generated documents.
    :ivar question: Interrogative text to present to the user during
        tailoring. It may also be included into a generated document.
        For &lt;xccdf:Rule&gt; and &lt;xccdf:Group&gt; elements, the
        &lt;xccdf:question&gt; text should be a simple binary (yes/no)
        question because it is supporting the selection aspect of
        tailoring. For &lt;xccdf:Value&gt; elements, the
        &lt;xccdf:question&gt; should solicit the user to provide a
        specific value. Tools may also display constraints on values and
        any defaults as specified by the other &lt;xccdf:Value&gt;
        properties.
    :ivar reference: References where the user can learn more about the
        subject of this item.
    :ivar metadata: XML metadata associated with this item, such as
        sources, special information, or other details.
    :ivar abstract: If true, then this item is abstract and exists only
        to be extended. The use of this attribute for
        &lt;xccdf:Group&gt; elements is deprecated and should be
        avoided.
    :ivar cluster_id: An identifier to be used as a means to identify
        (refer to) related items. It designates membership in a cluster
        of items, which are used for controlling items via
        &lt;xccdf:Profile&gt; elements. All the items with the same
        cluster identifier belong to the same cluster. A selector in an
        &lt;xccdf:Profile&gt; may refer to a cluster, thus making it
        easier for authors to create and maintain &lt;xccdf:Profile&gt;
        elements in a complex &lt;xccdf:Benchmark&gt;.
    :ivar extends: The identifier of an item on which to base this item.
        If present, it must have a value equal to the @id attribute of
        another item. The use of this attribute for &lt;xccdf:Group&gt;
        elements is deprecated and should be avoided.
    :ivar hidden: If this item should be excluded from any generated
        documents although it may still be used during assessments.
    :ivar prohibit_changes: If benchmark producers should prohibit
        changes to this item during tailoring. An author should use this
        when they do not want to allow end users to change the item.
    :ivar lang:
    :ivar base:
    :ivar id: An identifier used for referencing elements included in an
        XML signature
    """

    class Meta:
        name = "itemType"

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
            
        },
    )
    description: list[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    warning: list[WarningType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    question: list[TextType4] = field(
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
    metadata: list[MetadataType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    cluster_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "cluster-id",
            "type": "Attribute",
        },
    )
    extends: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    prohibit_changes: bool = field(
        default=False,
        metadata={
            "name": "prohibitChanges",
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
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
