from dataclasses import dataclass, field
from typing import Optional

from scap.notes_1 import Notes1
from scap.notes_2 import Notes2
from scap.operator_enumeration_1 import OperatorEnumeration1
from scap.signature import Signature

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class StateType:
    """The base type of every state includes an optional notes element and two
    attributes.

    The notes section of a state should be used to hold information that
    might be helpful to someone examining the technical aspects of the
    state. For example, why certain values have been used by the state,
    or maybe a link to where further information can be found. Please
    refer to the description of the NotesType complex type for more
    information about the notes element. The required id attribute
    uniquely identifies each state, and must conform to the format
    specified by the StateIdPattern simple type. The required version
    attribute holds the current version of the state. Versions are
    integers, starting at 1 and incrementing every time a state is
    modified. The required operator attribute provides the logical
    operator that binds the different characteristics inside a state
    together. The optional comment attribute provides a short
    description of the state. The optional deprecated attribute
    signifies that an id is no longer to be used or referenced but the
    information has been kept around for historic purposes. When
    evaluating a particular state against an object, one should evaluate
    each individual entity separately. The individual results are then
    combined by the operator to produce an overall result. This process
    holds true even when there are multiple instances of the same
    entity. Evaluate each instance separately, taking the entity check
    attribute into account, and then combine everything using the
    operator.
    """

    def generate_check(self, data):
        print("Generic state detected! Unimplemented!")

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
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:ste:[1-9][0-9]*",
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
    operator: OperatorEnumeration1 = field(
        default=OperatorEnumeration1.AND,
        metadata={
            "type": "Attribute",
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
