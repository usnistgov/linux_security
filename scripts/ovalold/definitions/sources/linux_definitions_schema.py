from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.data_stream_collection import (
    Filter,
    Set,
)

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


class EntityStateProtocolType(Enum):
    """The EntityStateProtocolType complex type restricts a string value to the set
    of physical layer protocols used by AF_PACKET sockets.

    The empty string is also allowed to support the empty element
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar ETH_P_LOOP: Ethernet loopback packet.
    :cvar ETH_P_PUP: Xerox PUP packet.
    :cvar ETH_P_PUPAT: Xerox PUP Address Transport packet.
    :cvar ETH_P_IP: Internet protocol packet.
    :cvar ETH_P_X25: CCITT X.25 packet.
    :cvar ETH_P_ARP: Address resolution packet.
    :cvar ETH_P_BPQ: G8BPQ AX.25 ethernet packet.
    :cvar ETH_P_IEEEPUP: Xerox IEEE802.3 PUP packet.
    :cvar ETH_P_IEEEPUPAT: Xerox IEEE802.3 PUP address transport packet.
    :cvar ETH_P_DEC: DEC assigned protocol.
    :cvar ETH_P_DNA_DL: DEC DNA Dump/Load.
    :cvar ETH_P_DNA_RC: DEC DNA Remote Console.
    :cvar ETH_P_DNA_RT: DEC DNA Routing.
    :cvar ETH_P_LAT: DEC LAT.
    :cvar ETH_P_DIAG: DEC Diagnostics.
    :cvar ETH_P_CUST: DEC Customer use.
    :cvar ETH_P_SCA: DEC Systems Comms Arch.
    :cvar ETH_P_RARP: Reverse address resolution packet.
    :cvar ETH_P_ATALK: Appletalk DDP.
    :cvar ETH_P_AARP: Appletalk AARP.
    :cvar ETH_P_8021_Q: 802.1Q VLAN Extended Header.
    :cvar ETH_P_IPX: IPX over DIX.
    :cvar ETH_P_IPV6: IPv6 over bluebook.
    :cvar ETH_P_SLOW: Slow Protocol. See 802.3ad 43B.
    :cvar ETH_P_WCCP: Web-cache coordination protocol.
    :cvar ETH_P_PPP_DISC: PPPoE discovery messages.
    :cvar ETH_P_PPP_SES: PPPoE session messages.
    :cvar ETH_P_MPLS_UC: MPLS Unicast traffic.
    :cvar ETH_P_MPLS_MC: MPLS Multicast traffic.
    :cvar ETH_P_ATMMPOA: MultiProtocol Over ATM.
    :cvar ETH_P_ATMFATE: Frame-based ATM Transport over Ethernet.
    :cvar ETH_P_AOE: ATA over Ethernet.
    :cvar ETH_P_TIPC: TIPC.
    :cvar ETH_P_802_3: Dummy type for 802.3 frames.
    :cvar ETH_P_AX25: Dummy protocol id for AX.25.
    :cvar ETH_P_ALL: Every packet.
    :cvar ETH_P_802_2: 802.2 frames.
    :cvar ETH_P_SNAP: Internal only.
    :cvar ETH_P_DDCMP: DEC DDCMP: Internal only
    :cvar ETH_P_WAN_PPP: Dummy type for WAN PPP frames.
    :cvar ETH_P_PPP_MP: Dummy type for PPP MP frames.
    :cvar ETH_P_PPPTALK: Dummy type for Atalk over PPP.
    :cvar ETH_P_LOCALTALK: Localtalk pseudo type.
    :cvar ETH_P_TR_802_2: 802.2 frames.
    :cvar ETH_P_MOBITEX: Mobitex.
    :cvar ETH_P_CONTROL: Card specific control frames.
    :cvar ETH_P_IRDA: Linux-IrDA.
    :cvar ETH_P_ECONET: Acorn Econet.
    :cvar ETH_P_HDLC: HDLC frames.
    :cvar ETH_P_ARCNET: 1A for ArcNet.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    ETH_P_LOOP = "ETH_P_LOOP"
    ETH_P_PUP = "ETH_P_PUP"
    ETH_P_PUPAT = "ETH_P_PUPAT"
    ETH_P_IP = "ETH_P_IP"
    ETH_P_X25 = "ETH_P_X25"
    ETH_P_ARP = "ETH_P_ARP"
    ETH_P_BPQ = "ETH_P_BPQ"
    ETH_P_IEEEPUP = "ETH_P_IEEEPUP"
    ETH_P_IEEEPUPAT = "ETH_P_IEEEPUPAT"
    ETH_P_DEC = "ETH_P_DEC"
    ETH_P_DNA_DL = "ETH_P_DNA_DL"
    ETH_P_DNA_RC = "ETH_P_DNA_RC"
    ETH_P_DNA_RT = "ETH_P_DNA_RT"
    ETH_P_LAT = "ETH_P_LAT"
    ETH_P_DIAG = "ETH_P_DIAG"
    ETH_P_CUST = "ETH_P_CUST"
    ETH_P_SCA = "ETH_P_SCA"
    ETH_P_RARP = "ETH_P_RARP"
    ETH_P_ATALK = "ETH_P_ATALK"
    ETH_P_AARP = "ETH_P_AARP"
    ETH_P_8021_Q = "ETH_P_8021Q"
    ETH_P_IPX = "ETH_P_IPX"
    ETH_P_IPV6 = "ETH_P_IPV6"
    ETH_P_SLOW = "ETH_P_SLOW"
    ETH_P_WCCP = "ETH_P_WCCP"
    ETH_P_PPP_DISC = "ETH_P_PPP_DISC"
    ETH_P_PPP_SES = "ETH_P_PPP_SES"
    ETH_P_MPLS_UC = "ETH_P_MPLS_UC"
    ETH_P_MPLS_MC = "ETH_P_MPLS_MC"
    ETH_P_ATMMPOA = "ETH_P_ATMMPOA"
    ETH_P_ATMFATE = "ETH_P_ATMFATE"
    ETH_P_AOE = "ETH_P_AOE"
    ETH_P_TIPC = "ETH_P_TIPC"
    ETH_P_802_3 = "ETH_P_802_3"
    ETH_P_AX25 = "ETH_P_AX25"
    ETH_P_ALL = "ETH_P_ALL"
    ETH_P_802_2 = "ETH_P_802_2"
    ETH_P_SNAP = "ETH_P_SNAP"
    ETH_P_DDCMP = "ETH_P_DDCMP"
    ETH_P_WAN_PPP = "ETH_P_WAN_PPP"
    ETH_P_PPP_MP = "ETH_P_PPP_MP"
    ETH_P_PPPTALK = "ETH_P_PPPTALK"
    ETH_P_LOCALTALK = "ETH_P_LOCALTALK"
    ETH_P_TR_802_2 = "ETH_P_TR_802_2"
    ETH_P_MOBITEX = "ETH_P_MOBITEX"
    ETH_P_CONTROL = "ETH_P_CONTROL"
    ETH_P_IRDA = "ETH_P_IRDA"
    ETH_P_ECONET = "ETH_P_ECONET"
    ETH_P_HDLC = "ETH_P_HDLC"
    ETH_P_ARCNET = "ETH_P_ARCNET"
    VALUE = ""


class EntityStateRpmVerifyResultType(Enum):
    """The EntityStateRpmVerifyResultType complex type restricts a string value to
    the set of possible outcomes of checking an attribute of a file included in an
    RPM against the actual value of that attribute in the RPM database.

    The empty string is also allowed to support the empty element
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar PASS: 'pass' indicates that the test passed and is equivalent
        to the '.' value reported by the rpm -V command.
    :cvar FAIL: 'fail' indicates that the test failed and is equivalent
        to a bold charcter in the test result string reported by the rpm
        -V command.
    :cvar NOT_PERFORMED: 'not performed' indicates that the test could
        not be performed and is equivalent to the '?' value reported by
        the rpm -V command.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    PASS = "pass"
    FAIL = "fail"
    NOT_PERFORMED = "not performed"
    VALUE = ""


class FileBehaviorsRecurse(Enum):
    DIRECTORIES = "directories"
    SYMLINKS = "symlinks"
    SYMLINKS_AND_DIRECTORIES = "symlinks and directories"


class FileBehaviorsRecurseDirection(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"


class FileBehaviorsRecurseFileSystem(Enum):
    ALL = "all"
    LOCAL = "local"
    DEFINED = "defined"


@dataclass
class RpmInfoBehaviors:
    """The RpmInfoBehaviors complex type defines a set of behaviors for controlling
    what data, for installed rpms, is collected.

    This behavior aligns with the rpm command.

    :ivar filepaths: 'filepaths', when true, this behavior means collect
        all filepaths (directory and file information) from the rpm
        database for the package.
    """

    filepaths: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RpmVerifyBehaviors:
    """The RpmVerifyBehaviors complex type defines a set of behaviors that for
    controlling how installed rpms are verified.

    These behaviors align with the verify-options of the rpm command
    with the addition of two behaviors that will indicate that a file
    with a given attribute marker should not be collected.

    :ivar nodeps: 'nodeps' when true this behavior means, don't verify
        dependencies of packages.
    :ivar nodigest: 'nodigest' when true this behavior means, don't
        verify package or header digests when reading.
    :ivar nofiles: 'nofiles' when true this behavior means, don't verify
        any attributes of package files.
    :ivar noscripts: 'noscripts' when true this behavior means, don't
        execute the %verifyscript scriptlet (if any).
    :ivar nosignature: 'nosignature' when true this behavior means,
        don't verify package or header signatures when reading.
    :ivar nolinkto: 'nolinkto' when true this behavior means, don't
        verify symbolic links attribute.
    :ivar nomd5: 'nomd5' when true this behavior means, don't verify the
        file md5 attribute.
    :ivar nosize: 'nosize' when true this behavior means, don't verify
        the file size attribute.
    :ivar nouser: 'nouser' when true this behavior means, don't verify
        the file owner attribute.
    :ivar nogroup: 'nogroup' when true this behavior means, don't verify
        the file group owner attribute.
    :ivar nomtime: 'nomtime' when true this behavior means, don't verify
        the file mtime attribute.
    :ivar nomode: 'nomode' when true this behavior means, don't verify
        the file mode attribute.
    :ivar nordev: 'nordev' when true this behavior means, don't verify
        the file rdev attribute.
    :ivar noconfigfiles: 'noconfigfiles' when true this behavior means,
        skip files that are marked with the %config attribute marker.
    :ivar noghostfiles: 'noghostfiles' when true this behavior means,
        skip files that are maked with %ghost attribute marker.
    """

    nodeps: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nodigest: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nofiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noscripts: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nosignature: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nolinkto: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomd5: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nosize: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nouser: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nogroup: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomtime: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomode: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nordev: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noconfigfiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noghostfiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RpmVerifyFileBehaviors:
    """The RpmVerifyFileBehaviors complex type defines a set of behaviors that for
    controlling how the individual files in installed rpms are verified.

    These behaviors align with the verify-options of the rpm command
    with the addition of two behaviors that will indicate that a file
    with a given attribute marker should not be collected.

    :ivar nolinkto: 'nolinkto' when true this behavior means, don't
        verify symbolic links attribute.
    :ivar nomd5: 'nomd5' when true this behavior means, don't verify the
        file md5 attribute.
    :ivar nosize: 'nosize' when true this behavior means, don't verify
        the file size attribute.
    :ivar nouser: 'nouser' when true this behavior means, don't verify
        the file owner attribute.
    :ivar nogroup: 'nogroup' when true this behavior means, don't verify
        the file group owner attribute.
    :ivar nomtime: 'nomtime' when true this behavior means, don't verify
        the file mtime attribute.
    :ivar nomode: 'nomode' when true this behavior means, don't verify
        the file mode attribute.
    :ivar nordev: 'nordev' when true this behavior means, don't verify
        the file rdev attribute.
    :ivar noconfigfiles: 'noconfigfiles' when true this behavior means,
        skip files that are marked with the %config attribute marker.
    :ivar noghostfiles: 'noghostfiles' when true this behavior means,
        skip files that are maked with %ghost attribute marker.
    """

    nolinkto: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomd5: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nosize: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nouser: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nogroup: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomtime: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomode: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nordev: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noconfigfiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noghostfiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RpmVerifyPackageBehaviors:
    """The RpmVerifyPackageBehaviors complex type defines a set of behaviors that
    for controlling how installed rpms are verified.

    These behaviors align with the verify-options of the rpm command.

    :ivar nodeps: 'nodeps' when true this behavior means, don't verify
        dependencies of packages.
    :ivar nodigest: 'nodigest' when true this behavior means, don't
        verify package or header digests when reading.
    :ivar noscripts: 'noscripts' when true this behavior means, don't
        execute the %verifyscript scriptlet (if any).
    :ivar nosignature: 'nosignature' when true this behavior means,
        don't verify package or header signatures when reading.
    """

    nodeps: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nodigest: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noscripts: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nosignature: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


class EpochDatatype(Enum):
    STRING = "string"
    INT = "int"


@dataclass
class IflistenersTest:
    """The iflisteners_test is used to check what applications such as packet
    sniffers that are bound to an interface on the system.

    This is limited to applications that are listening on AF_PACKET
    sockets. Furthermore, only applications bound to an ethernet
    interface should be collected. It extends the standard TestType as
    defined in the oval-definitions-schema and one should refer to the
    TestType description for more information. The required object
    element references an iflisteners_object and the optional
    iflisteners_state element specifies the data to check.
    """

    class Meta:
        name = "iflisteners_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


class ReleaseDatatype(Enum):
    STRING = "string"
    VERSION = "version"


@dataclass
class RpmverifyTest:
    """The rpmverify_test is used to verify the integrity of installed RPMs. This
    test aligns with the rpm -V command for verifying RPMs. It extends the standard
    TestType as defined in the oval-definitions-schema and one should refer to the
    TestType description for more information.

    The required object element references a rpmverify_object and the
    optional state element specifies the data to check.
    """

    class Meta:
        name = "rpmverify_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifypackageTest:
    """The rpmverifypackage_test is used to verify the integrity of installed RPMs.
    This test aligns with the rpm -V command for verifying RPMs. It extends the
    standard TestType as defined in the oval-definitions-schema and one should
    refer to the TestType description for more information.

    The required object element references a rpmverifypackage_object and
    the optional state element specifies the data to check.
    """

    class Meta:
        name = "rpmverifypackage_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SlackwarepkginfoState:
    """The slackwarepkginfo_state element defines the different information that
    can be used to evaluate the specified package.

    This includes the version, architecture, and revision. Please refer
    to the individual elements in the schema for more details about what
    each represents.

    :ivar name: This is the package name to check.
    :ivar version: This is the version number of the package.
    :ivar architecture:
    :ivar revision:
    """

    class Meta:
        name = "slackwarepkginfo_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    architecture: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    revision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SlackwarepkginfoTest:
    """The slackware package info test is used to check information associated with
    a given Slackware package.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    slackwarepkginfo_object and the optional state element specifies the
    data to check.
    """

    class Meta:
        name = "slackwarepkginfo_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


class VersionDatatype(Enum):
    STRING = "string"
    VERSION = "version"


@dataclass
class FileBehaviors:
    """The FileBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of a set of files or file related items to collect.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file.

    :ivar max_depth: 'max_depth' defines the maximum depth of recursion
        to perform when a recurse_direction is specified. A value of '0'
        is equivalent to no recursion, '1' means to step only one
        directory level up/down, and so on. The default value is '-1'
        meaning no limitation. For a 'max_depth' of -1 or any value of 1
        or more the starting directory must be considered in the
        recursive search. Note that the default recurse_direction
        behavior is 'none' so even though max_depth specifies no
        limitation by default, the recurse_direction behavior turns
        recursion off. Note that this behavior only applies with the
        equality operation on the path entity.
    :ivar recurse: 'recurse' defines how to recurse into the path
        entity, in other words what to follow during recursion. Options
        include symlinks, directories, or both. Note that a max-depth
        other than 0 has to be specified for recursion to take place and
        for this attribute to mean anything. Also note that this
        behavior does not apply to Windows systems since they do not
        support symbolic links. On Windows systems the 'recurse'
        behavior is always equivalent to directories. Note that this
        behavior only applies with the equality operation on the path
        entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction
        to recurse, either 'up' to parent directories, or 'down' into
        child directories. The default value is 'none' for no recursion.
        Note that this behavior only applies with the equality operation
        on the path entity.
    :ivar recurse_file_system: 'recurse_file_system' defines the file
        system limitation of any searching and applies to all operations
        as specified on the path or filepath entity. The value of
        'local' limits the search scope to local file systems (as
        opposed to file systems mounted from an external system). The
        value of 'defined' keeps any recursion within the file system
        that the file_object (path+filename or filepath) has specified.
        For example, if the path specified was "/", you would search
        only the filesystem mounted there, not other filesystems mounted
        to descendant paths. The value of 'defined' only applies when an
        equality operation is used for searching because the path or
        filepath entity must explicitly define a file system. The
        default value is 'all' meaning to search all available file
        systems for data collection. Note that in most cases it is
        recommended that the value of 'local' be used to ensure that
        file system searching is limited to only the local file systems.
        Searching 'all' file systems may have performance implications.
    """

    max_depth: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1,
            "fraction_digits": 0,
        },
    )
    recurse: FileBehaviorsRecurse = field(
        default=FileBehaviorsRecurse.SYMLINKS_AND_DIRECTORIES,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_direction: FileBehaviorsRecurseDirection = field(
        default=FileBehaviorsRecurseDirection.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    recurse_file_system: FileBehaviorsRecurseFileSystem = field(
        default=FileBehaviorsRecurseFileSystem.ALL,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class IflistenersObject:
    """The iflisteners_object element is used by an iflisteners_test to define the
    specific interface to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar interface_name: The interface_name entity specifies the name
        of the interface (eth0, eth1, fw0, etc.) to check.
    :ivar filter:
    """

    class Meta:
        name = "iflisteners_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class IflistenersState:
    """The iflisteners_state element defines the different information that can be
    used to evaluate the specified applications that are listening on interfaces on
    the system.

    This includes the interface name, protocol, hardware address,
    program name, pid, and user id. Please refer to the individual
    elements in the schema for more details about what each represents.

    :ivar interface_name: This is the name of the interface (eth0, eth1,
        fw0, etc.).
    :ivar protocol: This is the physical layer protocol used by the
        AF_PACKET socket.
    :ivar hw_address: This is the hardware address associated with the
        interface.
    :ivar program_name: This is the name of the communicating program.
    :ivar pid: The pid is the process ID of a specific process.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "iflisteners_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    protocol: Optional[EntityStateProtocolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hw_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    program_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyObject:
    """The rpmverify_object element is used by a rpmverify_test to define a set of
    files within a set of RPMs to verify.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar name: This is the package name to check.
    :ivar filepath: The filepath element specifies the absolute path for
        a file or directory in the specified package.
    :ivar filter:
    """

    class Meta:
        name = "rpmverify_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RpmVerifyBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class RpmverifyState:
    """The rpmverify_state element defines the different information that can be
    used to evaluate the specified rpm.

    This includes the architecture, epoch number, and version numbers.
    Most of this information can be obtained through the rpm function.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar name: This is the package name to check.
    :ivar filepath: The filepath element specifies the absolute path for
        a file or directory in the specified package.
    :ivar size_differs: The size_differs entity aligns with the first
        character ('S' flag) in the character string in the output
        generated by running rpm –V on a specific file.
    :ivar mode_differs: The mode_differs entity aligns with the second
        character ('M' flag) in the character string in the output
        generated by running rpm –V on a specific file.
    :ivar md5_differs: The md5_differs entity aligns with the third
        character ('5' flag) in the character string in the output
        generated by running rpm –V on a specific file.
    :ivar device_differs: The device_differs entity aligns with the
        fourth character ('D' flag) in the character string in the
        output generated by running rpm –V on a specific file.
    :ivar link_mismatch: The link_mismatch entity aligns with the fifth
        character ('L' flag) in the character string in the output
        generated by running rpm –V on a specific file.
    :ivar ownership_differs: The ownership_differs entity aligns with
        the sixth character ('U' flag) in the character string in the
        output generated by running rpm –V on a specific file.
    :ivar group_differs: The group_differs entity aligns with the
        seventh character ('U' flag) in the character string in the
        output generated by running rpm –V on a specific file.
    :ivar mtime_differs: The mtime_differs entity aligns with the eighth
        character ('T' flag) in the character string in the output
        generated by running rpm –V on a specific file.
    :ivar capabilities_differ: The size_differs entity aligns with the
        ninth character ('P' flag) in the character string in the output
        generated by running rpm –V on a specific file.
    :ivar configuration_file: The configuration_file entity represents
        the configuration file attribute marker that may be present on a
        file.
    :ivar documentation_file: The documentation_file entity represents
        the documenation file attribute marker that may be present on a
        file.
    :ivar ghost_file: The ghost_file entity represents the ghost file
        attribute marker that may be present on a file.
    :ivar license_file: The license_file entity represents the license
        file attribute marker that may be present on a file.
    :ivar readme_file: The readme_file entity represents the readme file
        attribute marker that may be present on a file.
    """

    class Meta:
        name = "rpmverify_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mode_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    md5_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    device_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    link_mismatch: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ownership_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mtime_differs: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    capabilities_differ: Optional[EntityStateRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    configuration_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    documentation_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ghost_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    readme_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifypackageObject:
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
            "namespace": "",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["RpmverifypackageObject.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpmverifypackageObject.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpmverifypackageObject.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
    class Epoch:
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version:
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release:
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RpmverifypackageState:
    """The rpmverifypackage_state element defines the different information that
    can be used to verify the integrity of installed rpms.

    This includes the architecture, epoch number, version numbers,
    verification of variuos attributes of an rpm. Most of this
    information can be obtained through the rpm function. Please refer
    to the individual elements in the schema for more details about what
    each represents.

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
        name = "rpmverifypackage_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["RpmverifypackageState.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpmverifypackageState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpmverifypackageState.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency_check_passed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    digest_check_passed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    verification_script_successful: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signature_check_passed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch:
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version:
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release:
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SlackwarepkginfoObject:
    """The slackwarepkginfo_object element is used by a slackware package info test
    to define the object to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A slackware package info object consists of a
    single name entity that identifies the package being checked.

    :ivar set:
    :ivar name: This is the package name to check.
    :ivar filter:
    """

    class Meta:
        name = "slackwarepkginfo_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
