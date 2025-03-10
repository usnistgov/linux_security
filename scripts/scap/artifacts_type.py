from dataclasses import dataclass, field

from scap.artifact_type import ArtifactType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactsType:
    """
    The ArtifactsType type defines structures containing a set of artifact
    elements.

    :ivar artifact: An artifact element holds information about an
        artifact, which is evidence supporting an answer. Examples
        include a file or submitted text.
    """

    artifact: list[ArtifactType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
