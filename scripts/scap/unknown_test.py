from dataclasses import dataclass

from scap.test_type import TestType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class UnknownTest(TestType):
    """An unknown_test acts as a placeholder for tests whose implementation is
    unknown.

    This test always evaluates to a result of 'unknown'. Any information
    that is known about the test should be held in the notes child
    element that is available through the extension of the abstract test
    element. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. Note that for an unknown_test, the required
    check attribute that is part of the extended TestType should be
    ignored during evaluation and hence can be set to any valid value.
    """

    class Meta:
        name = "unknown_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )
