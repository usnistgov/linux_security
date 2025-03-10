from dataclasses import dataclass

from scap.definition_type import DefinitionType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Definition(DefinitionType):
    """The definition element represents the globally defined element of type
    DefinitionType.

    For more information please see the documentation on the
    DefinitionType.
    """

    class Meta:
        name = "definition"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"
