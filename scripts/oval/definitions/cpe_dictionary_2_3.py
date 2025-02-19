from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class CheckType:
    """The CheckType complex type is used to define an element to hold information
    about an individual check.

    It includes a checking system specification URI, string content, and
    an optional external file reference. The checking system
    specification should be the URI for a particular version of OVAL or
    a related system testing language, and the content will be an
    identifier of a test written in that language. The external file
    reference could be used to point to the file in which the content
    test identifier is defined.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
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
        },
    )


@dataclass
class GeneratorType:
    """The GeneratorType complex type defines an element that is used to hold
    information about when a particular document was compiled, what version of the
    schema was used, what tool compiled the document, and what version of that tool
    was used.

    Additional generator information is also allowed although it is not
    part of the official schema. Individual organizations can place
    generator information that they feel is important and it will be
    skipped during the validation. All that this schema really cares
    about is that the stated generator information is there.

    :ivar product_name: The optional product_name element specifies the
        name of the application used to generate the file.
    :ivar product_version: The optional product_version element
        specifies the version of the application used to generate the
        file.
    :ivar schema_version: The required schema_version element specifies
        the version of the schema that the document has been written
        against and that should be used for validation.
    :ivar timestamp: The required timestamp element specifies when the
        particular document was compiled. The format for the timestamp
        is yyyy-mm-ddThh:mm:ss. Note that the timestamp element does not
        specify when an item in the document was created or modified but
        rather when the actual XML document that contains the items was
        created. For example, a document might pull a bunch of existing
        items together, each of which was created at some point in the
        past. The timestamp in this case would be when this combined
        document was created.
    :ivar other_element:
    """

    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class NotesType:
    """The NotesType complex type defines an element that consists of one or more
    child note elements.

    It is assumed that each of these note elements is representative of
    the same language as defined by their parent.
    """

    note: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class ReferencesType:
    """The ReferencesType complex type defines an element used to hold a collection
    of individual references.

    Each reference consists of a piece of text (intended to be human-
    readable) and a URI (intended to be a URL, and point to a real
    resource) and is used to point to extra descriptive material, for
    example a supplier's web site or platform documentation.
    """

    reference: list["ReferencesType.Reference"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Reference:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class TextType:
    """
    The TextType complex type allows the xml:lang attribute to associate a specific
    language with an element's string content.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


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

    title: list[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    notes: list[NotesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional[ReferencesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    check: list[CheckType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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
            "pattern": r"[cC][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
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
            "pattern": r"[cC][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        },
    )
    deprecation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CpeItem(ItemType):
    """The cpe-item element denotes a single CPE Name.

    Please refer to the description of ItemType for additional
    information about the structure of this element.
    """

    class Meta:
        name = "cpe-item"
        namespace = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class ListType:
    """The ListType complex type defines an element that is used to hold a
    collection of individual items.

    The required generator section provides information about when the
    definition file was compiled and under what version. Additional
    elements not part of the CPE namespace are allowed and are just
    skipped by validation. In essence, a dictionary file can contain
    additional information that a user can choose to use or not, but
    this information is not required to be used or understood.
    """

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cpe_item: list[CpeItem] = field(
        default_factory=list,
        metadata={
            "name": "cpe-item",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/dictionary/2.0",
            "min_occurs": 1,
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class CpeList(ListType):
    """The cpe-list element acts as a top-level container for CPE Name items.

    Each individual item must be unique. Please refer to the description
    of ListType for additional information about the structure of this
    element.
    """

    class Meta:
        name = "cpe-list"
        namespace = "http://cpe.mitre.org/dictionary/2.0"
