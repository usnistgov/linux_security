from dataclasses import dataclass

from scap.text_artifact_value_type import TextArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TextArtifactValue(TextArtifactValueType):
    """
    The text_artifact_value element contains an artifact that was provided as a
    text file or a block of text.
    """

    class Meta:
        name = "text_artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
