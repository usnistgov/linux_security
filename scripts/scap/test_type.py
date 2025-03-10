from dataclasses import dataclass, field
from typing import Optional

from scap.check_enumeration import CheckEnumeration
from scap.existence_enumeration import ExistenceEnumeration
from scap.notes_1 import Notes1
from scap.notes_2 import Notes2
from scap.operator_enumeration_1 import OperatorEnumeration1
from scap.signature import Signature

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class TestType:
    """The base type of every test includes an optional notes element and several
    attributes.

    The notes section of a test should be used to hold information that
    might be helpful to someone examining the technical aspects of the
    test. For example, why certain values have been used by the test, or
    maybe a link to where further information can be found. Please refer
    to the description of the NotesType complex type for more
    information about the notes element. The required comment attribute
    provides a short description of the test. The optional deprecated
    attribute signifies that an id is no longer to be used or referenced
    but the information has been kept around for historic purposes. The
    required id attribute uniquely identifies each test, and must
    conform to the format specified by the TestIdPattern simple type.
    The required version attribute holds the current version of the
    test. Versions are integers, starting at 1 and incrementing every
    time a test is modified. The optional check_existence attribute
    specifies how many items in the set defined by the OVAL Object must
    exist for the test to evaluate to true. The default value for this
    attribute is 'at_least_one_exists' indicating that by default the
    test may evaluate to true if at least one item defined by the OVAL
    Object exists on the system. For example, if a value of 'all_exist'
    is given, every item defined by the OVAL Object must exist on the
    system for the test to evaluate to true. If the OVAL Object uses a
    variable reference, then every value of that variable must exist.
    Note that a pattern match defines a unique set of matching items
    found on a system. So when check_existence = 'all_exist' and a regex
    matches anything on a system the test will evaluate to true (since
    all matching objects on the system were found on the system). When
    check_existence = 'all_exist' and a regex does not match anything on
    a system the test will evaluate to false. The required check
    attribute specifies how many items in the set defined by the OVAL
    Object (ignoring items with a status of Does Not Exist) must satisfy
    the state requirements.  For example, should the test check that all
    matching files have a specified version or that at least one file
    has the specified version?  The valid check values are explained in
    the description of the CheckEnumeration simple type. Note that if
    the test does not contain any references to OVAL States, then the
    check attribute has no meaning and can be ignored during evaluation.
    An OVAL Test evaluates to true if both the check_existence  and
    check attributes are satisfied during evaluation. The evaluation
    result for a test is determined by first evaluating the
    check_existence attribute. If the result of evaluating the
    check_existence attribute is true then the check attribute is
    evaluated. An interpreter may choose to always evaluate both the
    check_existence and the check attributes, but once the
    check_existence attribute evaluation has resulted in false the
    overall test result after evaluating the check attribute will not be
    affected. The optional state_operator attribute provides the logical
    operator that combines the evaluation results from each referenced
    state on a per item basis.  Each matching item is compared to each
    referenced state. The result of comparing each state to a single
    item is combined based on the specified state_operator value to
    determine one result for each item. Finally, the results for each
    item are combined based on the specified check value.  Note that if
    the test does not contain any references to OVAL States, then the
    state_operator attribute has no meaning and can be ignored during
    evaluation. Referencing multiple states in one test allows ranges of
    possible values to be expressed. For example, one state can check
    that a value greater than 8 is found and another state can check
    that a value of less than 16 is found.  In this example the
    referenced states are combined with a state_operator = 'AND'
    indicating that the conditions of all referenced states must be
    satisfied and that the value must be between 8 AND 16.  The valid
    state_operation values are explained in the description of the
    OperatorEnumeration simple type.
    """
    def generate_check(self, data):
        print(f"Recursively generating the check for the test {self.id}")
        print("Generic test detected! Unimplemented!!")

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
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:tst:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: ExistenceEnumeration = field(
        default=ExistenceEnumeration.AT_LEAST_ONE_EXISTS,
        metadata={
            "type": "Attribute",
        },
    )
    check: Optional[CheckEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: OperatorEnumeration1 = field(
        default=OperatorEnumeration1.AND,
        metadata={
            "type": "Attribute",
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
