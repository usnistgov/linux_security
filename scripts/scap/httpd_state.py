from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_string_type import EntityStateStringType
from scap.entity_state_version_type import EntityStateVersionType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache"


@dataclass
class HttpdState(StateType):
    """
    The httpd_state element defines information associated with a specific httpd
    binary.

    :ivar path: The path element specifies the directory component of
        the absolute path to a httpd binary on the system.
    :ivar binary_name: The binary_name element specifies the name of the
        file. If the xsi:nil attribute is set to true, then the object
        being specified is the higher level path. In this case, the
        binary_name element should not be collected or used in analysis.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, says to collect every file under a given path.
    :ivar version: The version entity is used to check the version of
        the httpd binary. The datatype for the version entity is
        'version' which means the value should be a delimited set of
        numbers. It is obtained by running 'httpd -v'.
    """

    class Meta:
        name = "httpd_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache"

    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    binary_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    version: Optional[EntityStateVersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
