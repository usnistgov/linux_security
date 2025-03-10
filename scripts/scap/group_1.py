from dataclasses import dataclass, field
from typing import Optional

from scap.delegate_public import DelegatePublic
from scap.delegate_system import DelegateSystem
from scap.delegate_uri import DelegateUri
from scap.next_catalog import NextCatalog
from scap.public import Public
from scap.rewrite_system import RewriteSystem
from scap.rewrite_uri import RewriteUri
from scap.system_1 import System1
from scap.system_or_public import SystemOrPublic
from scap.system_suffix import SystemSuffix
from scap.uri import Uri
from scap.uri_suffix import UriSuffix

__NAMESPACE__ = "urn:oasis:names:tc:entity:xmlns:xml:catalog"


@dataclass
class Group1:
    class Meta:
        name = "group"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    public: list[Public] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    system: list[System1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rewrite_system: list[RewriteSystem] = field(
        default_factory=list,
        metadata={
            "name": "rewriteSystem",
            "type": "Element",
        },
    )
    rewrite_uri: list[RewriteUri] = field(
        default_factory=list,
        metadata={
            "name": "rewriteURI",
            "type": "Element",
        },
    )
    uri_suffix: list[UriSuffix] = field(
        default_factory=list,
        metadata={
            "name": "uriSuffix",
            "type": "Element",
        },
    )
    system_suffix: list[SystemSuffix] = field(
        default_factory=list,
        metadata={
            "name": "systemSuffix",
            "type": "Element",
        },
    )
    delegate_public: list[DelegatePublic] = field(
        default_factory=list,
        metadata={
            "name": "delegatePublic",
            "type": "Element",
        },
    )
    delegate_system: list[DelegateSystem] = field(
        default_factory=list,
        metadata={
            "name": "delegateSystem",
            "type": "Element",
        },
    )
    delegate_uri: list[DelegateUri] = field(
        default_factory=list,
        metadata={
            "name": "delegateURI",
            "type": "Element",
        },
    )
    next_catalog: list[NextCatalog] = field(
        default_factory=list,
        metadata={
            "name": "nextCatalog",
            "type": "Element",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        },
    )
    prefer: Optional[SystemOrPublic] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
