from dataclasses import dataclass, field
from typing import Optional

from scap.epoch_datatype_2 import EpochDatatype2
from scap.evr_datatype_2 import EvrDatatype2
from scap.release_datatype_2 import ReleaseDatatype2
from scap.version_datatype_4 import VersionDatatype4

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class DpkginfoItem:
    """
    This item stores DPKG package info.

    :ivar name: This is the pakage name to check.
    :ivar arch: This is the architecture for which the DPKG was built,
        like : i386, ppc, sparc, noarch.
    :ivar epoch: This is the epoch number of the DPKG. For a null epoch
        (or '(none)' as returned by dpkg) the string '(none)' should be
        used.
    :ivar release: This is the release number of the build.
    :ivar version: This is the version number of the build, changed by
        the vendor/builder.
    :ivar evr: This type represents the epoch, upstream_version, and
        debian_revision fields, for a Debian package, as a single
        version string. It has the form "EPOCH:UPSTREAM_VERSION-
        DEBIAN_REVISION". Note that a null epoch (or '(none)' as
        returned by dpkg) is equivalent to '0' and would hence have the
        form 0:UPSTREAM_VERSION-DEBIAN_REVISION.
    """

    class Meta:
        name = "dpkginfo_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
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
    epoch: Optional["DpkginfoItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional["DpkginfoItem.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["DpkginfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    evr: Optional["DpkginfoItem.Evr"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )

    @dataclass
    class Epoch:
        datatype: EpochDatatype2 = field(
            default=EpochDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release:
        datatype: ReleaseDatatype2 = field(
            default=ReleaseDatatype2.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version:
        datatype: VersionDatatype4 = field(
            default=VersionDatatype4.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Evr:
        datatype: Optional[EvrDatatype2] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
