from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_any_simple_type import EntityObjectAnySimpleType
from scap.entity_object_string_type import EntityObjectStringType
from scap.epoch_datatype_1 import EpochDatatype1
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.release_datatype_1 import ReleaseDatatype1
from scap.rpm_verify_package_behaviors import RpmVerifyPackageBehaviors
from scap.set import Set
from scap.version_datatype_1 import VersionDatatype1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpmverifypackageObject(ObjectType2):
    """The rpmverifypackage_object element is used by a rpmverify_test to define a
    set of RPMs to verify.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
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
    :ivar filter:
    """

    class Meta:
        name = "rpmverifypackage_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RpmVerifyPackageBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    epoch: Optional["RpmverifypackageObject.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    version: Optional["RpmverifypackageObject.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    release: Optional["RpmverifypackageObject.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    arch: Optional[EntityObjectStringType] = field(
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
    class Epoch(EntityObjectAnySimpleType):
        datatype: EpochDatatype1 = field(
            default=EpochDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityObjectAnySimpleType):
        datatype: VersionDatatype1 = field(
            default=VersionDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityObjectAnySimpleType):
        datatype: ReleaseDatatype1 = field(
            default=ReleaseDatatype1.STRING,
            metadata={
                "type": "Attribute",
            },
        )
