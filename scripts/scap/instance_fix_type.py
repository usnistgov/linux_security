from dataclasses import dataclass, field

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class InstanceFixType:
    """Type for an &lt;xccdf:instance&gt; element which may appear in an
    &lt;xccdf:fix&gt; element.

    The &lt;xccdf:instance&gt; element inside an &lt;xccdf:fix&gt;
    element designates a spot where the name of the instance should be
    substituted into the fix template to generate the final fix data.

    :ivar context: Describes the scope or significance of the instance
        content. The context attribute is intended to be informative and
        does not affect basic processing.
    """

    class Meta:
        name = "instanceFixType"

    context: str = field(
        default="undefined",
        metadata={
            "type": "Attribute",
        },
    )
