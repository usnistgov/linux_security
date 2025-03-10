from dataclasses import dataclass, field
from typing import Optional

from scap.catalog import Catalog
from scap.type_type import TypeType

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

    catalog: Optional[Catalog] = field(
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
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
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
