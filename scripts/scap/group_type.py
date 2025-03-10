from dataclasses import dataclass, field
from typing import Optional

from scap.rule import Rule
from scap.selectable_item_type import SelectableItemType
from scap.signature_type_2 import SignatureType2
from scap.value import Value

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class GroupType(SelectableItemType):
    """Data type for the &lt;xccdf:Group&gt; element.

    A &lt;xccdf:Group&gt; element contains descriptive information about
    a portion of an &lt;xccdf:Benchmark&gt;, as well as
    &lt;xccdf:Rule&gt;, &lt;xccdf:Value&gt;, and/or other
    &lt;xccdf:Group&gt; elements

    :ivar value: &lt;xccdf:Value&gt; elements that belong to this
        &lt;xccdf:Group&gt;.
    :ivar group: Sub-&lt;xccdf:Groups&gt; under this
        &lt;xccdf:Group&gt;.
    :ivar rule: &lt;xccdf:Rule&gt; elements that belong to this
        &lt;xccdf:Group&gt;.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        &lt;xccdf:Group&gt;.
    :ivar id: Unique element identifier; used by other elements to refer
        to this element.
    """

    class Meta:
        name = "groupType"

    value: list[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        },
    )
    group: list["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        },
    )
    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
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
            "pattern": r"xccdf_[^_]+_group_.+",
        },
    )


@dataclass
class Group(GroupType):
    """An item that can hold other items.

    It allows an author to collect related items into a common structure
    and provide descriptive text and references about them.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
