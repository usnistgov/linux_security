from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.check_type_1 import CheckType1
from scap.notes_type_2 import NotesType2
from scap.references_type_1 import ReferencesType1
from scap.text_type_2 import TextType2

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class ItemType:
    """The ItemType complex type defines an element that represents a single CPE
    Name.

    The required name attribute is a URI which must be a unique key and
    should follow the URI structure outlined in the CPE Specification.
    The optional title element is used to provide a human-readable title
    for the platform. To support uses intended for multiple languages,
    this element supports the ‘xml:lang’ attribute. At most one title
    element can appear for each language. The notes element holds
    optional descriptive material. Multiple notes elements are allowed,
    but only one per language should be used. Note that the language
    associated with the notes element applies to all child note
    elements. The optional references element holds external info
    references. The optional check element is used to call out an OVAL
    Definition that can confirm or reject an IT system as an instance of
    the named platform. Additional elements not part of the CPE
    namespace are allowed and are just skipped by validation. In
    essence, a dictionary file can contain additional information that a
    user can choose to use or not, but this information is not required
    to be used or understood.
    """

    title: list[TextType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    notes: list[NotesType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    references: Optional[ReferencesType1] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    check: list[CheckType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    deprecated_by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        },
    )
    deprecation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
