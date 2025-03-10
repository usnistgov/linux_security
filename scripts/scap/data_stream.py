from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from scap.ref_list_type import RefListType
from scap.scap_version_type import ScapVersionType
from scap.use_case_type import UseCaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class DataStream:
    """
    An SCAP data stream containing pointers to all of the components composing the
    data stream.

    :ivar dictionaries: Holds pointers to dictionary components.
    :ivar checklists: Holds pointers to checklist components.
    :ivar checks: Holds pointers to check components.
    :ivar extended_components: Holds pointers to non-standard SCAP
        components captured as extended-component elements.
    :ivar id: This MUST be a globally unique ID.
    :ivar use_case: The SCAP capability being expressed by this data
        stream. The type is expressed to allow for future use of this
        schema while indicating the currently acceptable values.
    :ivar scap_version: The version of SCAP expressed by this data
        stream. The type is expressed to allow for future use of this
        schema while indicating the currently acceptable values.
    :ivar timestamp: The time when the data stream was created or last
        modified.
    """

    class Meta:
        name = "data-stream"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    dictionaries: Optional[RefListType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    checklists: Optional[RefListType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    checks: Optional[RefListType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "required": True,
        },
    )
    extended_components: Optional[RefListType] = field(
        default=None,
        metadata={
            "name": "extended-components",
            "type": "Element",
            
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"scap_[^_]+_datastream_.+",
        },
    )
    use_case: Optional[Union[UseCaseType, str]] = field(
        default=None,
        metadata={
            "name": "use-case",
            "type": "Attribute",
            "required": True,
        },
    )
    scap_version: Optional[Union[ScapVersionType, str]] = field(
        default=None,
        metadata={
            "name": "scap-version",
            "type": "Attribute",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
