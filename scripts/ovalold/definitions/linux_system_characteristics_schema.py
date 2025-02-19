from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


class EntityItemProtocolType(Enum):
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
        detailed error reporting.
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


class EntityItemRpmVerifyResultType(Enum):
    """The EntityItemRpmVerifyResultType complex type restricts a string value to
    the set of possible outcomes of checking an attribute of a file included in an
    RPM against the actual value of that attribute in the RPM database.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar PASS: 'pass' indicates that the test passed and is equivalent
        to the '.' value reported by the rpm -V command.
    :cvar FAIL: 'fail' indicates that the test failed and is equivalent
        to a bold charcter in the test result string reported by the rpm
        -V command.
    :cvar NOT_PERFORMED: 'not performed' indicates that the test could
        not be performed and is equivalent to the '?' value reported by
        the rpm -V command.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    PASS = "pass"
    FAIL = "fail"
    NOT_PERFORMED = "not performed"
    VALUE = ""


class EpochDatatype(Enum):
    STRING = "string"
    INT = "int"


@dataclass
class InetlisteningserverItem:
    """An inet listening server item stores the results of checking for network
    servers currently active on a system.

    It holds information pertaining to a specific protocol-address-port
    combination.

    :ivar protocol: This is the transport-layer protocol, in lowercase:
        tcp or udp.
    :ivar local_address: This is the IP address associated with the inet
        listening server. Note that the IP address can be IPv4 or IPv6.
    :ivar local_port: This is the TCP or UDP port on which the program
        listens.
    :ivar local_full_address: This is the IP address and network port on
        which the program listens, equivalent to
        local_address:local_port. Note that the IP address can be IPv4
        or IPv6.
    :ivar program_name: This is the name of the communicating program.
    :ivar foreign_address: This is the IP address with which the program
        is communicating, or with which it will communicate, in the case
        of a listening server. Note that the IP address can be IPv4 or
        IPv6.
    :ivar foreign_port: This is the TCP or UDP port to which the program
        communicates. In the case of a listening program accepting new
        connections, this value will be 0.
    :ivar foreign_full_address: This is the IP address and network port
        to which the program is communicating or will accept
        communications from, equivalent to foreign_address:foreign_port.
        Note that the IP address can be IPv4 or IPv6.
    :ivar pid: This is the process ID of the process. The process in
        question is that of the program communicating on the network.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "inetlisteningserver_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_port: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_full_address: Optional[str] = field(
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
    foreign_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_port: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_full_address: Optional[str] = field(
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
class PartitionItem:
    """
    The partition_item stores information about a partition on the local system.

    :ivar mount_point: The mount_point element contains a string that
        represents the mount point of a partition on the local system.
    :ivar device: The device element contains a string that represents
        the name of the device.
    :ivar uuid: The uuid element contains a string that represents the
        universally unique identifier associated with a partition.
    :ivar fs_type: The fs_type element contains a string that represents
        the type of filesystem on a partition.
    :ivar mount_options: The mount_options element contains a string
        that represents a mount option associated with a partition on
        the local system.
    :ivar total_space: The total_space element contains an integer that
        represents the total number of blocks on a partition.
    :ivar space_used: The space_used element contains an integer that
        represents the number of blocks used on a partition.
    :ivar space_left: The space_left element contains an integer that
        represents the number of blocks left on a partition.
    """

    class Meta:
        name = "partition_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    mount_point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    device: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    fs_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mount_options: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    total_space: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_used: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_left: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


class ReleaseDatatype(Enum):
    STRING = "string"
    VERSION = "version"


@dataclass
class SelinuxbooleanItem:
    """This item describes the current and pending status of a SELinux boolean.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar name: The name of the SELinux boolean.
    :ivar current_status: The current_status entity indicates current
        state of the specified SELinux boolean.
    :ivar pending_status: The pending_status entity indicates the
        pending state of the specified SELinux boolean.
    """

    class Meta:
        name = "selinuxboolean_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pending_status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SelinuxsecuritycontextItem:
    """This item describes the SELinux security context of a file or process on the
    local system.

    This item follows the SELinux security context structure: user:role:type:low_sensitivity[:low_category]- high_sensitivity [:high_category]. It extends the standard ItemType as defined in the oval-system-characteristics schema and one should refer to the ItemType description for more information.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file. If the xsi:nil attribute is
        set to true, then the item being represented is the higher
        directory represented by the path entity.
    :ivar pid: This is the process ID of the process.
    :ivar user: The user element specifies the SELinux user that either
        created the file or started the process.
    :ivar role: The role element specifies the types that a process may
        transition to (domain transitions). Note that this entity is not
        relevant for files and will always have a value of object_r.
    :ivar type_value: The type element specifies the domain in which the
        file is accessible or the domain in which a process executes.
    :ivar low_sensitivity: The low_sensitivity element specifies the
        current sensitivity of a file or process.
    :ivar low_category: The low_category element specifies the set of
        categories associated with the low sensitivity.
    :ivar high_sensitivity: The high_sensitivity element specifies the
        maximum range for a file or the clearance for a process.
    :ivar high_category: The high_category element specifies the set of
        categories associated with the high sensitivity.
    :ivar rawlow_sensitivity: The rawlow_sensitivity element specifies
        the current sensitivity of a file or process but in its raw
        context.
    :ivar rawlow_category: The rawlow_category element specifies the set
        of categories associated with the low sensitivity but in its raw
        context.
    :ivar rawhigh_sensitivity: The rawhigh_sensitivity element specifies
        the maximum range for a file or the clearance for a process but
        in its raw context.
    :ivar rawhigh_category: The rawhigh_category element specifies the
        set of categories associated with the high sensitivity but in
        its raw context.
    """

    class Meta:
        name = "selinuxsecuritycontext_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    low_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    low_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    high_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    high_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawlow_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawlow_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawhigh_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawhigh_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SlackwarepkginfoItem:
    """This item describes info related to Slackware packages.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar name: This is the pakage name to check.
    :ivar version: This is the version number of the pakage.
    :ivar architecture: This is the architecture the package is designed
        for.
    :ivar revision: This is the revision of the package.
    """

    class Meta:
        name = "slackwarepkginfo_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

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


class VersionDatatype(Enum):
    STRING = "string"
    VERSION = "version"


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
    :ivar evr: This represents the epoch, version, and release fields as
        a single version string. It has the form "EPOCH:VERSION-
        RELEASE". Note that a null epoch (or '(none)' as returned by
        rpm) is equivalent to '0' and would hence have the form
        0:VERSION-RELEASE.
    """

    class Meta:
        name = "dpkginfo_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
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
    epoch: Optional["DpkginfoItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["DpkginfoItem.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["DpkginfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    evr: Optional[str] = field(
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
    class Release:
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
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
class IflistenersItem:
    """An iflisteners_item stores the results of checking for applications that are
    bound to an interface on the system.

    Only applications that are bound to an ethernet interface should be
    collected.

    :ivar interface_name: This is the name of the interface (eth0, eth1,
        fw0, etc.).
    :ivar protocol: This is the physical layer protocol used by the
        AF_PACKET socket.
    :ivar hw_address: This is the hardware address associated with the
        interface.
    :ivar program_name: This is the name of the communicating program.
    :ivar pid: This is the process ID of the process. The process in
        question is that of the program communicating on the network.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "iflisteners_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    protocol: Optional[EntityItemProtocolType] = field(
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
        httpd-2.0.40-21.11.4.i686.rpm, this value would be 21.11.4.
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
        RELEASE.ARCHITECTURE.
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
    epoch: Optional["RpminfoItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpminfoItem.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpminfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    evr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signature_keyid: Optional[str] = field(
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
    filepath: list[str] = field(
        default_factory=list,
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
    class Release:
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
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
class RpmverifyItem:
    """
    This item stores rpm verification results similar to what is produced by the
    rpm -V command.

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
        name = "rpmverify_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

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
    size_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mode_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    md5_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    device_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    link_mismatch: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ownership_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mtime_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    capabilities_differ: Optional[EntityItemRpmVerifyResultType] = field(
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
class RpmverifyfileItem:
    """
    This item stores the verification results of the individual files in an rpm
    similar to what is produced by the rpm -V command.

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
        would be 21.11.4.
    :ivar release: This is the release number of the build, changed by
        the vendor/builder.
    :ivar arch: This is the architecture for which the RPM was built,
        like : i386, ppc, sparc, noarch. In the case of an apache rpm
        named httpd-2.0.40-21.11.4.i686.rpm, this value would be i686.
    :ivar filepath: The filepath element specifies the absolute path for
        a file or directory in the specified package.
    :ivar extended_name: This represents the name, epoch, version,
        release, and architecture fields as a single version string. It
        has the form "NAME-EPOCH:VERSION-RELEASE.ARCHITECTURE". Note
        that a null epoch (or '(none)' as returned by rpm) is equivalent
        to '0' and would hence have the form NAME-0:VERSION-
        RELEASE.ARCHITECTURE.
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
        name = "rpmverifyfile_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["RpmverifyfileItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpmverifyfileItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpmverifyfileItem.Release"] = field(
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
    filepath: Optional[str] = field(
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
    size_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mode_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    md5_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    device_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    link_mismatch: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ownership_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mtime_differs: Optional[EntityItemRpmVerifyResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    capabilities_differ: Optional[EntityItemRpmVerifyResultType] = field(
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
        would be 21.11.4.
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
            "namespace": "",
        },
    )
    epoch: Optional["RpmverifypackageItem.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpmverifypackageItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpmverifypackageItem.Release"] = field(
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
