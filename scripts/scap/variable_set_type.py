from dataclasses import dataclass, field

from scap.when_boolean import WhenBoolean
from scap.when_choice import WhenChoice
from scap.when_pattern import WhenPattern
from scap.when_range import WhenRange

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class VariableSetType:
    """The VariableSetType type defines structures containing information
    describing how to compute a variable value.

    It holds the patterns, choice_refs, range, or boolean values to be
    matched; and the appropriate value to be stored on the variable
    based on the match.
    """

    when_boolean: list[WhenBoolean] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_range: list[WhenRange] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_choice: list[WhenChoice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_pattern: list[WhenPattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
