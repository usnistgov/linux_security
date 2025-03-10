from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class DeprecatedInfoType:
    """The DeprecatedInfoType complex type defines a structure that will be used to
    flag schema-defined constructs as deprecated.

    It holds information related to the version of OVAL when the
    construct was deprecated along with a reason and comment.

    :ivar version: The required version child element details the
        version of OVAL in which the construct became deprecated.
    :ivar reason: The required reason child element is used to provide
        an explanation as to why an item was deprecated and to direct a
        reader to possible alternative structures within OVAL.
    :ivar comment: The optional comment child element is used to supply
        additional information regarding the element's deprecated
        status.
    """

    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
            "pattern": r"[0-9]+\.[0-9]+(\.[0-9]+)?(:[0-9]+\.[0-9]+(\.[0-9]+)?)?",
        },
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
