from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod


@dataclass
class CheckContentRef:
    class Meta:
        name = "check-content-ref"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CheckExport:
    class Meta:
        name = "check-export"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    export_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "export-name",
            "type": "Attribute",
            "required": True,
        },
    )
    value_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "value-id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Conflicts:
    class Meta:
        name = "conflicts"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Ident:
    class Meta:
        name = "ident"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Metadata:
    class Meta:
        name = "metadata"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    publisher: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "required": True,
        },
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "required": True,
        },
    )
    contributor: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "min_occurs": 1,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "required": True,
        },
    )


@dataclass
class Notice:
    class Meta:
        name = "notice"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Platform:
    class Meta:
        name = "platform"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Reference:
    class Meta:
        name = "reference"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Union[str, XmlPeriod, float, int, Decimal] = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class RefineRule:
    class Meta:
        name = "refine-rule"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    severity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RefineValue:
    class Meta:
        name = "refine-value"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    selector: Optional[Union[str, int, XmlPeriod]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Requires:
    class Meta:
        name = "requires"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Select:
    class Meta:
        name = "select"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Status:
    class Meta:
        name = "status"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Sub:
    class Meta:
        name = "sub"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Title:
    class Meta:
        name = "title"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    override: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Value2:
    class Meta:
        name = "value"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    selector: Optional[Union[str, int, XmlPeriod]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Union[int, str, bool, XmlPeriod] = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Version:
    class Meta:
        name = "version"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    update: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Check:
    class Meta:
        name = "check"
        namespace = "http://cpe.mitre.org/dictionary/2.0"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Title:
    class Meta:
        name = "title"
        namespace = "http://cpe.mitre.org/dictionary/2.0"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class CheckFactRef:
    class Meta:
        name = "check-fact-ref"
        namespace = "http://cpe.mitre.org/language/2.0"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Behaviors:
    class Meta:
        name = "behaviors"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    singleline: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    multiline: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max_depth: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FamilyObject:
    class Meta:
        name = "family_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FamilyState:
    class Meta:
        name = "family_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    family: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Filehash58Object:
    class Meta:
        name = "filehash58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    hash_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Filehash58State:
    class Meta:
        name = "filehash58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    hash_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Filename:
    class Meta:
        name = "filename"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Filepath:
    class Meta:
        name = "filepath"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Instance:
    class Meta:
        name = "instance"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[int] = field(default=None)
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Object:
    class Meta:
        name = "object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Path:
    class Meta:
        name = "path"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Pattern:
    class Meta:
        name = "pattern"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Pid:
    class Meta:
        name = "pid"
        nillable = True
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class State:
    class Meta:
        name = "state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    state_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Subexpression:
    class Meta:
        name = "subexpression"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    entity_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Union[float, int, str, bool] = field(default="")


@dataclass
class Text:
    class Meta:
        name = "text"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Union[str, int] = field(default="")


@dataclass
class Value:
    class Meta:
        name = "value"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Union[int, str] = field(default="")


@dataclass
class Arch:
    class Meta:
        name = "arch"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Behaviors:
    class Meta:
        name = "behaviors"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    nolinkto: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nomd5: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nosize: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nouser: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nogroup: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nomtime: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nomode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nordev: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    noghostfiles: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max_depth: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ConfigurationFile:
    class Meta:
        name = "configuration_file"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class CurrentStatus:
    class Meta:
        name = "current_status"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Dependency:
    class Meta:
        name = "dependency"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    entity_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Device:
    class Meta:
        name = "device"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    entity_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class DpkginfoObject:
    class Meta:
        name = "dpkginfo_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Epoch:
    class Meta:
        name = "epoch"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Evr:
    class Meta:
        name = "evr"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Filename:
    class Meta:
        name = "filename"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Filepath:
    class Meta:
        name = "filepath"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class GhostFile:
    class Meta:
        name = "ghost_file"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class LocalAddress:
    class Meta:
        name = "local_address"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class LocalPort:
    class Meta:
        name = "local_port"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MountOptions:
    class Meta:
        name = "mount_options"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    entity_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(default="")
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MountPoint:
    class Meta:
        name = "mount_point"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Object:
    class Meta:
        name = "object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Path:
    class Meta:
        name = "path"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PendingStatus:
    class Meta:
        name = "pending_status"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Release:
    class Meta:
        name = "release"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class RpminfoObject:
    class Meta:
        name = "rpminfo_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SelinuxbooleanObject:
    class Meta:
        name = "selinuxboolean_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class State:
    class Meta:
        name = "state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    state_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SystemdunitdependencyObject:
    class Meta:
        name = "systemdunitdependency_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Type:
    class Meta:
        name = "type"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Unit:
    class Meta:
        name = "unit"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Version:
    class Meta:
        name = "version"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Behaviors:
    class Meta:
        name = "behaviors"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    recurse: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    max_depth: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_file_system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CanonicalPath:
    class Meta:
        name = "canonical_path"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ChgReq:
    class Meta:
        name = "chg_req"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CommandLine:
    class Meta:
        name = "command_line"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class EncryptMethod:
    class Meta:
        name = "encrypt_method"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Filename:
    class Meta:
        name = "filename"
        nillable = True
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Filepath:
    class Meta:
        name = "filepath"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Flag:
    class Meta:
        name = "flag"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    entity_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Gexec:
    class Meta:
        name = "gexec"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Gread:
    class Meta:
        name = "gread"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class GroupId:
    class Meta:
        name = "group_id"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[int] = field(default=None)
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Gwrite:
    class Meta:
        name = "gwrite"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class HasExtendedAcl:
    class Meta:
        name = "has_extended_acl"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class HomeDir:
    class Meta:
        name = "home_dir"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class LoginShell:
    class Meta:
        name = "login_shell"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class MTime:
    class Meta:
        name = "m_time"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Object:
    class Meta:
        name = "object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Oexec:
    class Meta:
        name = "oexec"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Oread:
    class Meta:
        name = "oread"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Owrite:
    class Meta:
        name = "owrite"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Password:
    class Meta:
        name = "password"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    mask: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Path:
    class Meta:
        name = "path"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")


@dataclass
class Pid:
    class Meta:
        name = "pid"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ProcessorType:
    class Meta:
        name = "processor_type"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Sgid:
    class Meta:
        name = "sgid"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Size:
    class Meta:
        name = "size"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class State:
    class Meta:
        name = "state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    state_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Sticky:
    class Meta:
        name = "sticky"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Suid:
    class Meta:
        name = "suid"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class SysctlObject:
    class Meta:
        name = "sysctl_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Type:
    class Meta:
        name = "type"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Uexec:
    class Meta:
        name = "uexec"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class UnameObject:
    class Meta:
        name = "uname_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Uread:
    class Meta:
        name = "uread"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class UserId:
    class Meta:
        name = "user_id"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[int] = field(default=None)
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Username:
    class Meta:
        name = "username"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(default="")
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    var_check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Uwrite:
    class Meta:
        name = "uwrite"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Union[int, str] = field(default="")
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Affected:
    class Meta:
        name = "affected"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    family: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConstantVariable:
    class Meta:
        name = "constant_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Criterion:
    class Meta:
        name = "criterion"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    negate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    test_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExtendDefinition:
    class Meta:
        name = "extend_definition"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    negate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ExternalVariable:
    class Meta:
        name = "external_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Filter:
    class Meta:
        name = "filter"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    action: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Generator:
    class Meta:
        name = "generator"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
            "required": True,
        },
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
            "required": True,
        },
    )
    schema_version: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
            "required": True,
        },
    )


@dataclass
class LiteralComponent:
    class Meta:
        name = "literal_component"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Union[int, str] = field(default="")


@dataclass
class ObjectComponent:
    class Meta:
        name = "object_component"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    item_field: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Reference:
    class Meta:
        name = "reference"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class VariableComponent:
    class Meta:
        name = "variable_component"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Actions:
    class Meta:
        name = "actions"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    test_action_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BooleanQuestion:
    class Meta:
        name = "boolean_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    question_text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Generator:
    class Meta:
        name = "generator"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    schema_version: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WhenFalse:
    class Meta:
        name = "when_false"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WhenTrue:
    class Meta:
        name = "when_true"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "http://www.w3.org/1999/xhtml"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class P:
    class Meta:
        name = "p"
        namespace = "http://www.w3.org/1999/xhtml"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "code",
                    "type": ForwardRef("P.Code"),
                },
                {
                    "type": ForwardRef("P.Value"),
                },
            ),
        },
    )

    @dataclass
    class Code:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Uri:
    class Meta:
        name = "uri"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Check:
    class Meta:
        name = "check"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_export: list[CheckExport] = field(
        default_factory=list,
        metadata={
            "name": "check-export",
            "type": "Element",
        },
    )
    check_content_ref: Optional[CheckContentRef] = field(
        default=None,
        metadata={
            "name": "check-content-ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Fix:
    class Meta:
        name = "fix"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    complexity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    disruption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reboot: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    strategy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "type": str,
                },
            ),
        },
    )


@dataclass
class FrontMatter:
    class Meta:
        name = "front-matter"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "type": str,
                },
            ),
        },
    )


@dataclass
class CpeItem:
    class Meta:
        name = "cpe-item"
        namespace = "http://cpe.mitre.org/dictionary/2.0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    check: Optional[Check] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicalTest:
    class Meta:
        name = "logical-test"
        namespace = "http://cpe.mitre.org/language/2.0"

    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    negate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    logical_test: list["LogicalTest"] = field(
        default_factory=list,
        metadata={
            "name": "logical-test",
            "type": "Element",
        },
    )
    check_fact_ref: list[CheckFactRef] = field(
        default_factory=list,
        metadata={
            "name": "check-fact-ref",
            "type": "Element",
        },
    )


@dataclass
class Environmentvariable58Object:
    class Meta:
        name = "environmentvariable58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    pid: Optional[Pid] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Environmentvariable58State:
    class Meta:
        name = "environmentvariable58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[Union[Value, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Environmentvariable58Test:
    class Meta:
        name = "environmentvariable58_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FamilyTest:
    class Meta:
        name = "family_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Filehash58Test:
    class Meta:
        name = "filehash58_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Textfilecontent54State:
    class Meta:
        name = "textfilecontent54_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    text: Optional[Text] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    instance: Optional[Instance] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subexpression: Optional[Union[Subexpression, str, int]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pattern: Optional[Pattern] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filename: Optional[Filename] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filepath: Optional[Filepath] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Textfilecontent54Test:
    class Meta:
        name = "textfilecontent54_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: list[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class VariableState:
    class Meta:
        name = "variable_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[Union[Value, int]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VariableTest:
    class Meta:
        name = "variable_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class XmlfilecontentObject:
    class Meta:
        name = "xmlfilecontent_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filename: Optional[Filename] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class XmlfilecontentTest:
    class Meta:
        name = "xmlfilecontent_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DpkginfoState:
    class Meta:
        name = "dpkginfo_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    evr: Optional[Evr] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DpkginfoTest:
    class Meta:
        name = "dpkginfo_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InetlisteningserversObject:
    class Meta:
        name = "inetlisteningservers_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    local_address: Optional[LocalAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    local_port: Optional[LocalPort] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
            "min_occurs": 1,
        },
    )


@dataclass
class InetlisteningserversState:
    class Meta:
        name = "inetlisteningservers_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    local_port: Optional[LocalPort] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    local_address: Optional[LocalAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InetlisteningserversTest:
    class Meta:
        name = "inetlisteningservers_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PartitionObject:
    class Meta:
        name = "partition_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    mount_point: Optional[Union[MountPoint, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class PartitionState:
    class Meta:
        name = "partition_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    device: Optional[Device] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mount_options: Optional[MountOptions] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class PartitionTest:
    class Meta:
        name = "partition_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RpminfoState:
    class Meta:
        name = "rpminfo_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "version",
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: Optional[Union[str, Version]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    evr: Optional[Evr] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RpminfoTest:
    class Meta:
        name = "rpminfo_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RpmverifyfileObject:
    class Meta:
        name = "rpmverifyfile_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "version",
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    behaviors: Optional[Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    epoch: Optional[Epoch] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    release: Optional[Release] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arch: Optional[Arch] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filepath: Optional[Filepath] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class RpmverifyfileState:
    class Meta:
        name = "rpmverifyfile_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    md5_differs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    configuration_file: Optional[ConfigurationFile] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ghost_file: Optional[GhostFile] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ownership_differs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    group_differs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mode_differs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RpmverifyfileTest:
    class Meta:
        name = "rpmverifyfile_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SelinuxbooleanState:
    class Meta:
        name = "selinuxboolean_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    current_status: Optional[CurrentStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pending_status: Optional[PendingStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SelinuxbooleanTest:
    class Meta:
        name = "selinuxboolean_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SelinuxsecuritycontextObject:
    class Meta:
        name = "selinuxsecuritycontext_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    behaviors: Optional[Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    path: Optional[Union[str, Path]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filename: Optional[Filename] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filepath: Optional[Filepath] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class SelinuxsecuritycontextState:
    class Meta:
        name = "selinuxsecuritycontext_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[Type] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SelinuxsecuritycontextTest:
    class Meta:
        name = "selinuxsecuritycontext_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SystemdunitdependencyState:
    class Meta:
        name = "systemdunitdependency_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    dependency: Optional[Dependency] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SystemdunitdependencyTest:
    class Meta:
        name = "systemdunitdependency_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SystemdunitpropertyObject:
    class Meta:
        name = "systemdunitproperty_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit: Optional[Union[Unit, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    property: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class SystemdunitpropertyState:
    class Meta:
        name = "systemdunitproperty_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[Union[str, Value]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SystemdunitpropertyTest:
    class Meta:
        name = "systemdunitproperty_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FileObject:
    class Meta:
        name = "file_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    behaviors: Optional[Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    path: Optional[Union[str, Path]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filename: Optional[Union[Filename, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    filepath: Optional[Union[str, Filepath]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class FileState:
    class Meta:
        name = "file_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filename: Optional[Filename] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    group_id: Optional[GroupId] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    user_id: Optional[UserId] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[Union[Type, str]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    suid: Optional[Suid] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sgid: Optional[Sgid] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sticky: Optional[Sticky] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    uread: Optional[Uread] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    uwrite: Optional[Uwrite] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    uexec: Optional[Uexec] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gread: Optional[Gread] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gwrite: Optional[Gwrite] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gexec: Optional[Gexec] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    oread: Optional[Oread] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    owrite: Optional[Owrite] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    oexec: Optional[Oexec] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    has_extended_acl: Optional[HasExtendedAcl] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filepath: Optional[Filepath] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    size: Optional[Size] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    m_time: Optional[MTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class FileTest:
    class Meta:
        name = "file_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: list[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InterfaceObject:
    class Meta:
        name = "interface_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class InterfaceState:
    class Meta:
        name = "interface_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    flag: Optional[Flag] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class InterfaceTest:
    class Meta:
        name = "interface_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PasswordState:
    class Meta:
        name = "password_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    login_shell: Optional[LoginShell] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    username: Optional[Username] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    user_id: Optional[UserId] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    home_dir: Optional[HomeDir] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    password: Optional[Password] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class PasswordTest:
    class Meta:
        name = "password_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Process58Object:
    class Meta:
        name = "process58_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    command_line: Optional[CommandLine] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pid: Optional[Pid] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Process58Test:
    class Meta:
        name = "process58_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ShadowObject:
    class Meta:
        name = "shadow_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    username: Optional[Username] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class ShadowState:
    class Meta:
        name = "shadow_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    password: Optional[Password] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    chg_req: Optional[ChgReq] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    encrypt_method: Optional[EncryptMethod] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ShadowTest:
    class Meta:
        name = "shadow_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SymlinkObject:
    class Meta:
        name = "symlink_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    filepath: Optional[Union[Filepath, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class SymlinkState:
    class Meta:
        name = "symlink_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    canonical_path: Optional[Union[str, CanonicalPath]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SymlinkTest:
    class Meta:
        name = "symlink_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SysctlState:
    class Meta:
        name = "sysctl_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SysctlTest:
    class Meta:
        name = "sysctl_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: list[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class UnameState:
    class Meta:
        name = "uname_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    processor_type: Optional[ProcessorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class UnameTest:
    class Meta:
        name = "uname_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_value: Optional[Object] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "required": True,
        },
    )
    state: Optional[State] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Criteria:
    class Meta:
        name = "criteria"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    negate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    extend_definition: list[ExtendDefinition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    criterion: list[Criterion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    criteria: list["Criteria"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EscapeRegex:
    class Meta:
        name = "escape_regex"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GlobToRegex:
    class Meta:
        name = "glob_to_regex"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Metadata:
    class Meta:
        name = "metadata"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    affected: Optional[Affected] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RegexCapture:
    class Meta:
        name = "regex_capture"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Set:
    class Meta:
        name = "set"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    object_reference: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Split:
    class Meta:
        name = "split"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    delimiter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Substring:
    class Meta:
        name = "substring"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    substring_start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    substring_length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TimeDifference:
    class Meta:
        name = "time_difference"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    format_2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    literal_component: Optional[LiteralComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class BooleanQuestionTestAction:
    class Meta:
        name = "boolean_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    question_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    when_true: Optional[WhenTrue] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    when_false: Optional[WhenFalse] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Questionnaire:
    class Meta:
        name = "questionnaire"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    actions: Optional[Actions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Questions:
    class Meta:
        name = "questions"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    boolean_question: list[BooleanQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/1999/xhtml"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://checklists.nist.gov/xccdf/1.2",
                },
                {
                    "name": "a",
                    "type": A,
                },
            ),
        },
    )


@dataclass
class I:
    class Meta:
        name = "i"
        namespace = "http://www.w3.org/1999/xhtml"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "code",
                    "type": ForwardRef("I.Code"),
                },
                {
                    "type": ForwardRef("I.Value"),
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://checklists.nist.gov/xccdf/1.2",
                },
            ),
        },
    )

    @dataclass
    class Code:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Catalog:
    class Meta:
        name = "catalog"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class CpeList:
    class Meta:
        name = "cpe-list"
        namespace = "http://cpe.mitre.org/dictionary/2.0"

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    cpe_item: list[CpeItem] = field(
        default_factory=list,
        metadata={
            "name": "cpe-item",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Platform:
    class Meta:
        name = "platform"
        namespace = "http://cpe.mitre.org/language/2.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    logical_test: Optional[LogicalTest] = field(
        default=None,
        metadata={
            "name": "logical-test",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Textfilecontent54Object:
    class Meta:
        name = "textfilecontent54_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    behaviors: Optional[Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    path: Optional[Union[Path, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filename: Optional[Filename] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filepath: Optional[Union[Filepath, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pattern: Optional[Pattern] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    instance: Optional[Instance] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class VariableObject:
    class Meta:
        name = "variable_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class PasswordObject:
    class Meta:
        name = "password_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    username: Optional[Username] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class Concat:
    class Meta:
        name = "concat"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    literal_component: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    object_component: list[ObjectComponent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    escape_regex: Optional[EscapeRegex] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    split: list[Split] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    regex_capture: list[RegexCapture] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )


@dataclass
class Definition:
    class Meta:
        name = "definition"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        },
    )
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    criteria: Optional[Criteria] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class States:
    class Meta:
        name = "states"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    textfilecontent54_state: list[Textfilecontent54State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    file_state: list[FileState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    partition_state: list[PartitionState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    variable_state: list[VariableState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    inetlisteningservers_state: list[InetlisteningserversState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    symlink_state: list[SymlinkState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    selinuxsecuritycontext_state: list[SelinuxsecuritycontextState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    shadow_state: list[ShadowState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    password_state: list[PasswordState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    environmentvariable58_state: list[Environmentvariable58State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    interface_state: list[InterfaceState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    rpminfo_state: list[RpminfoState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    filehash58_state: list[Filehash58State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    sysctl_state: list[SysctlState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    rpmverifyfile_state: list[RpmverifyfileState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    selinuxboolean_state: list[SelinuxbooleanState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    systemdunitproperty_state: list[SystemdunitpropertyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    dpkginfo_state: list[DpkginfoState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    systemdunitdependency_state: list[SystemdunitdependencyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    family_state: list[FamilyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    uname_state: list[UnameState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "min_occurs": 1,
            "sequence": 1,
        },
    )


@dataclass
class Tests:
    class Meta:
        name = "tests"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    textfilecontent54_test: list[Textfilecontent54Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    file_test: list[FileTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    variable_test: list[VariableTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    inetlisteningservers_test: list[InetlisteningserversTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    xmlfilecontent_test: list[XmlfilecontentTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    rpminfo_test: list[RpminfoTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    symlink_test: list[SymlinkTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    selinuxsecuritycontext_test: list[SelinuxsecuritycontextTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    shadow_test: list[ShadowTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    password_test: list[PasswordTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    environmentvariable58_test: list[Environmentvariable58Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    interface_test: list[InterfaceTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    dpkginfo_test: list[DpkginfoTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    partition_test: list[PartitionTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    filehash58_test: list[Filehash58Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    process58_test: list[Process58Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    sysctl_test: list[SysctlTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    rpmverifyfile_test: list[RpmverifyfileTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    selinuxboolean_test: list[SelinuxbooleanTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    systemdunitproperty_test: list[SystemdunitpropertyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    systemdunitdependency_test: list[SystemdunitdependencyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    family_test: list[FamilyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    uname_test: list[UnameTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "min_occurs": 1,
            "sequence": 1,
        },
    )


@dataclass
class Unique:
    class Meta:
        name = "unique"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    glob_to_regex: Optional[GlobToRegex] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    regex_capture: Optional[RegexCapture] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Questionnaires:
    class Meta:
        name = "questionnaires"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    questionnaire: list[Questionnaire] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TestActions:
    class Meta:
        name = "test_actions"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    boolean_question_test_action: list[BooleanQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ComponentRef:
    class Meta:
        name = "component-ref"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
    catalog: Optional[Catalog] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:entity:xmlns:xml:catalog",
        },
    )


@dataclass
class Code:
    class Meta:
        name = "code"
        namespace = "http://www.w3.org/1999/xhtml"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "i",
                    "type": ForwardRef("Code.I"),
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://checklists.nist.gov/xccdf/1.2",
                },
                {
                    "type": ForwardRef("Code.Value"),
                },
                {
                    "name": "a",
                    "type": A,
                },
            ),
        },
    )

    @dataclass
    class I:
        value: Optional[Union[str, I]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Pre:
    class Meta:
        name = "pre"
        namespace = "http://www.w3.org/1999/xhtml"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "i",
                    "type": ForwardRef("Pre.I"),
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://checklists.nist.gov/xccdf/1.2",
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "code",
                    "type": ForwardRef("Pre.Code"),
                },
                {
                    "type": ForwardRef("Pre.Value"),
                },
            ),
        },
    )

    @dataclass
    class I:
        value: Optional[Union[str, I]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Code:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class PlatformSpecification:
    class Meta:
        name = "platform-specification"
        namespace = "http://cpe.mitre.org/language/2.0"

    platform: list[Platform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Count:
    class Meta:
        name = "count"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    unique: Optional[Unique] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    regex_capture: Optional[RegexCapture] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Definitions:
    class Meta:
        name = "definitions"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    definition: list[Definition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Objects:
    class Meta:
        name = "objects"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    textfilecontent54_object: list[Textfilecontent54Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    file_object: list[FileObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    partition_object: list[PartitionObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    variable_object: list[VariableObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    inetlisteningservers_object: list[InetlisteningserversObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    xmlfilecontent_object: list[XmlfilecontentObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    rpminfo_object: list[RpminfoObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    symlink_object: list[SymlinkObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    selinuxsecuritycontext_object: list[SelinuxsecuritycontextObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    password_object: list[PasswordObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    shadow_object: list[ShadowObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    environmentvariable58_object: list[Environmentvariable58Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    uname_object: list[UnameObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    interface_object: list[InterfaceObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    rpmverifyfile_object: list[RpmverifyfileObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    filehash58_object: list[Filehash58Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )
    process58_object: list[Process58Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    dpkginfo_object: list[DpkginfoObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    sysctl_object: list[SysctlObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
            "sequence": 1,
        },
    )
    selinuxboolean_object: list[SelinuxbooleanObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    systemdunitproperty_object: list[SystemdunitpropertyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    systemdunitdependency_object: list[SystemdunitdependencyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
            "sequence": 1,
        },
    )
    family_object: list[FamilyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
            "sequence": 1,
        },
    )


@dataclass
class Ocil:
    class Meta:
        name = "ocil"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    generator: Optional[Generator] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    questionnaires: Optional[Questionnaires] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    test_actions: Optional[TestActions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    questions: Optional[Questions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Checklists:
    class Meta:
        name = "checklists"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    component_ref: Optional[ComponentRef] = field(
        default=None,
        metadata={
            "name": "component-ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Checks:
    class Meta:
        name = "checks"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    component_ref: list[ComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "component-ref",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Dictionaries:
    class Meta:
        name = "dictionaries"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    component_ref: Optional[ComponentRef] = field(
        default=None,
        metadata={
            "name": "component-ref",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Li:
    class Meta:
        name = "li"
        namespace = "http://www.w3.org/1999/xhtml"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "code",
                    "type": ForwardRef("Li.Code"),
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Li.Pre"),
                },
                {
                    "type": ForwardRef("Li.Value"),
                },
                {
                    "name": "p",
                    "type": ForwardRef("Li.P"),
                },
                {
                    "name": "b",
                    "type": B,
                },
            ),
        },
    )

    @dataclass
    class Code:
        value: Optional[Union[str, Code, int]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Pre:
        value: Optional[Union[str, Pre]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class P:
        value: Optional[Union[str, P]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Arithmetic:
    class Meta:
        name = "arithmetic"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    arithmetic_operation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    literal_component: Optional[LiteralComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arithmetic: list["Arithmetic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    regex_capture: Optional[RegexCapture] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    count: list[Count] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DataStream:
    class Meta:
        name = "data_stream"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    scap_version: Optional[float] = field(
        default=None,
        metadata={
            "name": "scap-version",
            "type": "Attribute",
            "required": True,
        },
    )
    use_case: Optional[str] = field(
        default=None,
        metadata={
            "name": "use-case",
            "type": "Attribute",
            "required": True,
        },
    )
    dictionaries: Optional[Dictionaries] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    checklists: Optional[Checklists] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    checks: Optional[Checks] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ul:
    class Meta:
        name = "ul"
        namespace = "http://www.w3.org/1999/xhtml"

    li: list[Union[Li, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Description:
    class Meta:
        name = "description"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    override: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "code",
                    "type": ForwardRef("Description.Code"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "b",
                    "type": ForwardRef("Description.B"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "i",
                    "type": ForwardRef("Description.I"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Description.Em"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Description.Pre"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "type": ForwardRef("Description.Value"),
                },
            ),
        },
    )

    @dataclass
    class Code:
        value: Optional[Union[str, Code, int, bool, XmlPeriod]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B:
        value: Optional[Union[str, B]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class I:
        value: Optional[Union[str, I]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Em:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Pre:
        value: Optional[Union[Pre, str]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Rationale:
    class Meta:
        name = "rationale"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "code",
                    "type": ForwardRef("Rationale.Code"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Rationale.Pre"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "type": ForwardRef("Rationale.Value"),
                },
            ),
        },
    )

    @dataclass
    class Code:
        value: Optional[Union[str, Code, int]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Pre:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Warning:
    class Meta:
        name = "warning"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "pre",
                    "type": ForwardRef("Warning.Pre"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Warning.Code"),
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "type": ForwardRef("Warning.Value"),
                },
            ),
        },
    )

    @dataclass
    class Pre:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Code:
        value: Optional[Union[str, float, int]] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Value:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class LocalVariable:
    class Meta:
        name = "local_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    arithmetic: Optional[Arithmetic] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    substring: Optional[Substring] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    regex_capture: Optional[RegexCapture] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variable_component: Optional[VariableComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    object_component: Optional[ObjectComponent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    literal_component: Optional[Union[LiteralComponent, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    unique: Optional[Unique] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    concat: Optional[Concat] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time_difference: Optional[TimeDifference] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    split: Optional[Split] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Profile:
    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[Union[float, str]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    select: list[Select] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    refine_value: list[RefineValue] = field(
        default_factory=list,
        metadata={
            "name": "refine-value",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    refine_rule: list[RefineRule] = field(
        default_factory=list,
        metadata={
            "name": "refine-rule",
            "type": "Element",
        },
    )


@dataclass
class Rule:
    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    severity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Union[Description, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    warning: list[Warning] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rationale: Optional[Union[str, Rationale]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    platform: list[Platform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    requires: Optional[Requires] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conflicts: Optional[Conflicts] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ident: Optional[Ident] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fix: list[Fix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    check: list[Check] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Value1:
    class Meta:
        name = "Value"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    interactive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Union[Description, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    warning: Optional[Warning] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: list[Union[Value2, str, int, bool, XmlPeriod]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Variables:
    class Meta:
        name = "variables"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    external_variable: list[ExternalVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    constant_variable: list[ConstantVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    local_variable: list[LocalVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )


@dataclass
class Group:
    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Union[Description, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    platform: Optional[Platform] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    warning: list[Warning] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    value: list[Value1] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "sequence": 1,
        },
    )
    group: list["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
        },
    )


@dataclass
class OvalDefinitions:
    class Meta:
        name = "oval_definitions"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    generator: Optional[Generator] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    definitions: Optional[Definitions] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tests: Optional[Tests] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    objects: Optional[Objects] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    states: Optional[States] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    variables: Optional[Variables] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Benchmark:
    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    resolved: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    notice: Optional[Notice] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    front_matter: Optional[FrontMatter] = field(
        default=None,
        metadata={
            "name": "front-matter",
            "type": "Element",
            "required": True,
        },
    )
    rear_matter: Optional[str] = field(
        default=None,
        metadata={
            "name": "rear-matter",
            "type": "Element",
            "required": True,
        },
    )
    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    platform_specification: Optional[PlatformSpecification] = field(
        default=None,
        metadata={
            "name": "platform-specification",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
            "required": True,
        },
    )
    platform: list[Platform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    profile: list[Profile] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    group: list[Group] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Component:
    class Meta:
        name = "component"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
    benchmark: Optional[Benchmark] = field(
        default=None,
        metadata={
            "name": "Benchmark",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
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


@dataclass
class DataStreamCollection:
    class Meta:
        name = "data-stream-collection"
        namespace = "http://scap.nist.gov/schema/scap/source/1.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    schematron_version: Optional[float] = field(
        default=None,
        metadata={
            "name": "schematron-version",
            "type": "Attribute",
            "required": True,
        },
    )
    data_stream: Optional[DataStream] = field(
        default=None,
        metadata={
            "name": "data_stream",
            "type": "Element",
            "required": True,
        },
    )
    component: list[Component] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
