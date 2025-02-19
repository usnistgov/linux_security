from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.oval_definitions_schema import (
    EntityObjectAnySimpleType,
    EntityObjectIntType,
    EntityObjectIpaddressStringType,
    EntityObjectStringType,
    EntityStateAnySimpleType,
    EntityStateBoolType,
    EntityStateEvrstringType,
    EntityStateIntType,
    EntityStateIpaddressStringType,
    EntityStateStringType,
    Filter,
    ObjectRefType,
    ObjectType,
    Set,
    StateRefType,
    StateType,
    TestType,
)

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


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
    :ivar nofiledigest: 'nofiledigest' when true this behavior means,
        don't verify the file digest attribute.
    :ivar nocaps: 'nocaps' when true this behavior means, don't verify
        the presence of file capabilities.
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
    nofiledigest: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nocaps: bool = field(
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
class EntityStateProtocolType(EntityStateStringType):
    """The EntityStateProtocolType complex type restricts a string value to the set
    of physical layer protocols used by AF_PACKET sockets.

    The empty string is also allowed to support the empty element
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateRpmVerifyResultType(EntityStateStringType):
    """The EntityStateRpmVerifyResultType complex type restricts a string value to
    the set of possible outcomes of checking an attribute of a file included in an
    RPM against the actual value of that attribute in the RPM database.

    The empty string is also allowed to support the empty element
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateSestatusModeType(EntityStateStringType):
    """The EntityItemSEStatusModeType complex type restricts a string value to the
    set of SEStatus Current Mode values.

    The empty string is also allowed to support the empty element
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values
    """

    class Meta:
        name = "EntityStateSEStatusModeType"


@dataclass
class EntityStateSestatusPolicyType(EntityStateStringType):
    """The EntityItemSEStatusPolicyType complex type restricts a string value to
    the set of SEStatus Loaded Policy Name values.

    The empty string is also allowed to support the empty element
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values
    """

    class Meta:
        name = "EntityStateSEStatusPolicyType"


@dataclass
class EntityStateSestatusType(EntityStateStringType):
    """The EntityItemSEStatusType complex type restricts a string value to the set
    of SEStatus values that indicate whether SELinux module itself is enabled or
    disabled on your system.

    Keep in mind that even though this may say enabled, but SELinux
    might still be not technically enabled (enforced), which is really
    indicated by the "current_mode" value.
    """

    class Meta:
        name = "EntityStateSEStatusType"


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
class ApparmorstatusObject(ObjectType):
    """The apparmorstatus_object element is used by an apparmorstatus test to
    define the different information about the current AppArmor polciy.

    There is actually only one object relating to AppArmor Status and
    this is the system as a whole. Therefore, there are no child
    entities defined. Any OVAL Test written to check AppArmor status
    will reference the same apparmorstatus_object which is basically an
    empty object element.
    """

    class Meta:
        name = "apparmorstatus_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class ApparmorstatusState(StateType):
    """The AppArmor Status Item displays various information about the current
    AppArmor policy.

    This item maps the counts of profiles and processes as per the
    results of the "apparmor_status" or "aa-status" command.  Please
    refer to the individual elements in the schema for more details
    about what each represents.

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
        name = "apparmorstatus_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    loaded_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enforce_mode_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    complain_mode_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    processes_with_profiles_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enforce_mode_processes_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    complain_mode_processes_count: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unconfined_processes_with_profiles_count: Optional[EntityStateIntType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )


@dataclass
class ApparmorstatusTest(TestType):
    """The AppArmor Status Test is used to check properties representing the counts
    of profiles and processes as per the results of the "apparmor_status" or "aa-
    status" command.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    apparmorstatus_object and the optional state element specifies the
    data to check.
    """

    class Meta:
        name = "apparmorstatus_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class DpkginfoObject(ObjectType):
    """The dpkginfo_object element is used by a dpkginfo test to define the object
    to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A dpkginfo object consists of a single name
    entity that identifies the package being checked.

    :ivar set:
    :ivar name: This is the package name to check.
    :ivar filter:
    """

    class Meta:
        name = "dpkginfo_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    name: Optional[EntityObjectStringType] = field(
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
class DpkginfoState(StateType):
    """The dpkginfo_state element defines the different information that can be
    used to evaluate the specified DPKG package.

    This includes the architecture, epoch number, release, and version
    numbers. Please refer to the individual elements in the schema for
    more details about what each represents.

    :ivar name: This is the DPKG package name to check.
    :ivar arch: This is the architecture for which the package was
        built, like : i386, ppc, sparc, noarch.
    :ivar epoch: This is the epoch number of the DPKG. For a null epoch
        (or '(none)' as returned by dpkg) the string '(none)' should be
        used.
    :ivar release: This is the release number of the build, changed by
        the vendor/builder.
    :ivar version: This is the version number of the build.
    :ivar evr: This represents the epoch, upstream_version, and
        debian_revision fields, for a Debian package, as a single
        version string. It has the form "EPOCH:UPSTREAM_VERSION-
        DEBIAN_REVISION". Note that a null epoch (or '(none)' as
        returned by dpkg) is equivalent to '0' and would hence have the
        form 0:UPSTREAM_VERSION-DEBIAN_REVISION.
    """

    class Meta:
        name = "dpkginfo_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["DpkginfoState.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["DpkginfoState.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["DpkginfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    evr: Optional["DpkginfoState.Evr"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityStateAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityStateAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Evr(EntityStateAnySimpleType):
        datatype: Optional[EvrDatatype] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class DpkginfoTest(TestType):
    """The dpkginfo test is used to check information for a given DPKG package.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    dpkginfo_object and the optional state element specifies the data to
    check.
    """

    class Meta:
        name = "dpkginfo_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class IflistenersObject(ObjectType):
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
    interface_name: Optional[EntityObjectStringType] = field(
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
class IflistenersTest(TestType):
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

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InetlisteningserversObject(ObjectType):
    """The inetlisteningservers_object element is used by an inet listening servers
    test to define the specific protocol-address-port to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An inet listening servers object consists of
    three entities. The first identifies a specific IP address. The
    second entity represents a certain port number. While the third
    identifies the protocol.

    :ivar set:
    :ivar protocol: The protocol entity defines a certain transport-
        layer protocol, in lowercase: tcp or udp.
    :ivar local_address: This is the IP address of the network interface
        on which an application listens. Note that the IP address can be
        IPv4 or IPv6.
    :ivar local_port: This is the TCP or UDP port on which an
        application would listen. Note that this is not a list -- if a
        program listens on multiple ports, or on a combination of TCP
        and UDP, each will be represented by its own object.
    :ivar filter:
    """

    class Meta:
        name = "inetlisteningservers_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    protocol: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_address: Optional[EntityObjectIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_port: Optional[EntityObjectIntType] = field(
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
class InetlisteningserversState(StateType):
    """The inetlisteningservers_state element defines the different information
    that can be used to evaluate the specified inet listening server.

    This includes the local address, foreign address, port information,
    and process id. Please refer to the individual elements in the
    schema for more details about what each represents.

    :ivar protocol: The protocol entity defines the specific transport-
        layer protocol, in lowercase: tcp or udp, associated with the
        inet listening server.
    :ivar local_address: This is the IP address of the network interface
        on which the program listens. Note that the IP address can be
        IPv4 or IPv6.
    :ivar local_port: This is the TCP or UDP port number associated with
        the inet listening server.
    :ivar local_full_address: This is the IP address and network port
        number associated with the inet listening server, equivalent to
        local_address:local_port. Note that the IP address can be IPv4
        or IPv6.
    :ivar program_name: This is the name of the communicating program.
    :ivar foreign_address: This is the IP address with which the program
        is communicating, or with which it will communicate, in the case
        of a listening server. Note that the IP address can be IPv4 or
        IPv6.
    :ivar foreign_port: This is the TCP or UDP port to which the program
        communicates. In the case of a listening program accepting new
        connections, the value will be 0.
    :ivar foreign_full_address: This is the IP address and network port
        to which the program is communicating or will accept
        communications from, equivalent to foreign_address:foreign_port.
        Note that the IP address can be IPv4 or IPv6.
    :ivar pid: The pid is the process ID of a specific process.
    :ivar user_id: The numeric user id, or uid, is the third column of
        each user's entry in /etc/passwd. It represents the owner, and
        thus privilege level, of the specified program.
    """

    class Meta:
        name = "inetlisteningservers_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    protocol: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_port: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_full_address: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    program_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_port: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_full_address: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InetlisteningserversTest(TestType):
    """The inet listening servers test is used to check what applications are
    listening on the network.

    This is limited to applications that are listening for connections
    that use the TCP or UDP protocols and have addresses represented as
    IPv4 or IPv6 addresses (AF_INET or AF_INET6). It is generally using
    the parsed output of running the command netstat -tuwlnpe with root
    privilege. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references an
    inetlisteningservers_object and the optional state element specifies
    the data to check.
    """

    class Meta:
        name = "inetlisteningservers_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class KernelmoduleObject(ObjectType):
    """The kernelmodule_object element is used by the kernelmodule_test to specify
    those modules for which information will be collected.

    This object,
    using the specified module_name, will collect information on the current loaded and loadable status of the module.
    By default modprobe loads modules from subdirectories located in the /lib/modules/$(uname -r) directory. Usually the files have an extension of .ko,
    so they can be listed like this:  find /lib/modules/$(uname -r) -type f -name '*.ko*'.  An example line of output from this command would look like:
    /lib/modules/3.10.0-693.21.1.el7.x86_64/kernel/sound/usb/line6/snd-usb-pod.ko.xz.  In this case, the module name would be "snd-usb-pod".  This
    information may be useful when needing to collect kernel module information based on operators other than "equals", such as pattern matching.
    To populate the "loaded" element for a kernelmodule_item, the specified module name must appear in the output of the "lsmod" command.  "lsmod" is a
    trivial program which nicely formats the contents of the /proc/modules, showing what kernel modules are currently loaded.
    To populate the "loadable" element for a kernelmodule_item, implementors should explore the output of the "modprobe -n -v [module_name]" command.  If
    the output of this command contains a line reading "install /bin/true" then the module is NOT loadable.  Another option is to parse the output of the
    "modprobe --showconfig" command.  Similarly, if an output line matches "install [module_name] /bin/true", then the module is NOT loadable.
    A kernelmodule_object consists of a single module_name entity that identifies the package being checked.

    :ivar set:
    :ivar module_name: This is the name of the kernel module to collect.
    :ivar filter:
    """

    class Meta:
        name = "kernelmodule_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    module_name: Optional[EntityObjectStringType] = field(
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
class KernelmoduleState(StateType):
    """The kernelmodule_state element defines the different information that can be
    used to evaluate the specified kernel module.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar module_name: The name of the kernel module for which
        information was collected
    :ivar loaded: The loaded element is true when the collected kernel
        module is currently loaded; false otherwise.
    :ivar loadable: The loadable element is true when the collected
        kernel module is allowed to be loaded; false otherwise.
    """

    class Meta:
        name = "kernelmodule_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    module_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loaded: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loadable: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class KernelmoduleTest(TestType):
    """The kernelmodule_test is used to check the loaded/loadability status for a
    given kernel module.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    kernelmodule_object and the optional state element specifies the
    data to check.
    """

    class Meta:
        name = "kernelmodule_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PartitionObject(ObjectType):
    """The partition_object is used by a partition_test to define which partitions
    on the local system should be collected.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar mount_point: The mount_point element specifies the mount
        points of the partitions that should be collected from the local
        system.
    :ivar filter:
    """

    class Meta:
        name = "partition_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    mount_point: Optional[EntityObjectStringType] = field(
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
class PartitionState(StateType):
    """The partition_state element defines the different information associated
    with a partition.

    This includes the name, filesystem type, mount options, total space,
    space used, and space left. Please refer to the individual elements
    in the schema for more details about what each represents.

    :ivar mount_point: The mount_point element contains a string that
        represents the mount point of a partition on the local system.
    :ivar device: The device element contains a string that represents
        the name of the device.
    :ivar uuid: The uuid element contains a string that represents the
        universally unique identifier associated with a partition.
    :ivar fs_type: The fs_type element contains a string that represents
        the type of filesystem on a partition.
    :ivar mount_options: The mount_options element contains a string
        that represents the mount options associated with a partition.
        Implementation note: not all mount options are visible in
        /etc/mtab or /proc/mounts.  A complete source of additional
        mount options is the f_flag field of 'struct statvfs'.  See
        statvfs(2).  /etc/fstab may have additional mount options, but
        it need not contain all mounted filesystems, so it MUST NOT be
        relied upon.  Implementers MUST be sure to get all mount options
        in some way.
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
    :ivar block_size: The block_size element contains an integer that
        represents the actual byte size of each physical block on the
        partition's block device. This is the same block size used to
        compute the total_space, space_used, and space_left.
    """

    class Meta:
        name = "partition_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    mount_point: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    device: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    uuid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    fs_type: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mount_options: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    total_space: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_used: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_left: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    space_left_for_unprivileged_users: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    block_size: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PartitionTest(TestType):
    """The partition_test is used to check the information associated with
    partitions on the local system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    partition_object and the optional state element references a
    partition_state that specifies the information to check.
    """

    class Meta:
        name = "partition_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpminfoObject(ObjectType):
    """The rpminfo_object element is used by a rpm info test to define the object
    to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A rpm info object consists of a single name
    entity that identifies the package being checked.

    :ivar set:
    :ivar behaviors:
    :ivar name: This is the package name to check.
    :ivar filter:
    """

    class Meta:
        name = "rpminfo_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RpmInfoBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityObjectStringType] = field(
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
            "namespace": "",
        },
    )
    arch: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["RpminfoState.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpminfoState.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpminfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    evr: Optional[EntityStateEvrstringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signature_keyid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityStateAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityStateAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RpminfoTest(TestType):
    """The rpminfo_test is used to check the RPM header information for a given RPM
    package.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a rpminfo_object
    and the optional state element specifies the data to check.
    """

    class Meta:
        name = "rpminfo_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyObject(ObjectType):
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
    name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityObjectStringType] = field(
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
class RpmverifyTest(TestType):
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

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyfileObject(ObjectType):
    """The rpmverifyfile_object element is used by a rpmverifyfile_test to define a
    set of files within a set of RPMs to verify.

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
    :ivar filepath: The filepath element specifies the absolute path for
        a file or directory in the specified package.
    :ivar filter:
    """

    class Meta:
        name = "rpmverifyfile_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RpmVerifyFileBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["RpmverifyfileObject.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpmverifyfileObject.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpmverifyfileObject.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityObjectStringType] = field(
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
    class Epoch(EntityObjectAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityObjectAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityObjectAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RpmverifyfileTest(TestType):
    """The rpmverifyfile_test is used to verify the integrity of the individual
    files in installed RPMs. This test aligns with the rpm -V command for verifying
    RPMs. It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more information.

    The required object element references a rpmverifyfile_object and
    the optional state element specifies the data to check.
    """

    class Meta:
        name = "rpmverifyfile_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifypackageObject(ObjectType):
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
    name: Optional[EntityObjectStringType] = field(
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
    arch: Optional[EntityObjectStringType] = field(
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
    class Epoch(EntityObjectAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityObjectAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityObjectAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RpmverifypackageState(StateType):
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

    name: Optional[EntityStateStringType] = field(
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
    arch: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency_check_passed: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    digest_check_passed: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    verification_script_successful: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    signature_check_passed: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityStateAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityStateAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RpmverifypackageTest(TestType):
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

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SelinuxbooleanObject(ObjectType):
    """
    The selinuxboolean_object element is used by an selinuxboolean_test to define
    the items to evaluate based on a specified state.

    :ivar set:
    :ivar name: The name of the SELinux boolean.
    :ivar filter:
    """

    class Meta:
        name = "selinuxboolean_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    name: Optional[EntityObjectStringType] = field(
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
class SelinuxbooleanState(StateType):
    """The selinuxboolean_state element defines the different information that can
    be used to evaluate the specified SELinux boolean.

    This includes SELinux boolean's current and pending status. Please
    refer to the individual elements in the schema for more details
    about what each represents.

    :ivar name: The name of the SELinux boolean.
    :ivar current_status: The current_status entity represents the
        current state of the specified SELinux boolean.
    :ivar pending_status: The pending_status entity represents the
        pending state of the specified SELinux boolean.
    """

    class Meta:
        name = "selinuxboolean_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_status: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pending_status: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SelinuxbooleanTest(TestType):
    """The selinuxboolean_test is used to check the current and pending status of a
    SELinux boolean.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    selinuxboolean_object and the optional state element references a
    selinuxboolean_state that specifies the metadata to check.
    """

    class Meta:
        name = "selinuxboolean_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SelinuxsecuritycontextState(StateType):
    """The selinuxsecuritycontext_state element defines the different information
    that can be used to evaluate the specified SELinux security context.

    This includes SELinux security context's user, type role, low
    sensitivity, low category, high sensitivity, high category, raw low
    sensitivity, raw low category, raw high sensitivity, and raw high
    category. This state follows the SELinux security context structure:
    user:role
    :type: low_sensitivity[:low_category]- high_sensitivity
    [:high_category]. Please refer to the individual elements in the
    schema for more details about what each represents.

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
        name = "selinuxsecuritycontext_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    role: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    low_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    low_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    high_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    high_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawlow_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawlow_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawhigh_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rawhigh_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SelinuxsecuritycontextTest(TestType):
    """The selinuxsecuritycontext_test is used to check the security context of a
    file or process on the local system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    selinuxsecuritycontext_object and the optional state element
    references a selinuxsecuritycontext_state that specifies the
    metadata to check.
    """

    class Meta:
        name = "selinuxsecuritycontext_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SestatusObject(ObjectType):
    """The sestatus_object element is used by a sestatus test to define the
    different information about the current SEStatus polciy.

    There is actually only one object relating to SEStatus and this is
    the system as a whole. Therefore, there are no child entities
    defined. Any OVAL Test written to check SEStatus will reference the
    same sestatus_object which is basically an empty object element.
    """

    class Meta:
        name = "sestatus_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class SestatusTest(TestType):
    """The SEStatus Test is used to check properties representing the counts of
    profiles and processes as per the results of the "sestatus" command.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    sestatus_object and the optional state element specifies the data to
    check.
    """

    class Meta:
        name = "sestatus_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SlackwarepkginfoObject(ObjectType):
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
    name: Optional[EntityObjectStringType] = field(
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
class SlackwarepkginfoState(StateType):
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

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["SlackwarepkginfoState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    architecture: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    revision: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SlackwarepkginfoTest(TestType):
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

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SystemdunitdependencyObject(ObjectType):
    """The systemdunitdependency_object element is used by a
    systemdunitdependency_test to define the specific units to check the
    dependencies of.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar filter:
    """

    class Meta:
        name = "systemdunitdependency_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    unit: Optional[EntityObjectStringType] = field(
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
class SystemdunitdependencyState(StateType):
    """The systemdunitdependency_state element holds dependencies of a specific
    systemd unit.

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
        name = "systemdunitdependency_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    unit: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SystemdunitdependencyTest(TestType):
    """The systemdunitdependency_test is used to retrieve information about
    dependencies of a single systemd unit in the form of a list.

    This list contains all dependencies, including transitive
    dependencies. For more information see the output generated by
    systemctl list-dependencies --plain $unit. It extends the standard
    TestType as defined in the oval-definitions-schema and one should
    refer to the TestType description for more information. The required
    object element references a systemdunitdependency_object and the
    optional state element specifies the data to check.
    """

    class Meta:
        name = "systemdunitdependency_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SystemdunitpropertyObject(ObjectType):
    """The systemdunitproperty_object element is used by a systemdunitproperty_test
    to define the specific unit and property combination to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar property: The property entity refers to the systemd unit
        property that we are interested in.
    :ivar filter:
    """

    class Meta:
        name = "systemdunitproperty_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    unit: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    property: Optional[EntityObjectStringType] = field(
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
class SystemdunitpropertyState(StateType):
    """The systemdunitproperty_state element holds information about properties of
    a specific systemd unit.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar unit: The unit entity refers to the full systemd unit name,
        which has a form of "$name.$type". For example "cupsd.service".
        This name is usually also the filename of the unit configuration
        file located in the /etc/systemd/ and /usr/lib/systemd/
        directories.
    :ivar property: The name of the property associated with a systemd
        unit.
    :ivar value: The value of the property associated with a systemd
        unit.
    """

    class Meta:
        name = "systemdunitproperty_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    unit: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    property: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SystemdunitpropertyTest(TestType):
    """The systemdunitproperty_test is used to retrieve information about systemd
    units in form of properties.

    For more information see the output generated by systemctl show
    $unit. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references a
    systemdunitproperty_object and the optional state element specifies
    the data to check.
    """

    class Meta:
        name = "systemdunitproperty_test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class IflistenersState(StateType):
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

    interface_name: Optional[EntityStateStringType] = field(
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
    hw_address: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    program_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyState(StateType):
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

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityStateStringType] = field(
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
    configuration_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    documentation_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ghost_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    readme_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RpmverifyfileState(StateType):
    """The rpmverifyfile_state element defines the different information that can
    be used to determine if a set of files within a set of RPMs passed
    verification.

    This includes the architecture, epoch number, version numbers, and
    the verification of various file attributes. Most of this
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
        name = "rpmverifyfile_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    epoch: Optional["RpmverifyfileState.Epoch"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional["RpmverifyfileState.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    release: Optional["RpmverifyfileState.Release"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arch: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extended_name: Optional[EntityStateStringType] = field(
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
    filedigest_differs: Optional[EntityStateRpmVerifyResultType] = field(
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
    configuration_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    documentation_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ghost_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    readme_file: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Epoch(EntityStateAnySimpleType):
        datatype: EpochDatatype = field(
            default=EpochDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Version(EntityStateAnySimpleType):
        datatype: VersionDatatype = field(
            default=VersionDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Release(EntityStateAnySimpleType):
        datatype: ReleaseDatatype = field(
            default=ReleaseDatatype.STRING,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SelinuxsecuritycontextObject(ObjectType):
    """The selinuxsecuritycontext_object element is used by an
    selinuxsecuritycontext_test to define the security contexts of files and
    processes to collect from the local system.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        evaluate. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level directory object (not
        all the files in the directory).  In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar pid: The pid entity is the process ID of the process.  If the
        xsi:nil attribute is set to true, the process ID shall be the
        tool's running process.
    :ivar filter:
    """

    class Meta:
        name = "selinuxsecuritycontext_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filepath: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    path: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filename: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    pid: Optional[EntityObjectIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
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
class SestatusState(StateType):
    """The SEStatus Item displays various information about the current SEStatus
    policy.

    This item maps the counts of profiles and processes as per the
    results of the "sestatus" command. Please refer to the individual
    elements in the schema for more details about what each represents.

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
        is currently loaded. In pretty much all common situations,
        you’ll see “targeted” as the SELinux policy, as that is the
        default policy.
    """

    class Meta:
        name = "sestatus_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    selinux_status: Optional[EntityStateSestatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_mode: Optional[EntityStateSestatusModeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mode_from_config_file: Optional[EntityStateSestatusModeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loaded_policy_name: Optional[EntityStateSestatusPolicyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    policy_from_config_file: Optional[EntityStateSestatusPolicyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
