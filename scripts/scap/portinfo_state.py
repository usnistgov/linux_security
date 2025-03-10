from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType
from scap.version_datatype_2 import VersionDatatype2

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#freebsd"


@dataclass
class PortinfoState(StateType):
    """The portinfo_state element defines the different information that can be
    used to evaluate the specified package.

    This includes the name, category, version, vendor, and description.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar pkginst:
    :ivar name: The name of a package.
    :ivar category:
    :ivar version: The version of a package.
    :ivar vendor:
    :ivar description:
    """

    class Meta:
        name = "portinfo_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#freebsd"
        )

    pkginst: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["PortinfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    vendor: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    description: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype2 = field(
            default=VersionDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )
