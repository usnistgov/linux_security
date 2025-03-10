from dataclasses import dataclass, field

from scap.artifact_result_type import ArtifactResultType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactResultsType:
    """
    The ArtifactResultsType type defines structures containing a set of
    artifact_result elements.

    :ivar artifact_result: The artifact_result element contains an
        artifact, its value, who submitted it, and who provided it.
    """

    artifact_result: list[ArtifactResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
