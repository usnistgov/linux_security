from dataclasses import dataclass

from scap.set_expression_range_type import SetExpressionRangeType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenRange(SetExpressionRangeType):
    """The when_range element type defines criteria for evaluating the result of a
    numeric question result based on the answer selected.

    If the answer is within the range (inclusive), the expression must
    evaluate to TRUE.
    """

    class Meta:
        name = "when_range"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
