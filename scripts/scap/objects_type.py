from dataclasses import dataclass, field

from scap.apparmorstatus_object import ApparmorstatusObject
from scap.dnscache_object import DnscacheObject
from scap.dpkginfo_object import DpkginfoObject
from scap.environmentvariable58_object import Environmentvariable58Object
from scap.environmentvariable_object import EnvironmentvariableObject
from scap.family_object import FamilyObject
from scap.file_object import FileObject
from scap.fileextendedattribute_object import FileextendedattributeObject
from scap.filehash58_object import Filehash58Object
from scap.filehash_object import FilehashObject
from scap.gconf_object import GconfObject
from scap.httpd_object import HttpdObject
from scap.iflisteners_object import IflistenersObject
from scap.inetd_object import InetdObject
from scap.inetlisteningservers_object import InetlisteningserversObject
from scap.interface_object import InterfaceObject
from scap.ldap57_object import Ldap57Object
from scap.ldap_object import LdapObject
from scap.partition_object import PartitionObject
from scap.password_object import PasswordObject
from scap.portinfo_object import PortinfoObject
from scap.process58_object import Process58Object
from scap.process_object import ProcessObject
from scap.routingtable_object import RoutingtableObject
from scap.rpminfo_object import RpminfoObject
from scap.rpmverify_object import RpmverifyObject
from scap.rpmverifyfile_object import RpmverifyfileObject
from scap.rpmverifypackage_object import RpmverifypackageObject
from scap.runlevel_object import RunlevelObject
from scap.sccs_object import SccsObject
from scap.selinuxboolean_object import SelinuxbooleanObject
from scap.selinuxsecuritycontext_object import SelinuxsecuritycontextObject
from scap.shadow_object import ShadowObject
from scap.slackwarepkginfo_object import SlackwarepkginfoObject
from scap.sql57_object import Sql57Object
from scap.sql_object import SqlObject
from scap.symlink_object import SymlinkObject
from scap.sysctl_object import SysctlObject
from scap.systemdunitdependency_object import SystemdunitdependencyObject
from scap.systemdunitproperty_object import SystemdunitpropertyObject
from scap.textfilecontent54_object import Textfilecontent54Object
from scap.textfilecontent_object import TextfilecontentObject
from scap.uname_object import UnameObject
from scap.variable_object import VariableObject
from scap.xinetd_object import XinetdObject
from scap.xmlfilecontent_object import XmlfilecontentObject

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ObjectsType:
    """The ObjectsType complex type is a container for one or more object child
    elements.

    Each object element provides details that define a unique set of
    matching items to be used by an OVAL Test. Please refer to the
    description of the object element for more information about an
    individual object.
    """

    xinetd_object: list[XinetdObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    uname_object: list[UnameObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    sysctl_object: list[SysctlObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    symlink_object: list[SymlinkObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    shadow_object: list[ShadowObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    sccs_object: list[SccsObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    runlevel_object: list[RunlevelObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    routingtable_object: list[RoutingtableObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    process58_object: list[Process58Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    process_object: list[ProcessObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    password_object: list[PasswordObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    interface_object: list[InterfaceObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    inetd_object: list[InetdObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    gconf_object: list[GconfObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    fileextendedattribute_object: list[FileextendedattributeObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    file_object: list[FileObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    dnscache_object: list[DnscacheObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix",
        },
    )
    systemdunitproperty_object: list[SystemdunitpropertyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    systemdunitdependency_object: list[SystemdunitdependencyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    slackwarepkginfo_object: list[SlackwarepkginfoObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    selinuxsecuritycontext_object: list[SelinuxsecuritycontextObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    selinuxboolean_object: list[SelinuxbooleanObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverifypackage_object: list[RpmverifypackageObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverifyfile_object: list[RpmverifyfileObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpmverify_object: list[RpmverifyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    rpminfo_object: list[RpminfoObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    partition_object: list[PartitionObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    inetlisteningservers_object: list[InetlisteningserversObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    iflisteners_object: list[IflistenersObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    dpkginfo_object: list[DpkginfoObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    apparmorstatus_object: list[ApparmorstatusObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux",
        },
    )
    xmlfilecontent_object: list[XmlfilecontentObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    variable_object: list[VariableObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    textfilecontent_object: list[TextfilecontentObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    textfilecontent54_object: list[Textfilecontent54Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    sql57_object: list[Sql57Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    sql_object: list[SqlObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    ldap57_object: list[Ldap57Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    ldap_object: list[LdapObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    environmentvariable58_object: list[Environmentvariable58Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    environmentvariable_object: list[EnvironmentvariableObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    filehash58_object: list[Filehash58Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    filehash_object: list[FilehashObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    family_object: list[FamilyObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent",
        },
    )
    portinfo_object: list[PortinfoObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#freebsd",
        },
    )
    httpd_object: list[HttpdObject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5#apache",
        },
    )
