from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType
from scap.version_datatype_1 import VersionDatatype1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class SlackwarepkginfoState(StateType):
    """The slackwarepkginfo_state element defines the different information that
    can be used to evaluate the specified package.

    This includes the version, architecture, and revision. Please refer
    to the individual elements in the schema for more details about what
    each represents.

    :ivar name: This is the package name to check.
    :ivar version: This is the version number of the package.
    :ivar architecture:
    :ivar revision:
    """

    class Meta:
        name = "slackwarepkginfo_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["SlackwarepkginfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    architecture: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    revision: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype1 = field(
            default=VersionDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )
