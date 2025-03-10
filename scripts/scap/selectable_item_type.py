from dataclasses import dataclass, field
from decimal import Decimal

from scap.html_text_with_sub_type import HtmlTextWithSubType
from scap.idref_list_type import IdrefListType
from scap.idref_type import IdrefType
from scap.item_type_abstract import ItemTypeAbstract
from scap.overrideable_cpe2idref_type import OverrideableCpe2IdrefType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class SelectableItemType(ItemTypeAbstract):
    """
    This abstract item type represents the basic data shared by all
    &lt;xccdf:Group&gt; and &lt;xccdf:Rule&gt; elements.

    :ivar rationale: Descriptive text giving rationale or motivations
        for abiding by this &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt;
        (i.e., why it is important to the security of the target
        platform).
    :ivar platform: Platforms to which this
        &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt; applies.
    :ivar requires: The identifiers of other &lt;xccdf:Group&gt; or
        &lt;xccdf:Rule&gt; elements that must be selected for this
        &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt; to be evaluated and
        scored properly. Each &lt;xccdf:requires&gt; element specifies a
        list of one or more required items by their identifiers. If at
        least one of the specified &lt;xccdf:Group&gt; or
        &lt;xccdf:Rule&gt; elements is selected, the requirement is met.
    :ivar conflicts: The identifier of another &lt;xccdf:Group&gt; or
        &lt;xccdf:Rule&gt; that must be unselected for this
        &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt; to be evaluated and
        scored properly. Each &lt;xccdf:conflicts&gt; element specifies
        a single conflicting item using its idref attribute. If the
        specified &lt;xccdf:Group&gt; or &lt;xccdf:Rule&gt; element is
        not selected, the requirement is met.
    :ivar selected: If true, this &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt;
        is selected to be processed as part of the
        &lt;xccdf:Benchmark&gt; when it is applied to a target system.
        An unselected &lt;xccdf:Group&gt; does not get processed, and
        its contents are not processed either (i.e., all descendants of
        an unselected &lt;xccdf:Group&gt; are implicitly unselected). An
        unselected &lt;xccdf:Rule&gt; is not checked and does not
        contribute to scoring.
    :ivar weight: The relative scoring weight of this
        &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt;, for computing a score,
        expressed as a non-negative real number. It denotes the
        importance of an &lt;xccdf:Group&gt;/&lt;xccdf:Rule&gt;. Under
        some scoring models, scoring is computed independently for each
        collection of sibling &lt;xccdf:Group&gt; and &lt;xccdf:Rule&gt;
        elements, then normalized as part of the overall scoring
        process.
    """

    class Meta:
        name = "selectableItemType"

    rationale: list[HtmlTextWithSubType] = field(
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
    requires: list[IdrefListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    conflicts: list[IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    selected: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    weight: Decimal = field(
        default=Decimal("1.0"),
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "total_digits": 3,
        },
    )
