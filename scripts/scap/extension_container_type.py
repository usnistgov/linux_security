from dataclasses import dataclass, field

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ExtensionContainerType:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
