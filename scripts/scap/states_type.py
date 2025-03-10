from dataclasses import dataclass, field

from scap.apparmorstatus_state import ApparmorstatusState
from scap.dnscache_state import DnscacheState
from scap.dpkginfo_state import DpkginfoState
from scap.environmentvariable58_state import Environmentvariable58State
from scap.environmentvariable_state import EnvironmentvariableState
from scap.family_state import FamilyState
from scap.file_state import FileState
from scap.fileextendedattribute_state import FileextendedattributeState
from scap.filehash58_state import Filehash58State
from scap.filehash_state import FilehashState
from scap.gconf_state import GconfState
from scap.httpd_state import HttpdState
from scap.iflisteners_state import IflistenersState
from scap.inetd_state import InetdState
from scap.inetlisteningservers_state import InetlisteningserversState
from scap.interface_state import InterfaceState
from scap.ldap57_state import Ldap57State
from scap.ldap_state import LdapState
from scap.partition_state import PartitionState
from scap.password_state import PasswordState
from scap.portinfo_state import PortinfoState
from scap.process58_state import Process58State
from scap.process_state import ProcessState
from scap.routingtable_state import RoutingtableState
from scap.rpminfo_state import RpminfoState
from scap.rpmverify_state import RpmverifyState
from scap.rpmverifyfile_state import RpmverifyfileState
from scap.rpmverifypackage_state import RpmverifypackageState
from scap.runlevel_state import RunlevelState
from scap.sccs_state import SccsState
from scap.selinuxboolean_state import SelinuxbooleanState
from scap.selinuxsecuritycontext_state import SelinuxsecuritycontextState
from scap.shadow_state import ShadowState
from scap.slackwarepkginfo_state import SlackwarepkginfoState
from scap.sql57_state import Sql57State
from scap.sql_state import SqlState
from scap.symlink_state import SymlinkState
from scap.sysctl_state import SysctlState
from scap.systemdunitdependency_state import SystemdunitdependencyState
from scap.systemdunitproperty_state import SystemdunitpropertyState
from scap.textfilecontent54_state import Textfilecontent54State
from scap.textfilecontent_state import TextfilecontentState
from scap.uname_state import UnameState
from scap.variable_state import VariableState
from scap.xinetd_state import XinetdState
from scap.xmlfilecontent_state import XmlfilecontentState
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class StatesType:
    """The StatesType complex type is a container for one or more state child
    elements.

    Each state provides details about specific characteristics that can
    be used during an evaluation of an object. Please refer to the
    description of the state element for more information about an
    individual state.
    """

    xinetd_state: list[XinetdState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    uname_state: list[UnameState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    sysctl_state: list[SysctlState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    symlink_state: list[SymlinkState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    shadow_state: list[ShadowState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    sccs_state: list[SccsState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    runlevel_state: list[RunlevelState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    routingtable_state: list[RoutingtableState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    process58_state: list[Process58State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    process_state: list[ProcessState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    password_state: list[PasswordState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    interface_state: list[InterfaceState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    inetd_state: list[InetdState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    gconf_state: list[GconfState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    fileextendedattribute_state: list[FileextendedattributeState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    file_state: list[FileState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    dnscache_state: list[DnscacheState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    systemdunitproperty_state: list[SystemdunitpropertyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    systemdunitdependency_state: list[SystemdunitdependencyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    slackwarepkginfo_state: list[SlackwarepkginfoState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    selinuxsecuritycontext_state: list[SelinuxsecuritycontextState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    selinuxboolean_state: list[SelinuxbooleanState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverifypackage_state: list[RpmverifypackageState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverifyfile_state: list[RpmverifyfileState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverify_state: list[RpmverifyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpminfo_state: list[RpminfoState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    partition_state: list[PartitionState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    inetlisteningservers_state: list[InetlisteningserversState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    iflisteners_state: list[IflistenersState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    dpkginfo_state: list[DpkginfoState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    apparmorstatus_state: list[ApparmorstatusState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    xmlfilecontent_state: list[XmlfilecontentState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    variable_state: list[VariableState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    textfilecontent_state: list[TextfilecontentState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    textfilecontent54_state: list[Textfilecontent54State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    sql57_state: list[Sql57State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    sql_state: list[SqlState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    ldap57_state: list[Ldap57State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    ldap_state: list[LdapState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    environmentvariable58_state: list[Environmentvariable58State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    environmentvariable_state: list[EnvironmentvariableState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    filehash58_state: list[Filehash58State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    filehash_state: list[FilehashState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    family_state: list[FamilyState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    portinfo_state: list[PortinfoState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#freebsd",
        },
    )
    httpd_state: list[HttpdState] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache",
        },
    )
