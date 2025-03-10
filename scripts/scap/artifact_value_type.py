from dataclasses import dataclass

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactValueType:
    """
    The ArtifactValueType type defines structures containing either the artifact
    data itself or a pointer to it.
    """
