from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scap.benchmark import Benchmark
from scap.cpe_list import CpeList
from scap.ocil import Ocil
from scap.oval_definitions import OvalDefinitions
from scap.tailoring import Tailoring

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class Component:
    """
    A component that is used by an SCAP data stream.

    :ivar benchmark:
    :ivar oval_definitions:
    :ivar ocil:
    :ivar cpe_list:
    :ivar tailoring:
    :ivar id: This MUST be a globally unique ID.
    :ivar timestamp: The time when the component was created or last
        modified.
    """

    class Meta:
        name = "component"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    benchmark: Optional[Benchmark] = field(
        default=None,
        metadata={
            "name": "Benchmark",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        },
    )
    oval_definitions: Optional[OvalDefinitions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    ocil: Optional[Ocil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    cpe_list: Optional[CpeList] = field(
        default=None,
        metadata={
            "name": "cpe-list",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/dictionary/2.0",
        },
    )
    tailoring: Optional[Tailoring] = field(
        default=None,
        metadata={
            "name": "Tailoring",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"scap_[^_]+_comp_.+",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
