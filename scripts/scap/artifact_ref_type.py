from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactRefType:
    """
    The ArtifactRefType type defines a single artifact reference that may be
    collected as part of a questionnaire assessment.

    :ivar idref: The identifier of a referenced artifact.
    :ivar required: The required element specifies whether the artifact
        must be included or not. If true, then it must be included. The
        questionnaire is not considered complete without it. Otherwise,
        it is desired but not necessary.
    """

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:artifact:[1-9][0-9]*",
        },
    )
    required: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
