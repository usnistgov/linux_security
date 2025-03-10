from dataclasses import dataclass, field

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestActionRefType:
    """
    The TestActionRefType type defines a structure that holds a reference (id) to a
    test_action or questionnaire.

    :ivar value:
    :ivar negate: The negate attribute can be used to specify whether to
        toggle the result from PASS to FAIL, and vice versa. A result
        other than PASS or FAIL (e.g. ERROR, NOT_TESTED) will be
        unchanged by a negate operation.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:testaction:[1-9][0-9]*|ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
