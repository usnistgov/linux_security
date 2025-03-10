from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TargetIdRefType:
    """Type for an &lt;xccdf:target-id-ref&gt; element in an
    &lt;xccdf:TestResult&gt; element.

    This element contains references to external structures with
    identifying information about the target of an assessment.

    :ivar system: Indicates the language in which this identifying
        information is expressed. If the identifying language uses XML
        namespaces, then the @system attribute for the language should
        be its namespace.
    :ivar href: Points to the external resource (e.g., a file) that
        contains the identifying information.
    :ivar name: Identifies a specific structure within the referenced
        file. If the @name attribute is absent, the reference is to the
        entire resource indicated in the @href attribute.
    """

    class Meta:
        name = "targetIdRefType"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
