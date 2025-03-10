from dataclasses import dataclass, field

from scap.definition import Definition

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class DefinitionsType:
    """The DefinitionsType complex type is a container for one or more definition
    elements.

    Each definition element describes a single OVAL Definition. Please
    refer to the description of the DefinitionType for more information
    about an individual definition.
    """

    definition: list[Definition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
            "min_occurs": 1,
        },
    )
