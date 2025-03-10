from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class CheckExportType:
    """Data type for the &lt;xccdf:check-export&gt; element, which specifies a
    mapping from an &lt;xccdf:Value&gt; element to a checking system variable
    (i.e., external name or id for use by the checking system).

    This supports export of tailoring &lt;xccdf:Value&gt; elements from
    the XCCDF processing environment to the checking system. The
    interface between the XCCDF benchmark consumer and the checking
    system should support, at a minimum, passing the &lt;xccdf:value&gt;
    property of the &lt;xccdf:Value&gt; element, but may also support
    passing the &lt;xccdf:Value&gt; element's @type and @operator
    properties.

    :ivar value_id: The id of the &lt;xccdf:Value&gt; element to export.
    :ivar export_name: An identifier indicating some structure in the
        checking system into which the identified &lt;xccdf:Value&gt;
        element's properties will be mapped.
    """

    class Meta:
        name = "checkExportType"

    value_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "value-id",
            "type": "Attribute",
            "required": True,
        },
    )
    export_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "export-name",
            "type": "Attribute",
            "required": True,
        },
    )
