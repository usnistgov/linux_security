from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from oval.definitions.cpe_dictionary_2_3 import CpeList
from oval.definitions.oval_definitions_schema import OvalDefinitions
from oval.definitions.xccdf_1_2 import (
    Benchmark,
    Tailoring,
)
from oval.definitions.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


@dataclass
class ComponentRef:
    """
    An XLink element that points to a component.

    :ivar catalog:
    :ivar id: This MUST be a globally unique ID.
    :ivar type_value:
    :ivar href:
    """

    class Meta:
        name = "component-ref"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    catalog: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:entity:xmlns:xml:catalog",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"scap_[^_]+_cref_.+",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )


@dataclass
class ContentSourceType:
    class Meta:
        name = "contentSourceType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExtendedComponent:
    """
    A component that holds non-standard SCAP content.

    :ivar other_element:
    :ivar id: This MUST be a globally unique ID.
    :ivar timestamp: The time when the component was created or last
        modified.
    """

    class Meta:
        name = "extended-component"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"scap_[^_]+_ecomp_.+",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class ScapVersionType(Enum):
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"
    VALUE_1_2 = "1.2"
    VALUE_1_3 = "1.3"


class UseCaseType(Enum):
    CONFIGURATION = "CONFIGURATION"
    VULNERABILITY = "VULNERABILITY"
    INVENTORY = "INVENTORY"
    OTHER = "OTHER"


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
    ocil: Optional[str] = field(
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


@dataclass
class RefListType:
    class Meta:
        name = "refListType"

    component_ref: list[ComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "component-ref",
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/scap/source/1.2",
            "min_occurs": 1,
        },
    )


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
        name = "data_stream"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    dictionaries: Optional[RefListType] = field(
        default=None,
        metadata={
            "name":"dictionaries",
            "type": "Element",
            "namespace": "",
        },
    )
    checklists: Optional[RefListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    checks: Optional[RefListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    extended_components: Optional[RefListType] = field(
        default=None,
        metadata={
            "name": "extended-components",
            "type": "Element",
            "namespace": "",
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
            "name": "data_stream",
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
