from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from scap.status_type import StatusType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Status:
    """The acceptance status of an element with an optional date attribute, which
    signifies the date of the status change.

    If an element does not have its own &lt;xccdf:status&gt; element,
    its status is that of its parent element. If there is more than one
    &lt;xccdf:status&gt; for a single element, then every instance of
    the &lt;xccdf:status&gt; element must have a @date attribute, and
    the &lt;xccdf:status&gt; element with the latest date is considered
    the current status.

    :ivar value:
    :ivar date: The date the parent element achieved the indicated
        status.
    """

    class Meta:
        name = "status"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    value: Optional[StatusType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
