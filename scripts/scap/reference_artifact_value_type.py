from dataclasses import dataclass, field
from typing import Optional

from scap.artifact_value_type import ArtifactValueType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ReferenceArtifactValueType(ArtifactValueType):
    """
    The data model that references external artifacts.

    :ivar reference: The reference element contains a URI, which is a
        pointer to the location of an artifact.
    """

    reference: Optional["ReferenceArtifactValueType.Reference"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )

    @dataclass
    class Reference:
        """
        :ivar href: The href attribute specifies a URI provided by the
            user.
        """

        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
