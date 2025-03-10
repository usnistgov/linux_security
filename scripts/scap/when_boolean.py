from dataclasses import dataclass

from scap.set_expression_boolean_type import SetExpressionBooleanType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenBoolean(SetExpressionBooleanType):
    """The when_boolean element type defines criteria for evaluating the result of
    a boolean question result based on the answer selected.

    If the answer matches, the expression must evaluate to TRUE.
    """

    class Meta:
        name = "when_boolean"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
