from dataclasses import dataclass, field

from scap.artifact_ref_type import ArtifactRefType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactRefsType:
    """
    The ArtifactRefsType type defines a collection of artifact references that may
    be collected as part of a questionnaire assessment.

    :ivar artifact_ref: A single reference to an artifact.
    """

    artifact_ref: list[ArtifactRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
