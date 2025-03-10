from dataclasses import dataclass, field

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ItemBaseType:
    """The ItemBaseType complex type defines structures allowing a set of notes to
    be included.

    This type is inherited by many of the elements in the OCIL language.

    :ivar notes: An optional set of notes to describe additional
        information.
    :ivar revision: The specific refision of this item. This attribute
        is optional to support compatability with existing content.  By
        default the revision is '0' meaning that it is the initial
        revision. It is assumed that subsequent revisions will increment
        this value by 1.
    """

    notes: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    revision: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
