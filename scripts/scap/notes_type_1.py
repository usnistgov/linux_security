from dataclasses import dataclass, field

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class NotesType1:
    """The NotesType complex type is a container for one or more note child
    elements.

    Each note contains some information about the definition or tests
    that it references. A note may record an unresolved question about
    the definition or test or present the reason as to why a particular
    approach was taken.
    """

    class Meta:
        name = "NotesType"

    note: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
