from dataclasses import dataclass

from scap.notes_type_1 import NotesType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class Notes1(NotesType1):
    """
    Element for containing notes; can be replaced using a substitution group.
    """

    class Meta:
        name = "notes"
        namespace = "http://oval.mitre.org/XMLSchema/oval-common-5"
