from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.result_enum_type import ResultEnumType
from scap.text_type_4 import TextType4

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class OverrideType:
    """Type for an &lt;xccdf:override&gt; element in an &lt;xccdf:rule-result&gt;.

    This element is used to record manual modification or annotation of
    a particular &lt;xccdf:rule-result&gt;. All attributes and child
    elements are required. It will not always be the case that the
    &lt;xccdf:new-result&gt; value will differ from the &lt;xccdf:old-
    result&gt; value. They might match if an authority wished to make a
    remark on the result without changing it. If &lt;xccdf:new-
    result&gt; and &lt;xccdf:old-result&gt; differ, the
    &lt;xccdf:result&gt; element of the enclosing &lt;xccdf:rule-
    result&gt; must match the &lt;xccdf:new-result&gt; value.

    :ivar old_result: The &lt;xccdf:rule-result&gt; status before this
        override.
    :ivar new_result: The new, override &lt;xccdf:rule-result&gt;
        status.
    :ivar remark: Rationale or explanation text for why or how the
        override was applied.
    :ivar time: When the override was applied.
    :ivar authority: Name or other identification for the human
        principal authorizing the override.
    """

    class Meta:
        name = "overrideType"

    old_result: Optional[ResultEnumType] = field(
        default=None,
        metadata={
            "name": "old-result",
            "type": "Element",
            
            "required": True,
        },
    )
    new_result: Optional[ResultEnumType] = field(
        default=None,
        metadata={
            "name": "new-result",
            "type": "Element",
            
            "required": True,
        },
    )
    remark: Optional[TextType4] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
