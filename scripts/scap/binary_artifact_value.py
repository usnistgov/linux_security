from dataclasses import dataclass

from scap.binary_artifact_value_type import BinaryArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BinaryArtifactValue(BinaryArtifactValueType):
    """
    The binary_artifact_value element contains an artifact that was provided as a
    binary file.
    """

    class Meta:
        name = "binary_artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
