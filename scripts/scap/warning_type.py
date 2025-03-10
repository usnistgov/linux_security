from dataclasses import dataclass, field

from scap.html_text_with_sub_type import HtmlTextWithSubType
from scap.warning_category_enum_type import WarningCategoryEnumType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class WarningType(HtmlTextWithSubType):
    """Data type for the &lt;xccdf:warning&gt; element under the &lt;xccdf:Rule&gt;
    element.

    This element holds a note or caveat about the item intended to
    convey important cautionary information for the
    &lt;xccdf:Benchmark&gt; user.

    :ivar category: A hint as to the nature of the warning.
    """

    class Meta:
        name = "warningType"

    category: WarningCategoryEnumType = field(
        default=WarningCategoryEnumType.GENERAL,
        metadata={
            "type": "Attribute",
        },
    )
