from dataclasses import dataclass, field
from typing import Optional

from scap.class_enumeration import ClassEnumeration
from scap.criteria_type import CriteriaType
from scap.metadata_type_1 import MetadataType1
from scap.notes_1 import Notes1
from scap.notes_2 import Notes2
from scap.signature import Signature

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class DefinitionType:
    """The DefinitionType defines a single OVAL Definition.

    A definition is the key structure in OVAL. It is analogous to the
    logical sentence or proposition: if a computer's state matches the
    configuration parameters laid out in the criteria, then that
    computer exhibits the state described. The DefinitionType contains a
    section for various metadata related elements that describe the
    definition. This includes a description, version, affected system
    types, and reference information. The notes section of a definition
    should be used to hold information that might be helpful to someone
    examining the technical aspects of the definition. For example, why
    certain tests have been included in the criteria, or maybe a link to
    where further information can be found. The DefinitionType also
    (unless the definition is deprecated) contains a criteria child
    element that joins individual tests together with a logical operator
    to specify the specific computer state being described. The required
    id attribute is the OVAL-ID of the Definition. The form of an OVAL-
    ID must follow the specific format described by the
    oval:DefinitionIDPattern. The required version attribute holds the
    current version of the definition. Versions are integers, starting
    at 1 and incrementing every time a definition is modified. The
    required class attribute indicates the specific class to which the
    definition belongs. The class gives a hint to a user so they can
    know what the definition writer is trying to say. See the definition
    of oval-def:ClassEnumeration for more information about the
    different valid classes. The optional deprecated attribute signifies
    that an id is no longer to be used or referenced but the information
    has been kept around for historic purposes. When the deprecated
    attribute is set to true, the definition is considered to be
    deprecated. The criteria child element of a deprecated definition is
    optional. If a deprecated definition does not contain a criteria
    child element, the definition must evaluate to "not evaluated". If a
    deprecated definition contains a criteria child element, an
    interpreter should evaluate the definition as if it were not
    deprecated, but an interpreter may evaluate the definition to "not
    evaluated".
    """

    def generate_check(self, data):
        print(f"Recursively generating the check for definition {self.id}")
        return self.criteria.generate_check(data)

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    metadata: Optional[MetadataType1] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
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
    criteria: Optional[CriteriaType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:def:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    class_value: Optional[ClassEnumeration] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
