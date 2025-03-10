from dataclasses import dataclass

from scap.artifact_value_type import ArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactValue(ArtifactValueType):
    """
    The artifact_value element contains either a piece of artifact data itself or a
    pointer to it.
    """

    class Meta:
        name = "artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
