from dataclasses import dataclass, field
from typing import Optional

from scap.epoch_datatype_2 import EpochDatatype2
from scap.release_datatype_2 import ReleaseDatatype2
from scap.version_datatype_4 import VersionDatatype4

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class RpmverifypackageItem:
    """
    This item stores the rpm verification results of an rpm similar to what is
    produced by the rpm -V command.

    :ivar name: This is the package name to check.
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
    :ivar version: This is the version number of the build. In the case
        of an apache rpm named httpd-2.0.40-21.11.4.i686.rpm, this value
        would be 2.0.40.
    :ivar release: This is the release number of the build, changed by
        the vendor/builder.
    :ivar arch: This is the architecture for which the RPM was built,
        like : i386, ppc, sparc, noarch. In the case of an apache rpm
        named httpd-2.0.40-21.11.4.i686.rpm, this value would be i686.
    :ivar extended_name: This represents the name, epoch, version,
        release, and architecture fields as a single version string. It
        has the form "NAME-EPOCH:VERSION-RELEASE.ARCHITECTURE". Note
        that a null epoch (or '(none)' as returned by rpm) is equivalent
        to '0' and would hence have the form NAME-0:VERSION-
        RELEASE.ARCHITECTURE.
    :ivar dependency_check_passed: The dependency_check_passed entity
        indicates whether or not the dependency check passed. If the
        dependency check is not performed, due to the 'nodeps' behavior,
        this entity must not be collected.
    :ivar digest_check_passed: The digest_check_passed entity indicates
        whether or not the verification of the package or header digests
        passed. If the digest check is not performed, due to the
        'nodigest' behavior, this entity must not be collected.
    :ivar verification_script_successful: The
        verification_script_successful entity indicates whether or not
        the verification script executed successfully. If the
        verification script is not executed, due to the 'noscripts'
        behavior, this entity must not be collected.
    :ivar signature_check_passed: The signature_check_passed entity
        indicates whether or not the verification of the package or
        header signatures passed. If the signature check is not
        performed, due to the 'nosignature' behavior, this entity must
        not be collected.
    """

    class Meta:
        name = "rpmverifypackage_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    epoch: Optional["RpmverifypackageItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["RpmverifypackageItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional["RpmverifypackageItem.Release"] = field(
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
    extended_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    dependency_check_passed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    digest_check_passed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    verification_script_successful: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    signature_check_passed: Optional[str] = field(
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
    class Version:
        datatype: VersionDatatype4 = field(
            default=VersionDatatype4.STRING,
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
