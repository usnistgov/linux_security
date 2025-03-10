from dataclasses import dataclass, field
from typing import Optional

from scap.embedded_artifact_value_type import EmbeddedArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TextArtifactValueType(EmbeddedArtifactValueType):
    """
    The data model that holds text-based artifacts.

    :ivar data: The data element contains the text of an artifact that
        was provided as a text file or a block of text.
    """

    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
