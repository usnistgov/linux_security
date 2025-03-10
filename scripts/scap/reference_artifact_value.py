from dataclasses import dataclass

from scap.reference_artifact_value_type import ReferenceArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ReferenceArtifactValue(ReferenceArtifactValueType):
    """
    The reference_artifact_value element contains a reference to the location of an
    artifact.
    """

    class Meta:
        name = "reference_artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
