from dataclasses import dataclass

from scap.external_variable_type import ExternalVariableType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ExternalVariable2(ExternalVariableType):
    """
    An external_variable element is a variable defined elsewhere (an external
    source).
    """

    class Meta:
        name = "external_variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
