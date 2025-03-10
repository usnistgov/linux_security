from dataclasses import dataclass

from scap.set_expression_pattern_type import SetExpressionPatternType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenPattern(SetExpressionPatternType):
    """The when_pattern element type defines criteria for evaluating the result of
    a numeric or string question result based on a pattern.

    If the pattern matches, the expression must evaluate to TRUE.
    """

    class Meta:
        name = "when_pattern"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
