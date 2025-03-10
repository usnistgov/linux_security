from dataclasses import dataclass, field
from typing import Optional

from scap.artifact_value_type import ArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class EmbeddedArtifactValueType(ArtifactValueType):
    """
    The base data structure that holds artifact values that are embedded into the
    results model.

    :ivar mime_type: The MIME type of the embedded content.  Since the
        list of MIME types are continually expanding, this schema does
        not make an attempt to constrain the allowed values.
    """

    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
