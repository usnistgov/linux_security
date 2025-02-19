from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.oval_system_characteristics_schema import (
    EntityItemAnySimpleType,
    EntityItemBoolType,
    EntityItemEvrstringType,
    EntityItemIntType,
    EntityItemIpaddressStringType,
    EntityItemStringType,
    ItemType,
)

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


class EpochDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar INT: The int datatype describes standard integer data.  This
        datatype conforms to the W3C Recommendation for integer data
        which follows the standard mathematical concept of the integer
        numbers.  (no decimal point and infinite range)  Expected
        operations within OVAL for int values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'bitwise and', and 'bitwise or'.
    """

    STRING = "string"
    INT = "int"


class EvrDatatype(Enum):
    """
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    """

    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"


class ReleaseDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """

    STRING = "string"
    VERSION = "version"


class VersionDatatype(Enum):
    """
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """

    STRING = "string"
    VERSION = "version"


@dataclass
class EntityItemProtocolType(EntityItemStringType):
    """The EntityStateProtocolType complex type restricts a string value to the set
    of physical layer protocols used by AF_PACKET sockets.

    The empty string is also allowed to support the empty element
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityItemRpmVerifyResultType(EntityItemStringType):
    """The EntityItemRpmVerifyResultType complex type restricts a string value to
    the set of possible outcomes of checking an attribute of a file included in an
    RPM against the actual value of that attribute in the RPM database.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class EntityItemSestatusModeType(EntityItemStringType):
    """The EntityItemSEStatusModeType complex type restricts a string value to the
    set of SEStatus Current Mode values.

    The empty string is also allowed to support the empty element
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values
    """

    class Meta:
        name = "EntityItemSEStatusModeType"


@dataclass
class EntityItemSestatusPolicyType(EntityItemStringType):
    """The EntityItemSEStatusPolicyType complex type restricts a string value to
    the set of SEStatus Loaded Policy Name values.

    The empty string is also allowed to support the empty element
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values
    """

    class Meta:
        name = "EntityItemSEStatusPolicyType"


@dataclass
class EntityItemSestatusType(EntityItemStringType):
    """The EntityItemSEStatusType complex type restricts a string value to the set
    of SEStatus values that indicate whether SELinux module itself is enabled or
    disabled on your system.

    Keep in mind that even though this may say enabled, but SELinux
    might still be not technically enabled (enforced), which is really
    indicated by the "current_mode" value.
    """

    class Meta:
        name = "EntityItemSEStatusType"


@dataclass
class ApparmorstatusItem(ItemType):
    """The AppArmor Status Item displays various information about the current
    AppArmor policy.

    This item maps the counts of profiles and processes as per the
    results of the "apparmor_status" or "aa-status" command.  Each item
    extends the standard ItemType as defined in the oval-system-
    characteristics-schema and one should refer to the ItemType
    description for more information.

    :ivar loaded_profiles_count: Displays the number of loaded profiles
    :ivar enforce_mode_profiles_count: Displays the number of profiles
        in enforce mode
    :ivar complain_mode_profiles_count: Displays the number of profiles
        in complain mode
    :ivar processes_with_profiles_count: Displays the number of
        processes which have profiles defined
    :ivar enforce_mode_processes_count: Displays the number of processes
        in enforce mode
    :ivar complain_mode_processes_count: Displays the number of
        processes in complain mode
    :ivar unconfined_processes_with_profiles_count: Displays the number
        of processes which are unconfined but have a profile defined
    """

    class Meta:
        name = "apparmorstatus_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    loaded_profiles_count: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enforce_mode_profiles_count: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    complain_mode_profiles_count: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    processes_with_profiles_count: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enforce_mode_processes_count: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    complain_mode_processes_count: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unconfined_processes_with_profiles_count: Optional[EntityItemIntType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )


@dataclass
class DpkginfoItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[EntityItemStringType] = field(
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
    evr: Optional["DpkginfoItem.Evr"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityItemAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityItemAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityItemAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Evr(EntityItemAnySimpleType):
        datatype: Optional[EvrDatatype] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class InetlisteningserverItem(ItemType):
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

    protocol: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_address: Optional[EntityItemIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_port: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_full_address: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    program_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_address: Optional[EntityItemIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_port: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_full_address: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class KernelmoduleItem(ItemType):
    """The kernelmodule_item captures limited information, parsing the output of
    the "modprobe -n -v [module_name]" command.

    Need a combo of "lsmod", "modprobe -n -v" and potentially searching
    "" Collection of a modprobe_item is determined by the "modprobe -n
    -v module_name" command.  Due to the limitations of the modprobe
    command, and its requirement for a specific module_name, only the
    "equals" operation is supported, as there is no method to collect
    this information otherwise.  To support other collection methods,
    variable references should be used to collect specific module names
    for use in collection here.

    :ivar module_name: The name of the kernel module for which
        information was collected
    :ivar loaded: The loaded element is true when the collected kernel
        module is currently loaded; false otherwise.
    :ivar loadable: The loadable element is true when the collected
        kernel module is allowed to be loaded; false otherwise.
    """

    class Meta:
        name = "kernelmodule_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    module_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loaded: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loadable: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PartitionItem(ItemType):
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
        the local system. Implementation note: not all mount options are
        visible in /etc/mtab or /proc/mounts.  A complete source of
        additional mount options is the f_flag field of 'struct
        statvfs'.  See statvfs(2).  /etc/fstab may have additional mount
        options, but it need not contain all mounted filesystems, so it
        MUST NOT be relied upon.  Implementers MUST be sure to get all
        mount options in some way.
    :ivar total_space: The total_space element contains an integer that
        represents the total number of physical blocks on a partition.
    :ivar space_used: The space_used element contains an integer that
        represents the number of physical blocks used on a partition.
    :ivar space_left: The space_left element contains an integer that
        represents the number of physical blocks left on a partition
        available to be used by privileged users.
    :ivar space_left_for_unprivileged_users: The
        space_left_for_unprivileged_users element contains an integer
        that represents the number of physical blocks remaining on a
        partition that are available to be used by unprivileged users.
    :ivar block_size: The block_size element contains an integer
        representing the actual byte size of each physical block on the
        partition's block device. This is the same block size used to
        compute the total_space, space_used, and space_left.
    """

    class Meta:
        name = "partition_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    mount_point: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    device: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uuid: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    fs_type: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mount_options: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    total_space: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_used: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_left: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_left_for_unprivileged_users: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    block_size: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpminfoItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[EntityItemStringType] = field(
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
    evr: Optional[EntityItemEvrstringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signature_keyid: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityItemAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityItemAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityItemAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RpmverifypackageItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
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
    arch: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency_check_passed: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    digest_check_passed: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    verification_script_successful: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signature_check_passed: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityItemAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityItemAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityItemAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SelinuxbooleanItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_status: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pending_status: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SelinuxsecuritycontextItem(ItemType):
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

    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    pid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    role: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    low_sensitivity: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    low_category: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    high_sensitivity: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    high_category: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawlow_sensitivity: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawlow_category: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawhigh_sensitivity: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawhigh_category: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SlackwarepkginfoItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["SlackwarepkginfoItem.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    architecture: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    revision: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Version(EntityItemAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SystemdunitdependencyItem(ItemType):
    """This item stores the dependencies of the systemd unit.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar dependency: The dependency entity refers to the name of a unit
        that was confirmed to be a dependency of the given unit.
    """

    class Meta:
        name = "systemdunitdependency_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    unit: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SystemdunitpropertyItem(ItemType):
    """
    This item stores the properties and values of a systemd unit.

    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar property: The name of the property associated with a systemd
        unit.
    :ivar value: The value of the property associated with a systemd
        unit. Exactly one value shall be used for all property types
        except dbus arrays - each array element shall be represented by
        one value.
    """

    class Meta:
        name = "systemdunitproperty_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    unit: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    property: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class IflistenersItem(ItemType):
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

    interface_name: Optional[EntityItemStringType] = field(
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
    hw_address: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    program_name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyItem(ItemType):
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

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityItemStringType] = field(
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
    configuration_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    documentation_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ghost_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    readme_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyfileItem(ItemType):
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
        would be 2.0.40.
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
    :ivar filedigest_differs: The filedigest_differs entity aligns with
        the third character ('5' flag) in the character string in the
        output generated by running rpm –V on a specific file. This
        replaces the md5_differs entity due to naming changes for
        verification and reporting options.
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

    name: Optional[EntityItemStringType] = field(
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
    arch: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[EntityItemStringType] = field(
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
    filedigest_differs: Optional[EntityItemRpmVerifyResultType] = field(
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
    configuration_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    documentation_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ghost_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    readme_file: Optional[EntityItemBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityItemAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityItemAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityItemAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SestatusItem(ItemType):
    """The SEStatus Item displays various information about the current SEStatus
    policy.

    This item maps the counts of profiles and processes as per the
    results of the "sestatus" command. Each item extends the standard
    ItemType as defined in the oval-system-characteristics-schema and
    one should refer to the ItemType description for more information.

    :ivar selinux_status: Indicates whether SELinux module itself is
        enabled or disabled on your system.
    :ivar current_mode: This indicates whether SELinux is currently
        enforcing the policies or not utilizing the following values
        enforcing, permissive, disabled.
    :ivar mode_from_config_file: Displays the mode from config file.
    :ivar loaded_policy_name: Displays what type of SELinux policy is
        currently loaded. In pretty much all common situations, you’ll
        see “targeted” as the SELinux policy, as that is the default
        policy.
    :ivar policy_from_config_file: Displays what type of SELinux policy
        is present in the SELinux configuration.
    """

    class Meta:
        name = "sestatus_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    selinux_status: Optional[EntityItemSestatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_mode: Optional[EntityItemSestatusModeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mode_from_config_file: Optional[EntityItemSestatusModeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loaded_policy_name: Optional[EntityItemSestatusPolicyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    policy_from_config_file: Optional[EntityItemSestatusPolicyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
