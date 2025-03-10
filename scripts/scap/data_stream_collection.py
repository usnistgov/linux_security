from dataclasses import dataclass, field
from typing import Optional

from scap.component import Component
from scap.data_stream import DataStream
from scap.extended_component import ExtendedComponent
from scap.signature import Signature

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class DataStreamCollection:
    """
    Holds a collection of data streams and components.

    :ivar data_stream:
    :ivar component:
    :ivar extended_component:
    :ivar signature: A digital signature of a data stream.
    :ivar id: This MUST be a globally unique ID.
    :ivar schematron_version: The version of the requirements Schematron
        ruleset to which the instance conforms.
    """

    class Meta:
        name = "data-stream-collection"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    data_stream: list[DataStream] = field(
        default_factory=list,
        metadata={
            "name": "data-stream",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    component: list[Component] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    extended_component: list[ExtendedComponent] = field(
        default_factory=list,
        metadata={
            "name": "extended-component",
            "type": "Element",
        },
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"scap_[^_]+_collection_.+",
        },
    )
    schematron_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schematron-version",
            "type": "Attribute",
            "required": True,
        },
    )
