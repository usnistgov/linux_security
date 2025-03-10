from dataclasses import dataclass, field
from typing import Optional

from scap.epoch_datatype_2 import EpochDatatype2
from scap.release_datatype_2 import ReleaseDatatype2
from scap.version_datatype_4 import VersionDatatype4

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class RpminfoItem:
    """
    This item stores rpm info.

    :ivar name: This is the pakage name to check.
    :ivar arch: This is the architecture for which the RPM was built,
        like : i386, ppc, sparc, noarch. In the case of an apache rpm
        named httpd-2.0.40-21.11.4.i686.rpm, this value would be i686.
    :ivar epoch: This is the epoch number of the RPM, this is used as a
        kludge for version-release comparisons where the vendor has done
        some kind of re-numbering or version forking. For a null epoch
        (or '(none)' as returned by rpm) the string '(none)' should be
        used. This number is not revealed by a normal query of the RPM's
        information -- you must use a formatted rpm query command to
        gather this data from the command line, like so. For an already-
        installed RPM: rpm -q --qf '%{EPOCH}\\n' installed_rpm For an
        RPM file that has not been installed: rpm -qp --qf '%{EPOCH}\\n'
        rpm_file
    :ivar release: This is the release number of the build.
    :ivar version: This is the version number of the build, changed by
        the vendor/builder. In the case of an apache rpm named
        httpd-2.0.40-21.11.4.i686.rpm, this value would be 2.0.40.
    :ivar evr: This represents the epoch, version, and release fields as
        a single version string. It has the form "EPOCH:VERSION-
        RELEASE". Note that a null epoch (or '(none)' as returned by
        rpm) is equivalent to '0' and would hence have the form
        0:VERSION-RELEASE.
    :ivar signature_keyid: This field contains the PGP key ID that the
        RPM issuer (generally the original operating system vendor) uses
        to sign the key. PGP is used to verify the authenticity and
        integrity of the RPM being considered. Software packages and
        patches are signed cryptographically to allow administrators to
        allay concerns that the distribution mechanism has been
        compromised, whether that mechanism is web site, FTP server, or
        even a mirror controlled by a hostile party. OVAL uses this
        field most of all to confirm that the package installed on the
        system is that shipped by the vendor, since comparing package
        version numbers against patch announcements is only
        programmatically valid if the installed package is known to
        contain the patched code.
    :ivar extended_name: This represents the name, epoch, version,
        release, and architecture fields as a single version string. It
        has the form "NAME-EPOCH:VERSION-RELEASE.ARCHITECTURE". Note
        that a null epoch (or '(none)' as returned by rpm) is equivalent
        to '0' and would hence have the form NAME-0:VERSION-
        RELEASE.ARCHITECTURE. The 'gpg-pubkey' virtual package on RedHat
        and CentOS should use the string '(none)' for the architecture
        to construct the extended_name.
    :ivar filepath: This field contains the absolute path of a file or
        directory included in the rpm.
    """

    class Meta:
        name = "rpminfo_item"
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
    epoch: Optional["RpminfoItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional["RpminfoItem.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["RpminfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    evr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    signature_keyid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    extended_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filepath: list[str] = field(
        default_factory=list,
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
