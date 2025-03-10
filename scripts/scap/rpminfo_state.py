from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_evrstring_type import EntityStateEvrstringType
from scap.entity_state_string_type import EntityStateStringType
from scap.epoch_datatype_1 import EpochDatatype1
from scap.release_datatype_1 import ReleaseDatatype1
from scap.state_type import StateType
from scap.version_datatype_1 import VersionDatatype1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpminfoState(StateType):
    """The rpminfo_state element defines the different information that can be used
    to evaluate the specified rpm.

    This includes the architecture, epoch number, and version numbers.
    Most of this information can be obtained through the rpm function.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar name: This is the package name to check.
    :ivar arch: This is the architecture for which the RPM was built,
        like : i386, ppc, sparc, noarch. In the case of an apache rpm
        named httpd-2.0.40-21.11.4.i686.rpm, this value would be i686.
    :ivar epoch: This is the epoch number of the RPM, this is used as a
        kludge for version-release comparisons where the vendor has done
        some kind of re-numbering or version forking. For a null epoch
        (or '(none)' as returned by rpm) the string '(none)' should be
        used.. This number is not revealed by a normal query of the
        RPM's information -- you must use a formatted rpm query command
        to gather this data from the command line, like so. For an
        already-installed RPM: rpm -q --qf '%{EPOCH}\\n' installed_rpm
        For an RPM file that has not been installed: rpm -qp --qf
        '%{EPOCH}\\n' rpm_file
    :ivar release: This is the release number of the build, changed by
        the vendor/builder.
    :ivar version: This is the version number of the build. In the case
        of an apache rpm named httpd-2.0.40-21.11.4.i686.rpm, this value
        would be 2.0.40.
    :ivar evr: This represents the epoch, version, and release fields as
        a single version string. It has the form "EPOCH:VERSION-
        RELEASE". Note that a null epoch (or '(none)' as returned by
        rpm) is equivalent to '0' and would hence have the form
        0:VERSION-RELEASE. Comparisons involving this datatype should
        follow the algorithm of librpm's rpmvercmp() function.
    :ivar signature_keyid: This field contains the 64-bit PGP key ID
        that the RPM issuer (generally the original operating system
        vendor) uses to sign the key. Note that the value should NOT
        contain a hyphen to separate the higher 32-bits from the lower
        32-bits. It should simply be a 16 character hex string. PGP is
        used to verify the authenticity and integrity of the RPM being
        considered. Software packages and patches are signed
        cryptographically to allow administrators to allay concerns that
        the distribution mechanism has been compromised, whether that
        mechanism is web site, FTP server, or even a mirror controlled
        by a hostile party. OVAL uses this field most of all to confirm
        that the package installed on the system is that shipped by the
        vendor, since comparing package version numbers against patch
        announcements is only programmatically valid if the installed
        package is known to contain the patched code.
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
        name = "rpminfo_state"
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
    epoch: Optional["RpminfoState.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional["RpminfoState.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["RpminfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    evr: Optional[EntityStateEvrstringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    signature_keyid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    extended_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filepath: Optional[EntityStateStringType] = field(
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
