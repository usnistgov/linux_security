from dataclasses import dataclass, field
from typing import Optional

from scap.embedded_artifact_value_type import EmbeddedArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BinaryArtifactValueType(EmbeddedArtifactValueType):
    """
    The data model that holds binary data-based artifacts.

    :ivar data: The data element contains a binary file, which was
        provided as an artifact.
    """

    data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "format": "base64",
        },
    )
