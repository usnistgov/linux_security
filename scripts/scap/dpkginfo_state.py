from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.epoch_datatype_1 import EpochDatatype1
from scap.evr_datatype_1 import EvrDatatype1
from scap.release_datatype_1 import ReleaseDatatype1
from scap.state_type import StateType
from scap.version_datatype_1 import VersionDatatype1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class DpkginfoState(StateType):
    """The dpkginfo_state element defines the different information that can be
    used to evaluate the specified DPKG package.

    This includes the architecture, epoch number, release, and version
    numbers. Please refer to the individual elements in the schema for
    more details about what each represents.

    :ivar name: This is the DPKG package name to check.
    :ivar arch: This is the architecture for which the package was
        built, like : i386, ppc, sparc, noarch.
    :ivar epoch: This is the epoch number of the DPKG. For a null epoch
        (or '(none)' as returned by dpkg) the string '(none)' should be
        used.
    :ivar release: This is the release number of the build, changed by
        the vendor/builder.
    :ivar version: This is the version number of the build.
    :ivar evr: This represents the epoch, upstream_version, and
        debian_revision fields, for a Debian package, as a single
        version string. It has the form "EPOCH:UPSTREAM_VERSION-
        DEBIAN_REVISION". Note that a null epoch (or '(none)' as
        returned by dpkg) is equivalent to '0' and would hence have the
        form 0:UPSTREAM_VERSION-DEBIAN_REVISION.
    """

    class Meta:
        name = "dpkginfo_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    arch: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    epoch: Optional["DpkginfoState.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional["DpkginfoState.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["DpkginfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    evr: Optional["DpkginfoState.Evr"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class Epoch(EntityStateAnySimpleType):
        datatype: EpochDatatype1 = field(
            default=EpochDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityStateAnySimpleType):
        datatype: ReleaseDatatype1 = field(
            default=ReleaseDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype1 = field(
            default=VersionDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Evr(EntityStateAnySimpleType):
        datatype: Optional[EvrDatatype1] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
