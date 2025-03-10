from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class CriterionType:
    """The CriterionType complex type identifies a specific test to be included in
    the definition's criteria.

    The required test_ref attribute is the actual id of the test being
    referenced. The optional negate attribute signifies that the result
    of an individual test should be negated during analysis. For
    example, consider a test that evaluates to TRUE if a specific patch
    is installed. By negating this test, it now evaluates to TRUE if the
    patch is NOT installed. The optional comment attribute provides a
    short description of the specified test and should mirror the
    comment attribute of the actual test. The optional
    applicability_check attribute provides a Boolean flag that when true
    indicates that the criterion is being used to determine whether the
    OVAL Definition applies to a given system.
    """

    def generate_check(self, data):
        print(f"Recursively generating the check for criterion {self.comment}")
        #print(f"Test ref: {self.test_ref}")
        return data["tests"][self.test_ref].generate_check(data)
        

    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    test_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:tst:[1-9][0-9]*",
        },
    )
    negate: bool = field(
        default=False,
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
