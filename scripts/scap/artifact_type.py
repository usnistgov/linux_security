from dataclasses import dataclass, field
from typing import Optional

from scap.item_base_type import ItemBaseType
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactType(ItemBaseType):
    """
    The ArtifactType type defines structures containing information about an
    artifact such as title, description, persistence, and if it's required to
    complete an answer to a question.

    :ivar title: The title element holds a short summary or a caption
        about the artifact.
    :ivar description: The description element holds information that
        describes what the artifact is about.
    :ivar id: Each item is required to have a unique identifier that
        conforms to the definition of NCName in the Recommendation
        "Namespaces in XML 1.0", i.e., all XML 1.0 names that do not
        contain colons.
    :ivar persistent: The persistent attribute specifies whether the
        artifact is time sensitive or not. If the value is true, then a
        snapshot or a copy must be kept. Otherwise, a pointer to the
        location of the artifact is enough. The default value is true.
    """

    title: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    description: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:artifact:[1-9][0-9]*",
        },
    )
    persistent: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
