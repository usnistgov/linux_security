from dataclasses import dataclass, field

from scap.component_ref import ComponentRef

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class RefListType:
    class Meta:
        name = "refListType"

    component_ref: list[ComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "component-ref",
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/scap/source/1.2",
            "min_occurs": 1,
        },
    )
