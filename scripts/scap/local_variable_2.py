from dataclasses import dataclass

from scap.local_variable_type import LocalVariableType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class LocalVariable2(LocalVariableType):
    """A local_variable element holds a value defined during evaluation.

    It will try to match and set the value based on the answer to a
    question.
    """

    class Meta:
        name = "local_variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
