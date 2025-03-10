from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://cpe.mitre.org/dictionary/2.0"


@dataclass
class GeneratorType2:
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
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            
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
