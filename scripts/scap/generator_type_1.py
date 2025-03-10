from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.schema_version_type import SchemaVersionType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class GeneratorType1:
    """The GeneratorType complex type defines an element that is used to hold
    information about when a particular OVAL document was compiled, what version of
    the schema was used, what tool compiled the document, and what version of that
    tool was used.

    Additional generator information is also allowed although it is not
    part of the official OVAL Schema. Individual organizations can place
    generator information that they feel are important and these will be
    skipped during the validation. All OVAL really cares about is that
    the stated generator information is there.

    :ivar product_name: The optional product_name specifies the name of
        the application used to generate the file. Product names SHOULD
        be expressed as CPE Names according to the Common Platform
        Enumeration: Name Matching Specification Version 2.3.
    :ivar product_version: The optional product_version specifies the
        version of the application used to generate the file.
    :ivar schema_version: The required schema_version specifies the
        version of the OVAL Schema that the document has been written in
        and that should be used for validation. The versions for both
        the Core and any platform extensions used should be declared in
        separate schema_version elements.
    :ivar timestamp: The required timestamp specifies when the
        particular OVAL document was compiled. The format for the
        timestamp is yyyy-mm-ddThh:mm:ss. Note that the timestamp
        element does not specify when a definition (or set of
        definitions) was created or modified but rather when the actual
        XML document that contains the definition was created. For
        example, the document might have pulled a bunch of existing OVAL
        Definitions together, each of the definitions having been
        created at some point in the past. The timestamp in this case
        would be when the combined document was created.
    :ivar any_element: The Asset Identification specification
        (http://scap.nist.gov/specifications/ai/) provides a
        standardized way of reporting asset information across different
        organizations. Asset Identification elements can hold data
        useful for identifying what tool, what version of that tool was
        used, and identify other assets used to compile an OVAL
        document, such as persons or organizations. To support greater
        interoperability, an ai:assets element describing assets used to
        produce an OVAL document may appear at this point in an OVAL
        document.
    """

    class Meta:
        name = "GeneratorType"

    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    schema_version: list[SchemaVersionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "min_occurs": 1,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
