from dataclasses import dataclass

from scap.test_type import TestType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Test(TestType):
    """The test element is an abstract element that is meant to be extended (via
    substitution groups) by the individual tests found in the component schemas.

    An OVAL Test is used to compare an object(s) against a defined
    state. An actual test element is not valid. The use of this abstract
    class simplifies the OVAL schema by allowing individual tests to
    inherit the optional notes child element, and the id and comment
    attributes from the base TestType. Please refer to the description
    of the TestType complex type for more information.
    """

    class Meta:
        name = "test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"
