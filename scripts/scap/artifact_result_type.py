from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.binary_artifact_value import BinaryArtifactValue
from scap.reference_artifact_value import ReferenceArtifactValue
from scap.text_artifact_value import TextArtifactValue
from scap.user_type import UserType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactResultType:
    """
    The ArtifactResultType type defines structures containing information about the
    submitted artifact, its value, who provided and submitted it, and when it was
    submitted.

    :ivar reference_artifact_value:
    :ivar binary_artifact_value:
    :ivar text_artifact_value:
    :ivar provider: The provider element contains information about the
        user or system that provided the artifact.
    :ivar submitter: The submitter element contains information about
        the user who submitted the artifact.
    :ivar artifact_ref: The artifact_ref holds the unique identifier of
        the artifact object that describes what the artifact is about,
        the type of data it holds, and other metadata.
    :ivar timestamp: The timestamp attribute holds the date and time
        when the artifact was collected.
    """

    reference_artifact_value: Optional[ReferenceArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    binary_artifact_value: Optional[BinaryArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    text_artifact_value: Optional[TextArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    provider: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:user:[1-9][0-9]*|ocil:[A-Za-z0-9_\-\.]+:system:[1-9][0-9]*",
        },
    )
    submitter: Optional[UserType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    artifact_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:artifact:[1-9][0-9]*",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
