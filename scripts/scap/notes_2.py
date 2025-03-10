from dataclasses import dataclass

from scap.notes_type_1 import NotesType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Notes2(NotesType1):
    """The notes element is a container for one or more note child elements.

    It exists for backwards-compatibility purposes, for the pre-5.11.0
    oval-def:NotesType, which has been replaced by the oval:notes
    element in 5.11.1.
    """

    class Meta:
        name = "notes"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"
