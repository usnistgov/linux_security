from dataclasses import dataclass, field
from typing import Optional

from oval.definitions.oval_common_schema import GeneratorType
from oval.definitions.oval_results_schema import (
    ClassDirectivesType,
    DefaultDirectivesType,
)
from oval.definitions.xmldsig_core_schema import Signature

__NAMESPACE__ = "urn:oval:v6:directives"


@dataclass
class OvalDirectives:
    """The oval_directives element is the root of an OVAL Directive Document.

    Its purpose is to bind together the generator and the set of
    directives contained in the document. The generator section must be
    present and provides information about when the directives document
    was compiled and under what version. The optional Signature element
    allows an XML Signature as defined by the W3C to be attached to the
    document. This allows authentication and data integrity to be
    provided to the user. Enveloped signatures are supported. More
    information about the official W3C Recommendation regarding XML
    digital signatures can be found at
    http://www.w3.org/TR/xmldsig-core/.

    :ivar generator: The required generator section provides information
        about when the directives document was compiled and under what
        version.
    :ivar directives: The required directives section presents flags
        describing what information must be been included in an oval
        results document. This element represents the default set of
        directives. These directives apply to all classes of definitions
        for which there is not a class specific set of directives.
    :ivar class_directives: The optional class_directives section
        presents flags describing what information has been included in
        the results document for a specific OVAL Definition class. The
        directives for a particlar class override the default
        directives.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_directives"
        namespace = "urn:oval:v6:directives"

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    directives: Optional[DefaultDirectivesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    class_directives: list[ClassDirectivesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
