from dataclasses import dataclass, field
from typing import Optional

from scap.definitions_type import DefinitionsType
from scap.generator_type_1 import GeneratorType1
from scap.objects_type import ObjectsType
from scap.signature import Signature
from scap.states_type import StatesType
from scap.tests_type import TestsType
from scap.variables_type_1 import VariablesType1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class OvalDefinitions:
    """The oval_definitions element is the root of an OVAL Definition Document.

    Its purpose is to bind together the major sections of a document - generator, definitions, tests, objects, states, and variables - which are the children of the root element.

    :ivar generator: The required generator section provides information
        about when the definition file was compiled and under what
        version.
    :ivar definitions: The optional definitions section contains 1 or
        more definitions.
    :ivar tests: The optional tests section contains 1 or more tests.
    :ivar objects: The optional objects section contains 1 or more
        objects.
    :ivar states: The optional states section contains 1 or more states.
    :ivar variables: The optional variables section contains 1 or more
        variables.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_definitions"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    generator: Optional[GeneratorType1] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    definitions: Optional[DefinitionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    tests: Optional[TestsType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    objects: Optional[ObjectsType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    states: Optional[StatesType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    variables: Optional[VariablesType1] = field(
        default=None,
        metadata={
            "type": "Element",
            
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
