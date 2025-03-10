from dataclasses import dataclass

from scap.set_expression_choice_type import SetExpressionChoiceType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenChoice(SetExpressionChoiceType):
    """The when_choice element type defines criteria for evaluating the result of a
    choice question result based on the answer selected.

    If the choice_ref matches identifier of the selected choice, the
    expression must evaluate to TRUE.
    """

    class Meta:
        name = "when_choice"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
