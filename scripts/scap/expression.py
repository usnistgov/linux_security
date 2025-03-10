from dataclasses import dataclass

from scap.set_expression_base_type import SetExpressionBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Expression(SetExpressionBaseType):
    """
    The expression element provides a substitution for a variety of expressions
    that can be used to compute a variable value.
    """

    class Meta:
        name = "expression"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
