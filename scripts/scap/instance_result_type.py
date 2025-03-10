from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class InstanceResultType:
    """Type for an &lt;xccdf:instance&gt; element in an &lt;xccdf:rule-result&gt;.

    The content is a string, but the element may also have
    two attributes: @context and @parentContext. Both attributes are intended to provide
    hints as to the nature of the substituted content. This body of this type records
    the details of the target system instance for multiply instantiated
    &lt;xccdf:Rule&gt; elements.

    :ivar value:
    :ivar context: Describes the scope or significance of the instance
        content.
    :ivar parent_context: Used to express nested structure in instance
        context structures.
    """

    class Meta:
        name = "instanceResultType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    context: str = field(
        default="undefined",
        metadata={
            "type": "Attribute",
        },
    )
    parent_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentContext",
            "type": "Attribute",
        },
    )
