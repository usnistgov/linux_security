from dataclasses import dataclass, field

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ComplexValueType:
    """Data type that supports values that are lists of simple types.

    Each element in the list is represented by an instance of the
    &lt;xccdf:item&gt; child element. If there are no &lt;xccdf:item&gt;
    child elements then this represents an empty list.

    :ivar item: A single item in the list of values.
    """

    class Meta:
        name = "complexValueType"

    item: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
