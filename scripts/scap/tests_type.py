from dataclasses import dataclass, field

from scap.apparmorstatus_test import ApparmorstatusTest
from scap.dnscache_test import DnscacheTest
from scap.dpkginfo_test import DpkginfoTest
from scap.environmentvariable58_test import Environmentvariable58Test
from scap.environmentvariable_test import EnvironmentvariableTest
from scap.family_test import FamilyTest
from scap.file_test import FileTest
from scap.fileextendedattribute_test import FileextendedattributeTest
from scap.filehash58_test import Filehash58Test
from scap.filehash_test import FilehashTest
from scap.gconf_test import GconfTest
from scap.httpd_test import HttpdTest
from scap.iflisteners_test import IflistenersTest
from scap.inetd_test import InetdTest
from scap.inetlisteningservers_test import InetlisteningserversTest
from scap.interface_test import InterfaceTest
from scap.ldap57_test import Ldap57Test
from scap.ldap_test import LdapTest
from scap.partition_test import PartitionTest
from scap.password_test import PasswordTest
from scap.portinfo_test import PortinfoTest
from scap.process58_test import Process58Test
from scap.process_test import ProcessTest
from scap.routingtable_test import RoutingtableTest
from scap.rpminfo_test import RpminfoTest
from scap.rpmverify_test import RpmverifyTest
from scap.rpmverifyfile_test import RpmverifyfileTest
from scap.rpmverifypackage_test import RpmverifypackageTest
from scap.runlevel_test import RunlevelTest
from scap.sccs_test import SccsTest
from scap.selinuxboolean_test import SelinuxbooleanTest
from scap.selinuxsecuritycontext_test import SelinuxsecuritycontextTest
from scap.shadow_test import ShadowTest
from scap.slackwarepkginfo_test import SlackwarepkginfoTest
from scap.sql57_test import Sql57Test
from scap.sql_test import SqlTest
from scap.symlink_test import SymlinkTest
from scap.sysctl_test import SysctlTest
from scap.systemdunitdependency_test import SystemdunitdependencyTest
from scap.systemdunitproperty_test import SystemdunitpropertyTest
from scap.textfilecontent54_test import Textfilecontent54Test
from scap.textfilecontent_test import TextfilecontentTest
from scap.uname_test import UnameTest
from scap.unknown_test import UnknownTest
from scap.variable_test import VariableTest
from scap.xinetd_test import XinetdTest
from scap.xmlfilecontent_test import XmlfilecontentTest

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class TestsType:
    """The TestsType complex type is a container for one or more test child
    elements.

    Each test element describes a single OVAL Test. Please refer to the
    description of the TestType for more information about an individual
    test.
    """

    xinetd_test: list[XinetdTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    uname_test: list[UnameTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    sysctl_test: list[SysctlTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    symlink_test: list[SymlinkTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    shadow_test: list[ShadowTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    sccs_test: list[SccsTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    runlevel_test: list[RunlevelTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    routingtable_test: list[RoutingtableTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    process58_test: list[Process58Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    process_test: list[ProcessTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    password_test: list[PasswordTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    interface_test: list[InterfaceTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    inetd_test: list[InetdTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    gconf_test: list[GconfTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    fileextendedattribute_test: list[FileextendedattributeTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    file_test: list[FileTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    dnscache_test: list[DnscacheTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    systemdunitproperty_test: list[SystemdunitpropertyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    systemdunitdependency_test: list[SystemdunitdependencyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    slackwarepkginfo_test: list[SlackwarepkginfoTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    selinuxsecuritycontext_test: list[SelinuxsecuritycontextTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    selinuxboolean_test: list[SelinuxbooleanTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverifypackage_test: list[RpmverifypackageTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverifyfile_test: list[RpmverifyfileTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverify_test: list[RpmverifyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpminfo_test: list[RpminfoTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    partition_test: list[PartitionTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    inetlisteningservers_test: list[InetlisteningserversTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    iflisteners_test: list[IflistenersTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    dpkginfo_test: list[DpkginfoTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    apparmorstatus_test: list[ApparmorstatusTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    xmlfilecontent_test: list[XmlfilecontentTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    variable_test: list[VariableTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    unknown_test: list[UnknownTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    textfilecontent_test: list[TextfilecontentTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    textfilecontent54_test: list[Textfilecontent54Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    sql57_test: list[Sql57Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    sql_test: list[SqlTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    ldap57_test: list[Ldap57Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    ldap_test: list[LdapTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    environmentvariable58_test: list[Environmentvariable58Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    environmentvariable_test: list[EnvironmentvariableTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    filehash58_test: list[Filehash58Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    filehash_test: list[FilehashTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    family_test: list[FamilyTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    portinfo_test: list[PortinfoTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#freebsd",
        },
    )
    httpd_test: list[HttpdTest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache",
        },
    )
