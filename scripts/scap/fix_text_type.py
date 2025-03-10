from dataclasses import dataclass, field
from typing import Optional

from scap.fix_strategy_enum_type import FixStrategyEnumType
from scap.html_text_with_sub_type import HtmlTextWithSubType
from scap.rating_enum_type import RatingEnumType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class FixTextType(HtmlTextWithSubType):
    """Data type for the &lt;xccdf:fixtext&gt; element, which contains data that
    describes how to bring a target system into compliance with an
    &lt;xccdf:Rule&gt;.

    Each &lt;xccdf:fixtext&gt; element may be associated with one or
    more &lt;xccdf:fix&gt; elements through the @fixref attribute. The
    body holds explanatory text about the fix procedures.

    :ivar fixref: A reference to the @id of an &lt;xccdf:fix&gt;
        element.
    :ivar reboot: True if a reboot is known to be required and false
        otherwise.
    :ivar strategy: The method or approach for making the described fix.
    :ivar disruption: An estimate of the potential for disruption or
        operational degradation that the application of this fix will
        impose on the target.
    :ivar complexity: The estimated complexity or difficulty of applying
        the fix to the target.
    """

    class Meta:
        name = "fixTextType"

    fixref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reboot: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    strategy: FixStrategyEnumType = field(
        default=FixStrategyEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
    disruption: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
    complexity: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        },
    )
