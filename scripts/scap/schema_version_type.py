from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class SchemaVersionType:
    """
    The core version MUST match on all platform schema versions.

    :ivar value:
    :ivar platform: The platform attribute is available to indicate the
        URI of the target namespace for any platform extension being
        included. This platform attribute is to be omitted when
        specifying the core schema version.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]+\.[0-9]+(\.[0-9]+)?(:[0-9]+\.[0-9]+(\.[0-9]+)?)?",
        },
    )
    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
