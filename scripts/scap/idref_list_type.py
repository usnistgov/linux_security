from dataclasses import dataclass, field

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class IdrefListType:
    """
    Data type for elements contain list of references to other XCCDF elements.

    :ivar idref: A space-separated list of id values from other XCCDF
        elements
    """

    class Meta:
        name = "idrefListType"

    idref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
