from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.extension_container_type import ExtensionContainerType
from scap.user_type import UserType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class GeneratorType3:
    """The GeneratorType type defines an element that is used to hold information
    about when a particular OCIL document was generated, what version of the schema
    was used, what tool was used to generate the document, and what version of the
    tool was used.

    Additional generator information is also allowed although it is not
    part of the official OCIL language. Individual organizations can
    place generator information that they feel is important.

    :ivar product_name: The product_name element specifies the name of
        the application used to generate the file.
    :ivar product_version: The product_version element specifies the
        version of the application used to generate the file.
    :ivar author: The author element identifies one of the authors of
        this document.
    :ivar schema_version: The schema_version element specifies the
        version of the OCIL schema that the document has been written in
        and that should be used for validation.
    :ivar timestamp: The timestamp element specifies when the particular
        OCIL document was generated. The format for the timestamp is
        yyyy-mm-ddThh:mm:ss.
    :ivar additional_data: The additional_data element can be used to
        contain metadata extensions about the generator used to create
        the OCIL document instance.
    """

    class Meta:
        name = "GeneratorType"

    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    author: list[UserType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    additional_data: Optional[ExtensionContainerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
