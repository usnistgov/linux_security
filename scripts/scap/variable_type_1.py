from dataclasses import dataclass, field
from typing import Optional

from scap.notes_1 import Notes1
from scap.notes_2 import Notes2
from scap.signature import Signature
from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class VariableType1:
    """The VariableType complex type defines attributes associated with each OVAL
    Variable.

    The required id attribute uniquely identifies each variable, and
    must conform to the format specified by the VariableIDPattern simple
    type. The required version attribute holds the current version of
    the variable. Versions are integers, starting at 1 and incrementing
    every time a variable is modified. The required comment attribute
    provides a short description of the variable. The optional
    deprecated attribute signifies that an id is no longer to be used or
    referenced but the information has been kept around for historic
    purposes. The required datatype attribute specifies the type of
    value being defined.  The set of values identified by a variable
    must comply with the specified datatype, otherwise an error should
    be reported. Please see the DatatypeEnumeration for details about
    each valid datatype.  For example, if the datatype of the variable
    is specified as boolean then the value(s) returned by the component
    / function should be "true", "false", "1", or "0". Note that the
    'record' datatype is not permitted on variables. The notes section
    of a variable should be used to hold information that might be
    helpful to someone examining the technical aspects of the variable.
    Please refer to the description of the NotesType complex type for
    more information about the notes element.

    :ivar signature:
    :ivar notes:
    :ivar oval_mitre_org_xmlschema_oval_common_5_notes:
    :ivar id:
    :ivar version:
    :ivar datatype: Note that the 'record' datatype is not permitted on
        variables.
    :ivar comment:
    :ivar deprecated:
    """

    class Meta:
        name = "VariableType"

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
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[SimpleDatatypeEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
