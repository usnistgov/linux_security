from dataclasses import dataclass, field
from typing import Optional

from scap.notes_1 import Notes1
from scap.notes_2 import Notes2
from scap.signature import Signature


__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ObjectType2:
    """The base type of every object includes an optional notes element.

    The notes element of an object should be used to hold information
    that might be helpful to someone examining the technical aspects of
    the object. For example, why certain values have been used, or maybe
    a link to where further information can be found. Please refer to
    the description of the NotesType complex type for more information
    about the notes element. The required id attribute uniquely
    identifies each object, and must conform to the format specified by
    the ObjectIdPattern simple type. The required version attribute
    holds the current version of the object element. Versions are
    integers, starting at 1 and incrementing every time an object is
    modified. The optional comment attribute provides a short
    description of the object. The optional deprecated attribute
    signifies that an id is no longer to be used or referenced but the
    information has been kept around for historic purposes.
    """

    class Meta:
        name = "ObjectType"
    
    def generate_check(self, data):
        print(f"This Object is NOT supported! {self.id}")

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    notes: Optional[Notes2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    oval_mitre_org_xmlschema_oval_common_5_notes: Optional[Notes1] = field(
        default=None,
        metadata={
            "name": "notes",
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    version_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "version",
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
