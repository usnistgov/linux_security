from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.oval_definitions_schema import (
    EntityObjectIntType,
    EntityObjectIpaddressStringType,
    EntityObjectRecordType,
    EntityObjectStringType,
    EntityObjectVersionType,
    EntityStateAnySimpleType,
    EntityStateBoolType,
    EntityStateIntType,
    EntityStateIpaddressStringType,
    EntityStateRecordType,
    EntityStateStringType,
    EntityStateVersionType,
    Filter,
    ObjectRefType,
    ObjectType,
    Set,
    StateRefType,
    StateType,
    TestType,
)

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"


@dataclass
class AccesstokenBehaviors:
    """The AccesstokenBehaviors complex type defines a number of behaviors that
    allow a more detailed definition of the accesstoken_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_group: If a group security principle is specified,
        this behavior specifies whether to include the group or not. For
        example, maybe you want to check the access tokens associated
        with every user within a group, but not the group itself. In
        this case, you would set the include_group behavior to 'false'.
        If the security_principle is not a group, then this behavior
        should be ignored.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved and
        any valid domain users that are members of the group should also
        be included.  The intent of this behavior is to end up with a
        list of all individual users from that system that make up the
        group once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


class FileBehaviorsRecurseDirection(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"


class FileBehaviorsRecurseFileSystem(Enum):
    ALL = "all"
    LOCAL = "local"
    DEFINED = "defined"


class FileBehaviorsWindowsView(Enum):
    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"


class NtuserBehaviorsRecurseDirection(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"


class NtuserBehaviorsWindowsView(Enum):
    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"


@dataclass
class PrinterEffectiveRightsBehaviors:
    """The PrinterEffectiveRightsBehaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    pritnereffectiverights_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_group: 'include_group' defines whether the group
        trustee name should be included in the object when the object is
        defined by a group trustee name. For example, the intent of an
        object defined by a group trustee name might be to retrieve all
        the user trustee names that are members of the group, but not
        the group trustee name itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


class RegistryBehaviorsRecurseDirection(Enum):
    NONE = "none"
    UP = "up"
    DOWN = "down"


class RegistryBehaviorsWindowsView(Enum):
    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"


@dataclass
class SharedResourceAuditedPermissionsBehaviors:
    """The SharedResourceAuditedPermissionsBehaviors complex type defines a
    behavior that allows for a more detailed definition of the
    sharedresourceauditedpermissions_object being specified.

    Note that using this behavior may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SharedResourceEffectiveRightsBehaviors:
    """The SharedResourceEffectiveRightsBehaviors complex type defines a behavior
    that allows for a more detailed definition of the
    sharedresourceeffectiverights_object being specified.

    Note that using this behavior may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SidBehaviors:
    """The SidBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of the sid_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SidSidBehaviors:
    """The SidSidBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of the sid_sid_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class WuaUpdateSearcherBehaviors:
    """The WuaUpdateSearcherBehaviors complex type defines behaviors that allow a
    more detailed definition of the wuaupdatesearcher_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_superseded_updates: 'include_superseded_updates' is a
        boolean flag that when set to true indicates that the search
        results should include updates that are superseded by other
        updates in the search results. When set to 'false' superseded
        updates should be excluded from the set of matching update
        items. The default value is 'true'.
    """

    include_superseded_updates: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityObjectCmdletVerbType(EntityObjectStringType):
    """The EntityObjectCmdletVerbType restricts a string value to a set of allow
    cmdlet verbs.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the specified pattern restriction.
    """


@dataclass
class EntityObjectGuidtype(EntityObjectStringType):
    """The EntityObjectGUIDType restricts a string value to a representation of a
    GUID, used for module ID.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the specified pattern restriction.
    """

    class Meta:
        name = "EntityObjectGUIDType"


@dataclass
class EntityObjectNamingContextType(EntityObjectStringType):
    """The EntityObjectNamingContextType restricts a string value to a specific set of values: domain, configuration, and schema. These values describe the different default naming context found in active directory. A naming context is defined as a single object in the Directory Information Tree (DIT) along with every object in the tree subordinate to it. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityObjectProtocolType(EntityObjectStringType):
    """The EntityObjectProtocolType restricts a string value to a specific set of values: TCP and UDP. These values describe the different protocols available to a port. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityObjectRegistryHiveType(EntityObjectStringType):
    """The EntityObjectRegistryHiveType restricts a string value to a specific set of values: HKEY_CLASSES_ROOT, HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and HKEY_USERS. These values describe the possible hives in the registry. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityObjectSystemMetricIndexType(EntityObjectStringType):
    """The EntityObjectSystemMetricIndexType complex type defines the different
    values that are valid for the index entity of a system metric object.

    These values describe the system metric or configuration setting to
    be retrieved. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the index entity. Note that when using pattern matches
    and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    Please note that the values identified are for the index entity and
    are not valid values for the datatype attribute.
    """


@dataclass
class EntityObjectUserRightType(EntityObjectStringType):
    """The EntityObjectUserRightType restricts a string value to a specific set of
    values that describe the different user rights/privileges.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the specified pattern restriction.
    """


@dataclass
class EntityStateAddrTypeType(EntityStateStringType):
    """The EntityStateAddrTypeType complex type restricts a string value to a
    specific set of values that describe address types associated with an
    interface.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.
    """


@dataclass
class EntityStateAdstypeType(EntityStateStringType):
    """The EntityStateAdstypeType complex type restricts a string value to a
    specific set of values that specify the different types of information that an
    active directory attribute can represents.

    For more information look at the ADSTYPEENUM enumeration defined by
    Microsoft. The empty string is also allowed to support empty element
    associated with variable references. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateAuditType(EntityStateStringType):
    """The EntityStateAuditType complex type restricts a string value to a specific set of values: AUDIT_NONE, AUDIT_SUCCESS, AUDIT_FAILURE, and AUDIT_SUCCESS_FAILURE. These values describe which audit records should be generated. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityStateCmdletVerbType(EntityStateStringType):
    """The EntityStateCmdletVerbType restricts a string value to a set of allow
    cmdlet verbs.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the specified pattern restriction.
    """


@dataclass
class EntityStateDriveTypeType(EntityStateStringType):
    """The EntityStateDriveTypeType complex type defines the different values that
    are valid for the drive_type entity of a win-def:volume_state.

    Note that the Windows API returns a UINT value and OVAL uses the
    constant name that is normally defined for these return values. This
    is done to increase readability and maintainability of OVAL
    Definitions. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the drive_type entity. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateFileTypeType(EntityStateStringType):
    """The EntityStateFileTypeType complex type restricts a string value to a
    specific set of values.

    These values describe the type of file being represented. For more
    information see the GetFileType and GetFileAttributesEx functions as
    defined by Microsoft. The empty string is also allowed to support
    empty element associated with variable references. Note that when
    using pattern matches and variables care must be taken to ensure
    that the regular expression and variable values align with the
    enumerated values.
    """


@dataclass
class EntityStateGuidtype(EntityStateStringType):
    """The EntityStateGUIDType restricts a string value to a representation of a
    GUID, used for module ID.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the specified pattern restriction.
    """

    class Meta:
        name = "EntityStateGUIDType"


@dataclass
class EntityStateInterfaceTypeType(EntityStateStringType):
    """The EntityStateInterfaceTypeType complex type restricts a string value to a
    specific set of values.

    These values describe the different interface types. The empty
    string is also allowed to support empty element associated with
    variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.
    """


@dataclass
class EntityStateNtuserAccountTypeType(EntityStateStringType):
    """The EntityStateNTUserAccountTypeType restricts a string value to a specific
    set of values that describe the different types of accounts.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.
    """

    class Meta:
        name = "EntityStateNTUserAccountTypeType"


@dataclass
class EntityStateNamingContextType(EntityStateStringType):
    """The EntityStateNamingContextType restricts a string value to a specific set of values: domain, configuration, and schema. These values describe the different default naming context found in active directory. A naming context is defined as a single object in the Directory Information Tree (DIT) along with every object in the tree subordinate to it. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityStatePeSubsystemType(EntityStateStringType):
    """The EntityStatePeSubsystemType enumeration identifies the valid subsystem
    types that can be specified in the PE file header.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.
    """


@dataclass
class EntityStatePeTargetMachineType(EntityStateStringType):
    """The EntityStatePeTargetMachineType enumeration identifies the valid machine
    targets that can be specified in the PE file header.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the enumerated values.
    """


@dataclass
class EntityStateProtocolType(EntityStateStringType):
    """The EntityStateProtocolType restricts a string value to a specific set of values: TCP and UDP. These values describe the different protocols available to a port. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityStateRegistryHiveType(EntityStateStringType):
    """The EntityStateRegistryHiveType restricts a string value to a specific set of values: HKEY_CLASSES_ROOT, HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and HKEY_USERS. These values describe the possible hives in the registry. The empty string is also allowed to support empty element associated with variable references. Note that when using pattern matches and variables care must be taken to ensure that the regular expression and variable values align with the enumerated values."""


@dataclass
class EntityStateRegistryTypeType(EntityStateStringType):
    """The EntityStateRegistryTypeType complex type defines the different values
    that are valid for the type entity of a registry state.

    These values describe the possible types of data stored in a
    registry key. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the type entity. Note that when using pattern matches
    and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    Please note that the values identified are for the type entity and
    are not valid values for the datatype attribute. For information
    about how to encode registry data in OVAL for each of the different
    types, please visit the registry_state documentation.
    """


@dataclass
class EntityStateServiceControlsAcceptedType(EntityStateStringType):
    """The EntityStateServiceAcceptedControlsType complex type defines the
    different values that are valid for the controls_accepted entity of a service.

    Note that the Windows API returns a DWORD value and OVAL uses the
    constant name that is normally defined for these return values. This
    is done to increase readability and maintainability of OVAL
    Definitions. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the controls_accepted entity. Note that when using
    pattern matches and variables care must be taken to ensure that the
    regular expression and variable values align with the enumerated
    values.
    """


@dataclass
class EntityStateServiceCurrentStateType(EntityStateStringType):
    """The EntityStateServiceCurrentStateType complex type defines the different
    values that are valid for the current_state entity of a service.

    Note that the Windows API returns a DWORD value and OVAL uses the
    constant name that is normally defined for these return values. This
    is done to increase readability and maintainability of OVAL
    Definitions. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the current_state entity. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateServiceStartTypeType(EntityStateStringType):
    """The EntityStateServiceStartTypeType complex type defines the different
    values that are valid for the start_type entity of a service.

    Note that the Windows API returns a DWORD value and OVAL uses the
    constant name that is normally defined for these return values. This
    is done to increase readability and maintainability of OVAL
    Definitions. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the start_type entity. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateServiceTypeType(EntityStateStringType):
    """The EntityStateServiceTypeType complex type defines the different values
    that are valid for the service_type entity of a service.

    Note that the Windows API returns a DWORD value and OVAL uses the
    constant name that is normally defined for these return values. This
    is done to increase readability and maintainability of OVAL
    Definitions. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the service_type entity. Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    """


@dataclass
class EntityStateSharedResourceTypeType(EntityStateStringType):
    """The EntityStateSharedResourceTypeType complex type defines the different
    values that are valid for the type entity of a shared resource state.

    Note that the Windows API returns a DWORD value and OVAL uses the
    constant name that is normally defined for these return values. This
    is done to increase readability and maintainability of OVAL
    Definitions. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the type entity. Note that when using pattern matches
    and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values. It
    is also important to note that special shared resources are those
    reserved for remote administration, interprocess communication, and
    administrative shares.
    """


@dataclass
class EntityStateSystemMetricIndexType(EntityStateStringType):
    """The EntityStateSystemMetricIndexType complex type defines the different
    values that are valid for the index entity of a systemmetric_state.

    These values describe the system metric or configuration setting to
    be retrieved. The empty string is also allowed as a valid value to
    support an empty element that is found when a variable reference is
    used within the index entity. Note that when using pattern matches
    and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.
    Please note that the values identified are for the index entity and
    are not valid values for the datatype attribute.
    """


@dataclass
class EntityStateUserRightType(EntityStateStringType):
    """The EntityStateUserRightType restricts a string value to a specific set of
    values that describe the different user rights/privileges.

    The empty string is also allowed to support empty element associated
    with variable references. Note that when using pattern matches and
    variables care must be taken to ensure that the regular expression
    and variable values align with the specified pattern restriction.
    """


@dataclass
class EntityStateWindowsViewType(EntityStateStringType):
    """The EntityStateWindowsViewType restricts a string value to a specific set of values: 32-bit and 64-bit. These values describe the different values possible for the windows view behavior."""


@dataclass
class FileBehaviors:
    """The FileBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of the file_object being specified.

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
    :ivar recurse_direction: 'recurse_direction' defines the direction,
        either 'up' to parent directories, or 'down' into child
        directories to recursively search for files. When recursing up
        or down, one is limited by the max_depth behavior. Note that it
        is not an error if max_depth specifies a certain level of
        recursion and that level does not exist. Recursing should only
        go as deep as available. The default value is 'none' for no
        recursion. Note that this behavior only applies with the
        equality operation on the path entity.
    :ivar recurse_file_system: 'recurse_file_system' defines the file
        system limitation of any searching and applies to all operations
        as specified on the path or filepath entity. The value of
        'local' limits the search scope to local file systems (as
        opposed to file systems mounted from an external system). The
        value of 'defined' keeps any recursion within the file system
        that the file_object (path+filename or filepath) has specified.
        For example, if the path specified was "C:\\", you would search
        only the C: drive, not other filesystems mounted to descendant
        paths. The value of 'defined' only applies when an equality
        operation is used for searching because the path or filepath
        entity must explicitly define a file system. The default value
        is 'all' meaning to search all available file systems for data
        collection. Note that in most cases it is recommended that the
        value of 'local' be used to ensure that file system searching is
        limited to only the local file systems. Searching 'all' file
        systems may have performance implications.
    :ivar windows_view: 64-bit versions of Windows provide an alternate
        file system and registry views to 32-bit applications. This
        behavior allows the OVAL Object to state which view should be
        examined. This behavior only applies to 64-bit Windows, and must
        not be applied on other platforms. Note that the values have the
        following meaning: '64_bit' - Indicates that the 64-bit view on
        64-bit Windows operating systems must be examined. On a 32-bit
        system, the Object must be evaluated without applying the
        behavior. '32_bit' - Indicates that the 32-bit view must be
        examined. On a 32-bit system, the Object must be evaluated
        without applying the behavior. It is recommended that the
        corresponding 'windows_view' entity be set on the OVAL Items
        that are collected when this behavior is used to distinguish
        between OVAL Items that were collected in the 32-bit or 64-bit
        views.
    """

    max_depth: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1,
            "fraction_digits": 0,
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
    windows_view: FileBehaviorsWindowsView = field(
        default=FileBehaviorsWindowsView.VALUE_64_BIT,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class NtuserBehaviors:
    """The NTUserBehaviors complex type defines a number of behaviors that allow a
    more detailed definition of the ntuser_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar include_default: 'include_default' defines if the Window's
        local Default ntuser.dat file is included in the results.  By
        default, this file is not included in the results. The Default
        User's directory which contains the ntuser.dat file is stored in
        the registry at 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows
        NT/CurrentVersion/ProfileList/Default'.
    :ivar max_depth: 'max_depth' defines the maximum depth of recursion
        to perform when a recurse_direction is specified. A value of '0'
        is equivalent to no recursion, '1' means to step only one
        directory level up/down, and so on. The default value is '-1'
        meaning no limitation. For a 'max_depth' of -1 or any value of 1
        or more the starting key must be considered in the recursive
        search. Note that the default recurse_direction behavior is
        'none' so even though max_depth specifies no limitation by
        default, the recurse_direction behavior turns recursion off.
        Note that this behavior only applies with the equality operation
        on the key entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction,
        either 'up' to parent keys, or 'down' into child keys to
        recursively search for registry keys. When recursing up or down,
        one is limited by the max_depth behavior. Note that it is not an
        error if max_depth specifies a certain level of recursion and
        that level does not exist. Recursing should only go as deep as
        available. The default value is 'none' for no recursion. Note
        that this behavior only applies with the equality operation on
        the key entity.
    :ivar windows_view: 64-bit versions of Windows provide an alternate
        file system and registry views to 32-bit applications. This
        behavior allows the OVAL Object to specify which view should be
        examined. This behavior only applies to 64-bit Windows, and must
        not be applied on other platforms. Note that the values have the
        following meaning: '64_bit' – Indicates that the 64-bit view on
        64-bit Windows operating systems must be examined. On a 32-bit
        system, the Object must be evaluated without applying the
        behavior. '32_bit' – Indicates that the 32-bit view must be
        examined. On a 32-bit system, the Object must be evaluated
        without applying the behavior. It is recommended that the
        corresponding 'windows_view' entity be set on the OVAL Items
        that are collected when this behavior is used to distinguish
        between the OVAL Items that are collected in the 32-bit or
        64-bit views.
    """

    class Meta:
        name = "NTUserBehaviors"

    include_default: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    max_depth: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1,
            "fraction_digits": 0,
        },
    )
    recurse_direction: NtuserBehaviorsRecurseDirection = field(
        default=NtuserBehaviorsRecurseDirection.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    windows_view: NtuserBehaviorsWindowsView = field(
        default=NtuserBehaviorsWindowsView.VALUE_64_BIT,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegistryBehaviors:
    """The RegistryBehaviors complex type defines a number of behaviors that allow
    a more detailed definition of the registry_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in.

    :ivar max_depth: 'max_depth' defines the maximum depth of recursion
        to perform when a recurse_direction is specified. A value of '0'
        is equivalent to no recursion, '1' means to step only one
        directory level up/down, and so on. The default value is '-1'
        meaning no limitation. For a 'max_depth' of -1 or any value of 1
        or more the starting key must be considered in the recursive
        search. Note that the default recurse_direction behavior is
        'none' so even though max_depth specifies no limitation by
        default, the recurse_direction behavior turns recursion off.
        Note that this behavior only applies with the equality operation
        on the key entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction,
        either 'up' to parent keys, or 'down' into child keys to
        recursively search for registry keys. When recursing up or down,
        one is limited by the max_depth behavior. Note that it is not an
        error if max_depth specifies a certain level of recursion and
        that level does not exist. Recursing should only go as deep as
        available. The default value is 'none' for no recursion. Note
        that this behavior only applies with the equality operation on
        the key entity.
    :ivar windows_view: 64-bit versions of Windows provide an alternate
        file system and registry views to 32-bit applications. This
        behavior allows the OVAL Object to specify which view should be
        examined. This behavior only applies to 64-bit Windows, and must
        not be applied on other platforms. Note that the values have the
        following meaning: '64_bit' - Indicates that the 64-bit view on
        64-bit Windows operating systems must be examined. On a 32-bit
        system, the Object must be evaluated without applying the
        behavior. '32_bit' - Indicates that the 32-bit view must be
        examined. On a 32-bit system, the Object must be evaluated
        without applying the behavior. It is recommended that the
        corresponding 'windows_view' entity be set on the OVAL Items
        that are collected when this behavior is used to distinguish
        between the OVAL Items that are collected in the 32-bit or
        64-bit views.
    """

    max_depth: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1,
            "fraction_digits": 0,
        },
    )
    recurse_direction: RegistryBehaviorsRecurseDirection = field(
        default=RegistryBehaviorsRecurseDirection.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    windows_view: RegistryBehaviorsWindowsView = field(
        default=RegistryBehaviorsWindowsView.VALUE_64_BIT,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AccesstokenObject(ObjectType):
    """The accesstoken_object element is used by an access token test to define the
    object to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An accesstoken_object consists of a single
    security principle that identifies user, group, or computer account
    that is associated with the token.

    :ivar set:
    :ivar behaviors:
    :ivar security_principle: The security_principle element defines the
        access token being specified. Security principles include users
        or groups with either local or domain accounts, and computer
        accounts created when a computer joins a domain. In Windows,
        security principles are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. User rights and permissions to access objects such
        as Active Directory objects, files, and registry settings are
        assigned to security principles. In a domain environment,
        security principles should be identified in the form:
        "domain\\trustee name". For local security principles use:
        "computer name\\trustee name". For built-in accounts on the
        system, use the trustee name without a domain. If an operation
        other than equals is used to identify matching trustees (i.e.
        not equal, or a pattern match) then the resulting matches shall
        be limited to only the trustees referenced in the Local Security
        Authority database.  The scope is limited here to avoid
        unnecessarily resource intensive searches for trustees.  Note
        that the larger scope of all known trustees may be obtained
        through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "accesstoken_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[AccesstokenBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    security_principle: Optional[EntityObjectStringType] = field(
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
class AccesstokenState(StateType):
    """The accesstoken_state element defines the different information that can be
    used to evaluate the specified access tokens.

    This includes the multitude of user rights and permissions that can
    be granted. Please refer to the individual elements in the schema
    for more details about what each represents.

    :ivar security_principle: The security_principle element identifies
        an access token to test for. Security principles include users
        or groups with either local or domain accounts, and computer
        accounts created when a computer joins a domain. In Windows,
        security principles are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. User rights and permissions to access objects such
        as Active Directory objects, files, and registry settings are
        assigned to security principles. In a domain environment,
        security principles should be identified in the form:
        "domain\\trustee name". For local security principles use:
        "computer name\\trustee name". For built-in accounts on the
        system, use the trustee name without a domain.
    :ivar seassignprimarytokenprivilege: If the
        seassignprimarytokenprivilege privilege is enabled, it allows a
        parent process to replace the access token that is associated
        with a child process.
    :ivar seauditprivilege: If the seauditprivilege privilege is
        enabled, it allows a process to generate audit records in the
        security log. The security log can be used to trace unauthorized
        system access.
    :ivar sebackupprivilege: If the sebackupprivilege privilege is
        enabled, it allows the user to circumvent file and directory
        permissions to back up the system. The privilege is selected
        only when an application attempts access by using the NTFS
        backup application programming interface (API). Otherwise,
        normal file and directory permissions apply.
    :ivar sechangenotifyprivilege: If the sechangenotifyprivilege
        privilege is enabled, it allows the user to pass through folders
        to which the user otherwise has no access while navigating an
        object path in the NTFS file system or in the registry. This
        privilege does not allow the user to list the contents of a
        folder; it allows the user only to traverse its directories.
    :ivar secreateglobalprivilege: If the secreateglobalprivilege
        privilege is enabled, it allows the user to create named file
        mapping objects in the global namespace during Terminal Services
        sessions.
    :ivar secreatepagefileprivilege: If the secreatepagefileprivilege
        privilege is enabled, it allows the user to create and change
        the size of a pagefile.
    :ivar secreatepermanentprivilege: If the secreatepermanentprivilege
        privilege is enabled, it allows a process to create a directory
        object in the object manager. It is useful to kernel-mode
        components that extend the object namespace. Components that are
        running in kernel mode have this privilege inherently.
    :ivar secreatesymboliclinkprivilege: If the
        secreatesymboliclinkprivilege privilege is enabled, it allows
        users to create symbolic links.
    :ivar secreatetokenprivilege: If the secreatetokenprivilege
        privilege is enabled, it allows a process to create an access
        token by calling NtCreateToken() or other token-creating APIs.
    :ivar sedebugprivilege: If the sedebugprivilege privilege is
        enabled, it allows the user to attach a debugger to any process.
        It provides access to sensitive and critical operating system
        components.
    :ivar seenabledelegationprivilege: If the
        seenabledelegationprivilege privilege is enabled, it allows the
        user to change the Trusted for Delegation setting on a user or
        computer object in Active Directory. The user or computer that
        is granted this privilege must also have write access to the
        account control flags on the object.
    :ivar seimpersonateprivilege: If the seimpersonateprivilege
        privilege is enabled, it allows the user to impersonate a client
        after authentication.
    :ivar seincreasebasepriorityprivilege: If the
        seincreasebasepriorityprivilege privilege is enabled, it allows
        a user to increase the base priority class of a process.
    :ivar seincreasequotaprivilege: If the seincreasequotaprivilege
        privilege is enabled, it allows a process that has access to a
        second process to increase the processor quota assigned to the
        second process.
    :ivar seincreaseworkingsetprivilege: If the
        seincreaseworkingsetprivilege privilege is enabled, it allows a
        user to increase a process working set.
    :ivar seloaddriverprivilege: If the seloaddriverprivilege privilege
        is enabled, it allows a user to install and remove drivers for
        Plug and Play devices.
    :ivar selockmemoryprivilege: If the selockmemoryprivilege privilege
        is enabled, it allows a process to keep data in physical memory,
        which prevents the system from paging the data to virtual memory
        on disk.
    :ivar semachineaccountprivilege: If the semachineaccountprivilege
        privilege is enabled, it allows the user to add a computer to a
        specific domain.
    :ivar semanagevolumeprivilege: If the semanagevolumeprivilege
        privilege is enabled, it allows a non-administrative or remote
        user to manage volumes or disks.
    :ivar seprofilesingleprocessprivilege: If the
        seprofilesingleprocessprivilege privilege is enabled, it allows
        a user to sample the performance of an application process.
    :ivar serelabelprivilege: If the serelabelprivilege privilege is
        enabled, it allows a user to modify an object label.
    :ivar seremoteshutdownprivilege: If the seremoteshutdownprivilege
        privilege is enabled, it allows a user to shut down a computer
        from a remote location on the network.
    :ivar serestoreprivilege: If the serestoreprivilege privilege is
        enabled, it allows a user to circumvent file and directory
        permissions when restoring backed-up files and directories and
        to set any valid security principle as the owner of an object.
    :ivar sesecurityprivilege: If the sesecurityprivilege privilege is
        enabled, it allows a user to specify object access auditing
        options for individual resources such as files, Active Directory
        objects, and registry keys. A user who has this privilege can
        also view and clear the security log from Event Viewer.
    :ivar seshutdownprivilege: If the seshutdownprivilege privilege is
        enabled, it allows a user to shut down the local computer.
    :ivar sesyncagentprivilege: If the sesyncagentprivilege privilege is
        enabled, it allows a process to read all objects and properties
        in the directory, regardless of the protection on the objects
        and properties. It is required in order to use Lightweight
        Directory Access Protocol (LDAP) directory synchronization
        (Dirsync) services.
    :ivar sesystemenvironmentprivilege: If the
        sesystemenvironmentprivilege privilege is enabled, it allows
        modification of system environment variables either by a process
        through an API or by a user through System Properties.
    :ivar sesystemprofileprivilege: If the sesystemprofileprivilege
        privilege is enabled, it allows a user to sample the performance
        of system processes.
    :ivar sesystemtimeprivilege: If the sesystemtimeprivilege privilege
        is enabled, it allows the user to adjust the time on the
        computer's internal clock. It is not required to change the time
        zone or other display characteristics of the system time.
    :ivar setakeownershipprivilege: If the setakeownershipprivilege
        privilege is enabled, it allows a user to take ownership of any
        securable object in the system, including Active Directory
        objects, NTFS files and folders, printers, registry keys,
        services, processes, and threads.
    :ivar setcbprivilege: If the setcbprivilege privilege is enabled, it
        allows a process to assume the identity of any user and thus
        gain access to the resources that the user is authorized to
        access.
    :ivar setimezoneprivilege: If the setimezoneprivilege privilege is
        enabled, it allows the user to change the time zone.
    :ivar seundockprivilege: If the seundockprivilege privilege is
        enabled, it allows the user of a portable computer to undock the
        computer by clicking Eject PC on the Start menu.
    :ivar seunsolicitedinputprivilege: If the
        seunsolicitedinputprivilege privilege is enabled, it allows the
        user to read unsolicited data from a terminal device.
    :ivar sebatchlogonright: If an account is assigned the
        sebatchlogonright right, it can log on using the batch logon
        type.
    :ivar seinteractivelogonright: If an account is assigned the
        seinteractivelogonright right, it can log on using the
        interactive logon type.
    :ivar senetworklogonright: If an account is assigned the
        senetworklogonright right, it can log on using the network logon
        type.
    :ivar seremoteinteractivelogonright: If an account is assigned the
        seremoteinteractivelogonright right, it can log on to the
        computer by using a Remote Desktop connection.
    :ivar seservicelogonright: If an account is assigned the
        seservicelogonright right, it can log on using the service logon
        type.
    :ivar sedenybatch_logonright: If an account is assigned the
        sedenybatchLogonright right, it is explicitly denied the ability
        to log on using the batch logon type.
    :ivar sedenyinteractivelogonright: If an account is assigned the
        sedenyinteractivelogonright right, it is explicitly denied the
        ability to log on using the interactive logon type.
    :ivar sedenynetworklogonright: If an account is assigned the
        sedenynetworklogonright right, it is explicitly denied the
        ability to log on using the network logon type.
    :ivar sedenyremote_interactivelogonright: If an account is assigned
        the sedenyremoteInteractivelogonright right, it is explicitly
        denied the ability to log on through Terminal Services.
    :ivar sedenyservicelogonright: If an account is assigned the
        sedenyservicelogonright right, it is explicitly denied the
        ability to log on using the service logon type.
    :ivar setrustedcredmanaccessnameright: If an account is assigned
        this right, it can access the Credential Manager as a trusted
        caller.
    """

    class Meta:
        name = "accesstoken_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    security_principle: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seassignprimarytokenprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seauditprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sebackupprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sechangenotifyprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    secreateglobalprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    secreatepagefileprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    secreatepermanentprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    secreatesymboliclinkprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    secreatetokenprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sedebugprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seenabledelegationprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seimpersonateprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seincreasebasepriorityprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seincreasequotaprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seincreaseworkingsetprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seloaddriverprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    selockmemoryprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    semachineaccountprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    semanagevolumeprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seprofilesingleprocessprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    serelabelprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seremoteshutdownprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    serestoreprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sesecurityprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seshutdownprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sesyncagentprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sesystemenvironmentprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sesystemprofileprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sesystemtimeprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    setakeownershipprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    setcbprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    setimezoneprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seundockprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seunsolicitedinputprivilege: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sebatchlogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seinteractivelogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    senetworklogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seremoteinteractivelogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    seservicelogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sedenybatch_logonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "name": "sedenybatchLogonright",
            "type": "Element",
            "namespace": "",
        },
    )
    sedenyinteractivelogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sedenynetworklogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sedenyremote_interactivelogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "name": "sedenyremoteInteractivelogonright",
            "type": "Element",
            "namespace": "",
        },
    )
    sedenyservicelogonright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    setrustedcredmanaccessnameright: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class AccesstokenTest(TestType):
    """The accesstoken_test is used to check the properties of a Windows access
    token as well as individual privileges and rights associated with it.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    accesstoken_object and the optional state element specifies the data
    to check.
    """

    class Meta:
        name = "accesstoken_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Activedirectory57Test(TestType):
    """The active directory test is used to check information about specific
    entries in active directory.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    activedirectory57_object and the optional state element specifies
    the metadata to check. Note that this test supports complex values
    that are in the form of a record. For simple (string based) value
    collection see the activedirectory_test.
    """

    class Meta:
        name = "activedirectory57_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class ActivedirectoryTest(TestType):
    """The active directory test is used to check information about specific
    entries in active directory.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    activedirectory_object and the optional state element specifies the
    metadata to check. Note that this test supports only simple (string
    based) value collection. For more complex values see the
    activedirectory57_test.
    """

    class Meta:
        name = "activedirectory_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class AuditeventpolicyObject(ObjectType):
    """The auditeventpolicy_object element is used by an audit event policy test to
    define those objects to evaluate based on a specified state.

    There is actually only one object relating to audit event policy and
    this is the system as a whole. Therefore, there are no child
    entities defined. Any OVAL Test written to check audit event policy
    will reference the same auditeventpolicy_object which is basically
    an empty object element.
    """

    class Meta:
        name = "auditeventpolicy_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )


@dataclass
class AuditeventpolicyTest(TestType):
    """The auditeventpolicy_test is used to check different types of events the
    system should audit.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    auditeventpolicy_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "auditeventpolicy_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class AuditeventpolicysubcategoriesObject(ObjectType):
    """The auditeventpolicysubcategories_object element is used by an audit event
    policy subcategories test to define those objects to evaluate based on a
    specified state.

    There is actually only one object relating to audit event policy
    subcategories and this is the system as a whole. Therefore, there
    are no child entities defined. Any OVAL Test written to check audit
    event policy subcategories will reference the same
    auditeventpolicysubcategories_object which is basically an empty
    object element.
    """

    class Meta:
        name = "auditeventpolicysubcategories_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )


@dataclass
class AuditeventpolicysubcategoriesTest(TestType):
    """The auditeventpolicysubcategories_test is used to check the audit event
    policy settings on a Windows system.

    These settings are used to specify which system and network events
    are monitored.  For example, if the credential_validation element
    has a value of AUDIT_FAILURE, it means that the system is configured
    to log all unsuccessful attempts to validate a user account on a
    system. It is important to note that these audit event policy
    settings are specific to certain versions of Windows. As a result,
    the documentation for that version of Windows should be consulted
    for more information on each setting. The test extends the standard
    TestType as defined in the oval-definitions-schema and one should
    refer to the TestType description for more information. The required
    object element references a auditeventpolicy_object and the optional
    state element specifies the metadata to check.
    """

    class Meta:
        name = "auditeventpolicysubcategories_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class CmdletTest(TestType):
    """The cmdlet_test is used to levarage a PowerShell cmdlet to check a Windows
    system.

    The test extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references a
    cmdlet_object and the optional state element specifies the metadata
    to check.
    """

    class Meta:
        name = "cmdlet_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class DnscacheObject(ObjectType):
    """The dnscache_object is used by the dnscache_test to specify the domain
    name(s) that should be collected from the DNS cache on the local system.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar domain_name: The domain_name element specifies the domain
        name(s) that should be collected from the DNS cache on the local
        system.
    :ivar filter:
    """

    class Meta:
        name = "dnscache_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    domain_name: Optional[EntityObjectStringType] = field(
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
class DnscacheState(StateType):
    """
    The dnscache_state contains three entities that are used to check the domain
    name, time to live, and IP addresses associated with the DNS cache entry.

    :ivar domain_name: The domain_name element contains a string that
        represents a domain name that was collected from the DNS cache
        on the local system.
    :ivar ttl: The ttl element contains an integer that represents the
        time to live in seconds of the DNS cache entry.
    :ivar ip_address: The ip_address element contains a string that
        represents an IP address associated with the specified domain
        name that was collected from the DNS cache on the local system.
        Note that the IP address can be IPv4 or IPv6.
    """

    class Meta:
        name = "dnscache_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    domain_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ttl: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ip_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class DnscacheTest(TestType):
    """The dnscache_test is used to check the time to live and IP addresses
    associated with a domain name.

    The time to live and IP addresses for a particular domain name are
    retrieved from the DNS cache on the local system. The entries in the
    DNS cache can be collected using Microsoft's DnsGetCacheDataTable()
    and DnsQuery() API calls. It extends the standard TestType as
    defined in the oval-definitions-schema and one should refer to the
    TestType description for more information. The required object
    element references a dnscache_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "dnscache_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class FileTest(TestType):
    """The file test is used to check metadata associated with Windows files.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a file_object
    and the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "file_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Fileauditedpermissions53Test(TestType):
    """The file audit permissions test is used to check the audit permissions
    associated with Windows files.

    Note that the trustee's audited permissions are the audit permissons
    that the SACL grants to the trustee or to any groups of which the
    trustee is a member. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a fileauditedpermissions_object and the optional state
    element specifies the metadata to check.
    """

    class Meta:
        name = "fileauditedpermissions53_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class FileauditedpermissionsTest(TestType):
    """The file audited permissions test is used to check the audit permissions
    associated with Windows files.

    Note that the trustee's audited permissions are the audit permissons
    that the SACL grants to the trustee or to any groups of which the
    trustee is a member. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a fileauditedpermissions_object, and the optional state
    element references a fileauditedpermissions_state that specifies the
    metadata to check.
    """

    class Meta:
        name = "fileauditedpermissions_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Fileeffectiverights53Test(TestType):
    """The file effective rights test is used to check the effective rights
    associated with Windows files.

    Note that the trustee's effective access rights are the access
    rights that the DACL grants to the trustee or to any groups of which
    the trustee is a member. The fileeffectiverights53_test element
    extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    fileeffectiverights53_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "fileeffectiverights53_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class FileeffectiverightsTest(TestType):
    """The file effective rights test is used to check the effective rights
    associated with Windows files.

    Note that the trustee's effective access rights are the access
    rights that the DACL grants to the trustee or to any groups of which
    the trustee is a member. The fileeffectiverights_test element
    extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    fileeffectiverights_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "fileeffectiverights_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class GroupObject(ObjectType):
    """The group_object element is used by a group test to define the specific
    group(s) (identified by name) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar group: The group element holds a string that represents the
        name of a particular group. In Windows, group names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, the group should be identified in the form:
        "domain\\group name".  In a local environment, the group should
        be identified in the form: "computer name\\group name".  If the
        group is a built-in group, the group should be identified in the
        form: "group name" without a domain component.
    :ivar filter:
    """

    class Meta:
        name = "group_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    group: Optional[EntityObjectStringType] = field(
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
class GroupSidObject(ObjectType):
    """The group_sid_object element is used by a group_test to define the specific
    group(s) (identified by SID) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar group_sid: The group_sid entity holds a string that represents
        the SID of a particular group.
    :ivar filter:
    """

    class Meta:
        name = "group_sid_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    group_sid: Optional[EntityObjectStringType] = field(
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
class GroupSidState(StateType):
    """The group_state element enumerates the different users and subgroups
    directly associated with a Windows group.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar group_sid: The group_sid entity holds a string that represents
        the SID of a particular group.
    :ivar user_sid: The user_sid entity holds a string that represents
        the SID of a particular user.  This entity can be included
        multiple times in a system characteristic item in order to
        record that a group contains a number of different users. Note
        that the entity_check attribute associated with
        EntityStateStringType guides the evaluation of entities like
        user that refer to items that can occur an unbounded number of
        times.
    :ivar subgroup_sid: The subgroup_sid entity holds a string that
        represents the SID of particular subgroup in the specified
        group. This entity can be included multiple times in a system
        characteristic item in order to record that a group contains a
        number of different subgroups. Note that the entity_check
        attribute associated with EntityStateStringType guides the
        evaluation of entities like subgroup_sid that refer to items
        that can occur an unbounded number of times.
    """

    class Meta:
        name = "group_sid_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    group_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subgroup_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GroupSidTest(TestType):
    """The group_sid_test allows the different users and subgroups, that directly
    belong to specific groups (identified by SID), to be tested.

    When the group_sid_test collects the group SIDs on the system, it
    should only include the local and built-in group SIDs and not domain
    group SIDs.  However, it is important to note that domain group SIDs
    can still be looked up. Also, note that the subgroups of the group
    will not be resolved to find indirect user and group members. If the
    subgroups need to be resolved, it should be done using the
    sid_sid_object. It extends the standard TestType as defined in the
    oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a group_sid_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "group_sid_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class GroupState(StateType):
    """The group_state element enumerates the different users and subgroups
    directly associated with a Windows group.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar group: The group element holds a string that represents the
        name of a particular group. In Windows, group names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, groups should be identified in the form:
        "domain\\group name". For local groups use: "computer
        name\\group name". For built-in accounts on the system, use the
        group name without a domain.
    :ivar user: The user element holds a string that represents the name
        of a particular user. In Windows, user names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, users should be identified in the form:
        "domain\\user name". For local users use: "computer name\\user
        name". For built-in accounts on the system, use the user name
        without a domain. The user element can be included multiple
        times in a system characteristic item in order to record that a
        group contains a number of different users. Note that the
        entity_check attribute associated with EntityStateStringType
        guides the evaluation of entities like user that refer to items
        that can occur an unbounded number of times.
    :ivar subgroup: A string that represents the name of a particular
        subgroup in the specified group. In Windows, group names are
        case-insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, the subgroups should be identified in the form:
        "domain\\group name".  In a local environment, the subgroups
        should be identified in the form: "computer name\\group name".
        If the subgroups are built-in groups, the subgroups should be
        identified in the form: "group name" without a domain component.
        The subgroup element can be included multiple times in a system
        characteristic item in order to record that a group contains a
        number of different subgroups. Note that the entity_check
        attribute associated with EntityStateStringType guides the
        evaluation of entities like the subgroup entity that refer to
        items that can occur an unbounded number of times.
    """

    class Meta:
        name = "group_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    group: Optional[EntityStateStringType] = field(
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
    subgroup: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GroupTest(TestType):
    """The group_test allows the different users and subgroups, that directly
    belong to specific groups (identified by name), to be tested.

    When the group_test collects the groups on the system, it should
    only include the local and built-in group accounts and not domain
    group accounts.  However, it is important to note that domain group
    accounts can still be looked up. Also, note that the subgroups of
    the group will not be resolved to find indirect user and group
    members. If the subgroups need to be resolved, it should be done
    using the sid_object. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a group_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "group_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class InterfaceObject(ObjectType):
    """The interface_object element is used by an interface test to define the
    specific interfaces(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An interface object consists of a single name
    entity that identifies which interface is being specified. For help
    understanding this object, see the MIB_IFROW and MIB_IPADDRROW
    structures.

    :ivar set:
    :ivar name: The name element specifies the name of an interface.
    :ivar filter:
    """

    class Meta:
        name = "interface_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class InterfaceTest(TestType):
    """The interface test enumerate various attributes about the interfaces on a
    system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an
    interface_object and the optional state element specifies the
    interface information to check.
    """

    class Meta:
        name = "interface_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class LicenseObject(ObjectType):
    """The license_object element is used by a license_test to define the object to
    be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar name: The name entity provides the address of a UNICODE_STRING
        structure for the name of the value for which data is desired,
        for example, TabletPCPlatformInput-core-EnableTouchUI.
    :ivar filter:
    """

    class Meta:
        name = "license_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class LicenseTest(TestType):
    """The license_test is used to check the content of a particular entry in the
    Windows registry HKLM\\SYSTEM\\CurrentControlSet\\Control\\ProductOptions key,
    ProductPolicy value.

    Access to this data is exposed by the functions NtQueryLicenseValue
    (and also, in version 6.0 and higher, ZwQueryLicenseValue) in
    NTDLL.DLL.
    """

    class Meta:
        name = "license_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class LockoutpolicyObject(ObjectType):
    """The lockoutpolicy_object element is used by a lockout policy test to define
    those objects to evaluated based on a specified state.

    There is actually only one object relating to lockout policy and
    this is the system as a whole. Therefore, there are no child
    entities defined. Any OVAL Test written to check lockout policy will
    reference the same lockoutpolicy_object which is basically an empty
    object element.
    """

    class Meta:
        name = "lockoutpolicy_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )


@dataclass
class LockoutpolicyState(StateType):
    """The lockoutpolicy_state element specifies the various attributes associated
    with lockout information for users and global groups in the security database.

    A lockout policy test will reference a specific instance of this
    state that defines the exact settings that need to be evaluated.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar force_logoff: Specifies, in seconds, the amount of time
        between the end of the valid logon time and the time when the
        user is forced to log off the network. A value of TIMEQ_FOREVER
        (-1) indicates that the user is never forced to log off. A value
        of zero indicates that the user will be forced to log off
        immediately when the valid logon time expires. See the
        USER_MODALS_INFO_0 structure returned by a call to
        NetUserModalsGet().
    :ivar lockout_duration: Specifies, in seconds, how long a locked
        account remains locked before it is automatically unlocked. See
        the USER_MODALS_INFO_3 structure returned by a call to
        NetUserModalsGet().
    :ivar lockout_observation_window: Specifies the maximum time, in
        seconds, that can elapse between any two failed logon attempts
        before lockout occurs. See the USER_MODALS_INFO_3 structure
        returned by a call to NetUserModalsGet().
    :ivar lockout_threshold: Specifies the number of invalid password
        authentications that can occur before an account is marked
        "locked out." See the USER_MODALS_INFO_3 structure returned by a
        call to NetUserModalsGet().
    """

    class Meta:
        name = "lockoutpolicy_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    force_logoff: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    lockout_duration: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    lockout_observation_window: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    lockout_threshold: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LockoutpolicyTest(TestType):
    """The lockout policy test enumerates various attributes associated with
    lockout information for users and global groups in the security database.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    lockoutpolicy_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "lockoutpolicy_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class MetabaseObject(ObjectType):
    """The metabase_object element is used by a metabase test to define the
    specific metabase item(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A metabase object defines the key and id of the
    item(s).

    :ivar set:
    :ivar key: The key element specifies a metabase key.
    :ivar id: The id element specifies a particular object under the
        metabase key. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level key. In this case,
        the id element should not be collected or used in analysis.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, says to collect every id under a given key. The
        most likely use for xsi:nil within a metabase object is when
        checking for the existence of a particular key, without regards
        to the different ids associated with it.
    :ivar filter:
    """

    class Meta:
        name = "metabase_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[EntityObjectIntType] = field(
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
class MetabaseState(StateType):
    """The metabase_state element defines the different metadata associate with a
    metabase item.

    This includes the name, user type, data type, and the actual data.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar key: The key element specifies a metabase key.
    :ivar id: The id element specifies a particular object under the
        metabase key.
    :ivar name: The name element describes the name of the specified
        metabase object.
    :ivar user_type: The user_type element is an unsigned 32-bit integer
        (DWORD) that specifies the user type of the data. See the
        METADATA_RECORD structure.
    :ivar data_type: The data_type element identifies the type of data
        in the metabase entry. See the METADATA_RECORD structure.
    :ivar data: The actual data of the named item under the specified
        metabase key
    """

    class Meta:
        name = "metabase_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_type: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data_type: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    data: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class MetabaseTest(TestType):
    """The metabase test is used to check information found in the Windows
    metabase.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    metabase_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "metabase_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class NtuserTest(TestType):
    """The ntuser test is used to check metadata associated with Windows ntuser.dat
    files.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a ntuser_object
    and the optional state element specifies the ntuser data to check.
    """

    class Meta:
        name = "ntuser_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class PasswordpolicyObject(ObjectType):
    """The passwordpolicy_object element is used by a password policy test to
    define those objects to evaluated based on a specified state.

    There is actually only one object relating to password policy and
    this is the system as a whole. Therefore, there are no child
    entities defined. Any OVAL Test written to check password policy
    will reference the same passwordpolicy_object which is basically an
    empty object element.
    """

    class Meta:
        name = "passwordpolicy_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )


@dataclass
class PasswordpolicyState(StateType):
    """The passwordpolicy_state element specifies the various policies associated
    with passwords.

    A password policy test will reference a specific instance of this
    state that defines the exact settings that need to be evaluated.

    :ivar max_passwd_age: Specifies, in seconds, the maximum allowable
        password age. A value of TIMEQ_FOREVER (-1) indicates that the
        password never expires. The minimum valid value for this element
        is ONE_DAY (86400).
    :ivar min_passwd_age: Specifies the minimum number of seconds that
        can elapse between the time a password changes and when it can
        be changed again. A value of zero indicates that no delay is
        required between password updates.
    :ivar min_passwd_len: Specifies the minimum allowable password
        length. Valid values for this element are zero through PWLEN.
    :ivar password_hist_len: Specifies the length of password history
        maintained. A new password cannot match any of the previous
        usrmod0_password_hist_len passwords. Valid values for this
        element are zero through DEF_MAX_PWHIST.
    :ivar password_complexity: A boolean value that signifies whether
        passwords must meet the complexity requirements put forth by the
        operating system.
    :ivar reversible_encryption: Determines whether or not passwords are
        stored using reversible encryption.
    """

    class Meta:
        name = "passwordpolicy_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    max_passwd_age: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    min_passwd_age: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    min_passwd_len: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    password_hist_len: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    password_complexity: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    reversible_encryption: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PasswordpolicyTest(TestType):
    """The password policy test is used to check specific policy associated with
    passwords.

    It is important to note that these policies are specific to certain versions of Windows.  As a result, the documentation for that version of Windows should be consulted for more information. It extends the standard TestType as defined in the oval-definitions-schema and one should refer to the TestType description for more information. The required object element references a passwordpolicy_object and the optional state element specifies the metadata to check.
    NOTE: This information is stored in the SAM or Active Directory but is encrypted or hidden so the registry_test and activedirectory57_test are of no use. If this can be figured out, then the password_policy test is not needed.
    """

    class Meta:
        name = "passwordpolicy_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class PeheaderTest(TestType):
    """The peheader_test is used to check data from a Portable Executable file
    header.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    peheader_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "peheader_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class PortTest(TestType):
    """The port test is used to check information about the available ports on a
    Windows system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a port_object
    and the optional state element specifies the port information to
    check.
    """

    class Meta:
        name = "port_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class PrintereffectiverightsObject(ObjectType):
    """
    :ivar set:
    :ivar behaviors:
    :ivar printer_name: The printer_name element describes a printer
        that a user may have rights on.
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the printer's Security Descriptor.  The scope is
        limited here to ensure that it is possible to avoid
        unnecessarily resource intensive searches for trustees.  Note
        that the larger scope of all known trustees may be obtained
        through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "printereffectiverights_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[PrinterEffectiveRightsBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    printer_name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class PrintereffectiverightsState(StateType):
    """The printereffectiverights_state element defines the different rights that
    can be associated with a given printereffectiverights_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar printer_name: This element specifies the name of the printer.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar printer_access_administer:
    :ivar printer_access_use:
    :ivar job_access_administer:
    :ivar job_access_read:
    """

    class Meta:
        name = "printereffectiverights_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    printer_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    printer_access_administer: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    printer_access_use: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    job_access_administer: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    job_access_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PrintereffectiverightsTest(TestType):
    """The printer effective rights test is used to check the effective rights
    associated with Windows printers.

    The printereffectiverights_test element extends the standard
    TestType as defined in the oval-definitions-schema and one should
    refer to the TestType description for more information. The required
    object element references a printereffectiverights_object and the
    optional state element specifies the metadata to check.
    """

    class Meta:
        name = "printereffectiverights_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Process58Object(ObjectType):
    """The process58_object element is used by a process58_test to define the
    specific process(es) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A process58_object defines the command line used
    to start the process(es)and pid.

    :ivar set:
    :ivar command_line: The command_line entity is the string used to
        start the process. This includes any parameters that are part of
        the command line.
    :ivar pid: The id given to the process that is created for a
        specified command line.
    :ivar filter:
    """

    class Meta:
        name = "process58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    command_line: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pid: Optional[EntityObjectIntType] = field(
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
class Process58State(StateType):
    """The process58_state element defines the different metadata associate with a
    Windows process.

    This includes the command line, pid, ppid, image path, and current
    directory. Please refer to the individual elements in the schema for
    more details about what each represents.

    :ivar command_line: The command_line entity is the string used to
        start the process. This includes any parameters that are part of
        the command line.
    :ivar pid: The id given to the process that is created for a
        specified command line.
    :ivar ppid: The id given to the parent of the process that is
        created for the specified command line
    :ivar priority: The base priority of the process.
    :ivar image_path: The image_path entity represents the name of the
        executable file for the process.
    :ivar current_dir: The current_dir entity represents the current
        path to the executable file for the process.
    :ivar creation_time: The creation_time entity represents the
        creation time of the process. The value of this entity
        represents the FILETIME structure which is a 64-bit value
        representing the number of 100-nanosecond intervals since
        January 1, 1601 (UTC). See the GetProcessTimes function
        lpCreationTime.
    :ivar dep_enabled: The dep_enabled entity represents whether or not
        data execution prevention (DEP) is enabled. See the
        GetProcessDEPPolicy lpFlags.
    :ivar primary_window_text: The primary_window_text entity represents
        the title of the primary window of the process. See the
        GetWindowText function.
    :ivar name: The name of the process.
    """

    class Meta:
        name = "process58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    command_line: Optional[EntityStateStringType] = field(
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
    ppid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_dir: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    creation_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dep_enabled: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    primary_window_text: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Process58Test(TestType):
    """The process58_test is used to check information found in the Windows
    processes.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    process58_object and the optional state element references a
    process58_state element that specifies the process information to
    check.
    """

    class Meta:
        name = "process58_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class ProcessObject(ObjectType):
    """The process_object element is used by a process test to define the specific
    process(es) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A process_object defines the command line used
    to start the process(es).

    :ivar set:
    :ivar command_line: The command_line entity is the string used to
        start the process. This includes any parameters that are part of
        the command line.
    """

    class Meta:
        name = "process_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    command_line: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ProcessState(StateType):
    """The process_state element defines the different metadata associate with a
    Windows process.

    This includes the command line, pid, ppid, image path, and current
    directory. Please refer to the individual elements in the schema for
    more details about what each represents.

    :ivar command_line: The command_line entity is the string used to
        start the process. This includes any parameters that are part of
        the command line.
    :ivar pid: The id given to the process that is created for a
        specified command line.
    :ivar ppid: The id given to the parent of the process that is
        created for the specified command line
    :ivar priority: The base priority of the process.
    :ivar image_path: The image_path entity contains the name of the
        executable file in question.
    :ivar current_dir: The current_directory entity represents the
        current path to the executable.
    """

    class Meta:
        name = "process_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    command_line: Optional[EntityStateStringType] = field(
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
    ppid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    priority: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_dir: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ProcessTest(TestType):
    """The process_test is used to check information found in the Windows
    processes.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a process_object
    and the optional state element references a process_state element
    that specifies the process information to check.
    """

    class Meta:
        name = "process_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class RegistryTest(TestType):
    """The registry test is used to check metadata associated with Windows registry
    key.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    registry_object and the optional state element specifies the
    registry data to check.
    """

    class Meta:
        name = "registry_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Regkeyauditedpermissions53Test(TestType):
    """The registry key audited permissions test is used to check the audit
    permissions associated with Windows registry keys.

    Note that the trustee's audited permissions are the audit permissons
    that the SACL grants to the trustee or to any groups of which the
    trustee is a member. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a regkeyauditedpermissions53_object and the optional
    state element specifies the metadata to check.
    """

    class Meta:
        name = "regkeyauditedpermissions53_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class RegkeyauditedpermissionsTest(TestType):
    """The registry key audited permissions test is used to check the audit
    permissions associated with Windows registry keys.

    Note that the trustee's audited permissions are the audit permissons
    that the SACL grants to the trustee or to any groups of which the
    trustee is a member. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a regkeyauditedpermissions_object and the optional state
    element specifies the metadata to check.
    """

    class Meta:
        name = "regkeyauditedpermissions_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Regkeyeffectiverights53Test(TestType):
    """The registry key effective rights test is used to check the effective rights
    associated with Windows files.

    Note that the trustee's effective access rights are the access
    rights that the DACL grants to the trustee or to any groups of which
    the trustee is a member. The regkeyeffectiverights53_test element
    extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    regkeyeffectiverights53_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "regkeyeffectiverights53_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class RegkeyeffectiverightsTest(TestType):
    """The registry key effective rights test is used to check the effective rights
    associated with Windows files.

    Note that the trustee's effective access rights are the access
    rights that the DACL grants to the trustee or to any groups of which
    the trustee is a member. The regkeyeffectiverights_test element
    extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    regkeyeffectiverights_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "regkeyeffectiverights_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class ServiceObject(ObjectType):
    """The service_object element is used by a service_test to define the specific
    service(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar service_name: The service_name element specifies the service
        name as stored in the Service Control Manager (SCM) database on
        the system.
    :ivar filter:
    """

    class Meta:
        name = "service_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    service_name: Optional[EntityObjectStringType] = field(
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
class ServiceTest(TestType):
    """The service_test is used to check metadata associated with Windows services.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a service_object
    and the optional state elements specify the metadata to check.
    """

    class Meta:
        name = "service_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class ServiceeffectiverightsObject(ObjectType):
    """The serviceeffectiverights_object element is used by the
    serviceeffectiverights_test to define the objects used to evalutate against the
    specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. A
    serviceeffectiverights_object is defined as a combination of a
    Windows service_name and trustee_sid. The service_name entity
    represents the service to be evaluated while the trustee_sid entity
    represents the account (SID) to check the effective rights of.  If
    multiple services or SIDs are matched by either reference, then each
    possible combination of service and SID is a matching service
    effective rights object.

    :ivar set:
    :ivar service_name: The service_name element describes a service to
        be collected. Note that the service_name element should contain
        the actual name of the service and not its display name that is
        found in Control Panel-&gt;Administrative Tools-&gt;Services.
        For example, if you wanted to check the effective rights of the
        Automatic Updates service you would specify 'wuauserv' for the
        service_name element not 'Automatic Updates'.
    :ivar trustee_sid: The trustee_sid entity identifies a set of SIDs
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the service's Security Descriptor.  The scope is
        limited here to avoid unnecessarily resource intensive searches
        for trustees.  Note that the larger scope of all known trustees
        may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "serviceeffectiverights_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    service_name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class ServiceeffectiverightsState(StateType):
    """The serviceeffectiverights_state element defines the different rights that
    can be associated with a given serviceeffectiverights_object.

    Please refer to the individual elements in the schema for more
    details about what each represents. See
    http://support.microsoft.com/kb/914392
    for more information.

    :ivar service_name: The service_name element specifies a service on
        the machine from which to retrieve the DACL. Note that the
        service_name element should contain the actual name of the
        service and not its display name that is found in Control
        Panel-&gt;Administrative Tools-&gt;Services.  For example, if
        you wanted to check the effective rights of the Automatic
        Updates service you would specify 'wuauserv' for the
        service_name element not 'Automatic Updates'.
    :ivar trustee_sid: The trustee_sid element is the unique SID that is
        associated with a user, group, system, or program (such as a
        Windows service).
    :ivar standard_delete: This permission is required to call the
        DeleteService function to delete the service.
    :ivar standard_read_control: This permission is required to call the
        QueryServiceObjectSecurity function to query the Security
        Descriptor of the service object.
    :ivar standard_write_dac: This permission is required to call the
        SetServiceObjectSecurity function to modify the DACL member of
        the service object's Security Descriptor.
    :ivar standard_write_owner: This permission is required to call the
        SetServiceObjectSecurity function to modify the Owner and Group
        members of the service object's Security Descriptor.
    :ivar generic_read: Read access (STANDARD_RIGHTS_READ,
        SERVICE_QUERY_CONFIG, SERVICE_QUERY_STATUS, SERVICE_INTERROGATE,
        SERVICE_ENUMERATE_DEPENDENTS).
    :ivar generic_write: Write access (STANDARD_RIGHTS_WRITE,
        SERVICE_CHANGE_CONFIG).
    :ivar generic_execute: Execute access (STANDARD_RIGHTS_EXECUTE,
        SERVICE_START, SERVICE_STOP, SERVICE_PAUSE_CONTINUE,
        SERVICE_USER_DEFINED_CONTROL).
    :ivar service_query_conf: This permission is required to call the
        QueryServiceConfig and QueryServiceConfig2 functions to query
        the service configuration.
    :ivar service_change_conf: This permission is required to call the
        ChangeServiceConfig or ChangeServiceConfig2 function to change
        the service configuration.
    :ivar service_query_stat: This permission is required to call the
        QueryServiceStatusEx function to ask the service control manager
        about the status of the service.
    :ivar service_enum_dependents: This permission is required to call
        the EnumDependentServices function to enumerate all the services
        dependent on the service.
    :ivar service_start: This permission is required to call the
        StartService function to start the service.
    :ivar service_stop: This permission is required to call the
        ControlService function to stop the service.
    :ivar service_pause: This permission is required to call the
        ControlService function to pause or continue the service.
    :ivar service_interrogate: This permission is required to call the
        ControlService function to ask the service to report its status
        immediately.
    :ivar service_user_defined: This permission is required to call the
        ControlService function to specify a user-defined control code.
    """

    class Meta:
        name = "serviceeffectiverights_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    service_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_query_conf: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_change_conf: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_query_stat: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_enum_dependents: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_start: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_stop: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_pause: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_interrogate: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_user_defined: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ServiceeffectiverightsTest(TestType):
    """The service effective rights test is used to check the effective rights
    associated with Windows services.

    Note that the trustee's effective access rights are the access
    rights that the DACL grants to the trustee or to any groups of which
    the trustee is a member. The serviceeffectiverights_test element
    extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    serviceeffectiverights_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "serviceeffectiverights_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class SharedresourceObject(ObjectType):
    """The sharedresource_object element is used by a shared resource test to
    define the object, in this case a shared resource, to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An shared resource object consists of a single
    netname entity that identifies a specific shared resource.

    :ivar set:
    :ivar netname: The netname element is the unique name that is
        associated with a specific shared resource.
    :ivar filter:
    """

    class Meta:
        name = "sharedresource_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    netname: Optional[EntityObjectStringType] = field(
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
class SharedresourceTest(TestType):
    """The shared resource test is used to check properties associated with any
    shared resource on the system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    sharedresource_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "sharedresource_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class SharedresourceauditedpermissionsObject(ObjectType):
    """The sharedresourceauditedpermissions_object element is used by a shared
    resource audited permissions test to define the objects used to evaluate
    against the specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. A shared
    resource audited permissions object consists of a netname entity
    that identifies a specific shared resource and a trustee_sid entity
    that identifies a specific account (SID) to check the audited
    permissions of.

    :ivar set:
    :ivar behaviors:
    :ivar netname: The netname element is the unique name that is
        associated with a specific shared resource.
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the file's Security Descriptor.  The scope is
        limited here to avoid unnecessarily resource intensive searches
        for trustees.  Note that the larger scope of all known trustees
        may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "sharedresourceauditedpermissions_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[SharedResourceAuditedPermissionsBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    netname: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class SharedresourceauditedpermissionsTest(TestType):
    """The shared resource audited permissions test is used to check the audit
    permissions associated with any shared resource on the system.

    Note that the trustee's audited permissions are the audit permissons
    that the SACL grants to the trustee or to any groups of which the
    trustee is a member. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a sharedresourceauditedpermissions_object and the
    optional state element specifies the metadata to check.
    """

    class Meta:
        name = "sharedresourceauditedpermissions_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class SharedresourceeffectiverightsObject(ObjectType):
    """The sharedresourceeffectiverights_object element is used by a shared
    resource effective rights test to define the object, in this case a shared
    resource effective rights object, to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A shared resource effective rights object
    consists of a netname entity that identifies a specific shared
    resource and a trustee_sid entity that identifies a specific account
    (SID) to check the effective rights of.

    :ivar set:
    :ivar behaviors:
    :ivar netname: The netname element is the unique name that is
        associated with a specific shared resource.
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the file's Security Descriptor.  The scope is
        limited here to avoid unnecessarily resource intensive searches
        for trustees.  Note that the larger scope of all known trustees
        may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "sharedresourceeffectiverights_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[SharedResourceEffectiveRightsBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    netname: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class SharedresourceeffectiverightsState(StateType):
    """The sharedresourceeffectiverights_state element defines the different rights
    that can be associated with a given sharedresourceeffectiverights_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar netname: This element specifies the name associated with a
        particular shared resource.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    """

    class Meta:
        name = "sharedresourceeffectiverights_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    netname: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SharedresourceeffectiverightsTest(TestType):
    """The shared resource effective rights test is used to check the effective
    rights associated with any shared resource on the system.

    Note that the trustee's effective access rights are the access
    rights that the DACL grants to the trustee or to any groups of which
    the trustee is a member. It extends the standard TestType as defined
    in the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a sharedresourceeffectiverights_object and the optional
    state element specifies the metadata to check.
    """

    class Meta:
        name = "sharedresourceeffectiverights_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class SidObject(ObjectType):
    """The sid_object element is used by a sid_test to define the object set, in
    this case a set of SIDs (identified by name), to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar trustee_name: The trustee_name element is the unique name that
        associated a particular SID. A SID can be associated with a
        user, group, or program (such as a Windows service). In Windows,
        trustee names are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. In a domain environment, trustee names should be
        identified in the form: "domain\\trustee name". For local
        trustee names use: "computer name\\trustee name". For built-in
        accounts on the system, use the trustee name without a domain.
    :ivar filter:
    """

    class Meta:
        name = "sid_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[SidBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_name: Optional[EntityObjectStringType] = field(
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
class SidSidObject(ObjectType):
    """The sid_sid_object element is used by a sid_sid_test to define the object
    set, in this case a set of SIDs, to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).
    :ivar filter:
    """

    class Meta:
        name = "sid_sid_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[SidSidBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class SidSidState(StateType):
    """The sid_state element defines the different metadata associate with a
    Windows trustee (identified by SID).

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar trustee_sid: The security identifier (SID) of the specified
        trustee name.
    :ivar trustee_name: This element specifies the trustee name
        associated with a particular SID. In Windows, trustee names are
        case-insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, trustee names should be identified in the form:
        "domain\\trustee name". For local trustee names use: "computer
        name\\trustee name". For built-in accounts on the system, use
        the trustee name without a domain.
    :ivar trustee_domain: The domain of the specified trustee name.
    """

    class Meta:
        name = "sid_sid_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_domain: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SidSidTest(TestType):
    """The sid_sid_test is used to check properties associated with the specified
    SID.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a sid_sid_object
    and the optional state element specifies the metadata to check. Note
    that this sid_sid test was added in version 5.4 as a temporary fix.
    There is a need within the community to identify things like users
    and groups by both the name and the SID.  For version 6 of OVAL,
    work is underway for a better solution to the problem, but for now,
    a second test was added to satisfy the need.
    """

    class Meta:
        name = "sid_sid_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class SidState(StateType):
    """The sid_state element defines the different metadata associate with a
    Windows trustee (identified by name).

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar trustee_name: This element specifies the trustee name
        associated with a particular SID. In Windows, trustee names are
        case-insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, trustee names should be identified in the form:
        "domain\\trustee name". For local trustee names use: "computer
        name\\trustee name". For built-in accounts on the system, use
        the trustee name without a domain.
    :ivar trustee_sid: The security identifier (SID) of the specified
        trustee name.
    :ivar trustee_domain: The domain of the specified trustee name.
    """

    class Meta:
        name = "sid_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    trustee_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_domain: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SidTest(TestType):
    """The SID test is used to check properties associated with the specified SID.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a sid_object and
    the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "sid_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class SystemmetricTest(TestType):
    """The system metric test is used to check the value of a particular Windows
    system metric.

    Access to this information is exposed by the GetSystemMetrics
    function in User32.dll.
    """

    class Meta:
        name = "systemmetric_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class UacObject(ObjectType):
    """The uac_object element is used by a user access control test to define those
    objects to evaluate based on a specified state.

    There is actually only one object relating to user access control
    and this is the system as a whole. Therefore, there are no child
    entities defined. Any OVAL Test written to check user access control
    settings will reference the same uac_object which is basically an
    empty object element.
    """

    class Meta:
        name = "uac_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )


@dataclass
class UacState(StateType):
    """The uac_state element specifies the different settings that are available
    under User Access Control.

    A user access control test will reference a specific instance of
    this state that defines the exact settings that need to be
    evaluated. Please refer to the individual elements in the schema for
    more details about what each represents.

    :ivar admin_approval_mode: Admin Approval Mode for the Built-in
        Administrator account.
    :ivar elevation_prompt_admin: Behavior of the elevation prompt for
        administrators in Admin Approval Mode.
    :ivar elevation_prompt_standard: Behavior of the elevation prompt
        for standard users.
    :ivar detect_installations: Detect application installations and
        prompt for elevation.
    :ivar elevate_signed_executables: Only elevate executables that are
        signed and validated.
    :ivar elevate_uiaccess: Only elevate UIAccess applications that are
        installed in secure locations.
    :ivar run_admins_aam: Run all administrators in Admin Approval Mode.
    :ivar secure_desktop: Switch to the secure desktop when prompting
        for elevation.
    :ivar virtualize_write_failures: Virtualize file and registry write
        failures to per-user locations.
    """

    class Meta:
        name = "uac_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    admin_approval_mode: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elevation_prompt_admin: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elevation_prompt_standard: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detect_installations: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elevate_signed_executables: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elevate_uiaccess: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    run_admins_aam: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    secure_desktop: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    virtualize_write_failures: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UacTest(TestType):
    """The user access control test is used to check setting related to User Access
    Control within Windows.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a uaac_object
    and the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "uac_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class UserObject(ObjectType):
    """
    :ivar set:
    :ivar user: The user entity holds a string that represents the name
        of a particular user. In Windows, user names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, users should be identified in the form:
        "domain\\user name". For local users use: "computer name\\user
        name". For built-in accounts on the system, use the user name
        without a domain.
    :ivar filter:
    """

    class Meta:
        name = "user_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    user: Optional[EntityObjectStringType] = field(
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
class UserSid55Object(ObjectType):
    """The user_sid55_object represents a set of users on a Windows system.

    This set (which might contain only one user) is identified by a SID.

    :ivar set:
    :ivar user_sid: The user_sid entity holds a string that represents
        the SID of a particular user.
    :ivar filter:
    """

    class Meta:
        name = "user_sid55_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    user_sid: Optional[EntityObjectStringType] = field(
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
class UserSid55State(StateType):
    """The user_sid55_state element enumerates the different groups (identified by
    SID) that a Windows user might belong to.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar user_sid: The user_sid entity holds a string that represents
        the SID of a particular user.
    :ivar enabled: This element holds a boolean value that specifies
        whether the particular user account is enabled or not.
    :ivar group_sid: A string the represents the SID of a particular
        group.  The group_sid element can be included multiple times in
        a system characteristic item in order to record that a user can
        be a member of a number of different groups. Note that the
        entity_check attribute associated with EntityStateStringType
        guides the evaluation of entities like group that refer to items
        that can occur an unbounded number of times.
    :ivar last_logon: The date and time when the last logon occurred.
        This value is stored as the number of seconds that have elapsed
        since 00:00:00, January 1, 1970, GMT.
    """

    class Meta:
        name = "user_sid55_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    user_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enabled: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    last_logon: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UserSid55Test(TestType):
    """The user_sid55_test is used to check information about Windows users.

    When the user_sid55_test collects the user SIDs on the system, it
    should only include the local and built-in user SIDs and not domain
    user SIDs.  However, it is important to note that domain user SIDs
    can still be looked up. Also, note that the collection of groups,
    for which a user is a member, is not recursive. The only groups that
    will be collected are those for which the user is a direct member.
    For example, if a user is a member of group A, and group A is a
    member of group B, the only group that will be collected is group A.
    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    user_sid55_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "user_sid55_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class UserSidObject(ObjectType):
    """The user_sid_object represents a set of users on a Windows system.

    This set (which might contain only one user) is identified by a SID.

    :ivar set:
    :ivar user: The user_sid entity holds a string that represents the
        SID of a particular user.
    """

    class Meta:
        name = "user_sid_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    user: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UserSidState(StateType):
    """The user_sid_state element enumerates the different groups (identified by
    SID) that a Windows user might belong to.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar user: The user_sid entity holds a string that represents the
        SID of a particular user.
    :ivar enabled: This element holds a boolean value that specifies
        whether the particular user account is enabled or not.
    :ivar group: A string the represents the SID of a particular group.
        The group_sid element can be included multiple times in a system
        characteristic item in order to record that a user can be a
        member of a number of different groups. Note that the
        entity_check attribute associated with EntityStateStringType
        guides the evaluation of entities like group that refer to items
        that can occur an unbounded number of times.
    """

    class Meta:
        name = "user_sid_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    user: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enabled: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UserSidTest(TestType):
    """The user_sid_test is used to check information about Windows users.

    When the user_sid_test collects the user SIDs on the system, it
    should only include the local and built-in user SIDs and not domain
    user SIDs.  However, it is important to note that domain user SIDs
    can still be looked up. Also, note that the collection of groups,
    for which a user is a member, is not recursive. The only groups that
    will be collected are those for which the user is a direct member.
    For example, if a user is a member of group A, and group A is a
    member of group B, the only group that will be collected is group A.
    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    user_sid_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "user_sid_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class UserState(StateType):
    """The user_state element enumerates the different groups (identified by name)
    that a Windows user might belong to.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar user: The user entity holds a string that represents the name
        of a particular user. In Windows, user names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, users should be identified in the form:
        "domain\\user name". For local users use: "computer name\\user
        name". For built-in accounts on the system, use the user name
        without a domain.
    :ivar enabled: This element holds a boolean value that specifies
        whether the particular user account is enabled or not.
    :ivar group: A string that represents the name of a particular
        group. In Windows, group names are case-insensitive. As a
        result, it is recommended that the case-insensitive operations
        are used for this entity. In a domain environment, groups should
        be identified in the form: "domain\\group name". For local
        groups use: "computer name\\group name". For built-in accounts
        on the system, use the group name without a domain. The group
        element can be included multiple times in a system
        characteristic item in order to record that a user can be a
        member of a number of different groups. Note that the
        entity_check attribute associated with EntityStateStringType
        guides the evaluation of entities like group that refer to items
        that can occur an unbounded number of times.
    :ivar last_logon: The date and time when the last logon occurred.
        This value is stored as the number of seconds that have elapsed
        since 00:00:00, January 1, 1970, GMT.
    """

    class Meta:
        name = "user_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    user: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enabled: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    group: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    last_logon: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UserTest(TestType):
    """The user_test is used to check information about Windows users.

    When the user_test collects the users on the system, it should only
    include the local and built-in user accounts and not domain user
    accounts.  However, it is important to note that domain user
    accounts can still be looked up. Also, note that the collection of
    groups, for which a user is a member, is not recursive. The only
    groups that will be collected are those for which the user is a
    direct member. For example, if a user is a member of group A, and
    group A is a member of group B, the only group that will be
    collected is group A. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a user_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "user_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class UserrightTest(TestType):
    """
    The userright_test is used to enumerate all of the SIDs that have been granted
    a specific user right/privilege.
    """

    class Meta:
        name = "userright_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class VolumeObject(ObjectType):
    """The volume_object element is used by a volume test to define the specific
    volume(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A volume object defines the rootpath of the
    volume(s).

    :ivar set:
    :ivar rootpath: A string that contains the root directory of the
        volume to be described. A trailing backslash is required. For
        example, you would specify \\\\MyServer\\MyShare as
        "\\\\MyServer\\MyShare\\", or the C drive as "C:\\".
    :ivar filter:
    """

    class Meta:
        name = "volume_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    rootpath: Optional[EntityObjectStringType] = field(
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
class VolumeTest(TestType):
    """The volume_test is used to check information about different storage volumes
    found on a Windows system.

    This includes the various system flags returned by
    GetVolumeInformation(). It is important to note that these system
    flags are specific to certain versions of Windows.  As a result, the
    documentation for that version of Windows should be consulted for
    more information. It extends the standard TestType as defined in the
    oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a volume_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "volume_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class Wmi57Object(ObjectType):
    """
    :ivar set:
    :ivar namespace: Specifies which WMI namespace to look under. Each
        WMI provider normally registers its own WMI namespace and then
        all its classes within that namespace. For example, all Win32
        WMI classes can be found in the namespace "root\\cimv2", all IIS
        WMI classes can be found at "root\\microsoftiisv2", and all LDAP
        WMI classes can be found at "root\\directory\\ldap".
    :ivar wql: A WQL query used to identify the object(s) to test
        against. Any valid WQL query is usable with one exception, all
        fields must be named in the SELECT portion of the query. For
        example SELECT name, age FROM ... is valid. However, SELECT *
        FROM ... is not valid. This is because the record element in the
        state and item require a unique field name value to ensure that
        any query results can be evaluated consistently.
    :ivar filter:
    """

    class Meta:
        name = "wmi57_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    namespace: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wql: Optional[EntityObjectStringType] = field(
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
class Wmi57State(StateType):
    """
    :ivar namespace: Specifies which WMI namespace to look under. Each
        WMI provider normally registers its own WMI namespace and then
        all its classes within that namespace. For example, all Win32
        WMI classes can be found in the namespace "root\\cimv2", all IIS
        WMI classes can be found at "root\\microsoftiisv2", and all LDAP
        WMI classes can be found at "root\\directory\\ldap".
    :ivar wql: A WQL query used to identify the object(s) to test
        against. Any valid WQL query is usable with one exception, all
        fields must be named in the SELECT portion of the query. For
        example SELECT name, age FROM ... is valid. However, SELECT *
        FROM ... is not valid. This is because the record element in the
        state and item require a unique field name value to ensure that
        any query results can be evaluated consistantly.
    :ivar result: The result element specifies how to test items in the
        result set of the specified WQL statement.
    """

    class Meta:
        name = "wmi57_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    namespace: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wql: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Wmi57Test(TestType):
    """The wmi57 test is used to check information accessed by WMI.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a wmi57_object
    and the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "wmi57_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class WmiObject(ObjectType):
    """
    :ivar set:
    :ivar namespace: Specifies which WMI namespace to look under. Each
        WMI provider normally registers its own WMI namespace and then
        all its classes within that namespace. For example, all Win32
        WMI classes can be found in the namespace "root\\cimv2", all IIS
        WMI classes can be found at "root\\microsoftiisv2", and all LDAP
        WMI classes can be found at "root\\directory\\ldap".
    :ivar wql: A WQL query used to identify the object(s) to test
        against. Any valid WQL query is usable with one exception, at
        most one field is allowed in the SELECT portion of the query.
        For example SELECT name FROM ... is valid, as is SELECT 'true'
        FROM ..., but SELECT name, number FROM ... is not valid. This is
        because the result element in the data section is only designed
        to work against a single field.
    """

    class Meta:
        name = "wmi_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    namespace: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wql: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class WmiState(StateType):
    """
    :ivar namespace: Specifies which WMI namespace to look under. Each
        WMI provider normally registers its own WMI namespace and then
        all its classes within that namespace. For example, all Win32
        WMI classes can be found in the namespace "root\\cimv2", all IIS
        WMI classes can be found at "root\\microsoftiisv2", and all LDAP
        WMI classes can be found at "root\\directory\\ldap".
    :ivar wql: A WQL query used to identify the object(s) to test
        against. Any valid WQL query is usable with one exception, at
        most one field is allowed in the SELECT portion of the query.
        For example SELECT name FROM ... is valid, as is SELECT 'true'
        FROM ..., but SELECT name, number FROM ... is not valid. This is
        because the result element in the data section is only designed
        to work against a single field.
    :ivar result: The result element specifies how to test objects in
        the result set of the specified WQL statement. Only one
        comparable field is allowed. So if the WQL statement look like
        'SELECT name FROM ...', then a result element with a value of
        'Fred' would test that value against the names returned by the
        WQL statement.
    """

    class Meta:
        name = "wmi_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    namespace: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    wql: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class WmiTest(TestType):
    """The wmi test is used to check information accessed by WMI.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a wmi_object and
    the optional state element specifies the metadata to check.
    """

    class Meta:
        name = "wmi_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class WuaupdatesearcherObject(ObjectType):
    """The wuaupdatesearcher_object element is used by a wuaupdatesearcher_test to
    define the specific search criteria to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar search_criteria: The search_criteria entity specifies a search
        criteria to use when generating a search result.  The string
        used for the search criteria entity must match the custom search
        language for Search method of the IUpdateSearcher interface.
        The string consists of criteria that are evaluated to determine
        which updates to return.  The Search method performs a
        synchronous search for updates by using the current configured
        search options.   For more information about possible search
        criteria, please see the Search method of the IUpdateSearcher
        interface.
    :ivar filter:
    """

    class Meta:
        name = "wuaupdatesearcher_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[WuaUpdateSearcherBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    search_criteria: Optional[EntityObjectStringType] = field(
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
class WuaupdatesearcherState(StateType):
    """The wuaupdatesearcher_state element defines entities that can be tested
    related to a uaupdatesearcher_object.

    This includes the search criteria and updated id.  Please refer to
    the individual elements in the schema for more details about what
    each represents.

    :ivar search_criteria: The search_criteria entity specifies a string
        to examine the search criteria that was used to generate the
        object set.  Note that since this entity is part of the state,
        it is not used to determine the object set, but rather is used
        to test the search criteria that was actually used.
    :ivar update_id: The update_id enity specifies a string that
        represents a revision-independent identifier of an update.  This
        information is part of the IUpdateIdentity interface that is
        part of the result of the IUpdateSearcher interface's Search
        method.
    """

    class Meta:
        name = "wuaupdatesearcher_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    search_criteria: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_id: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class WuaupdatesearcherTest(TestType):
    """The wuaupdatesearcher_test is used to evaluate patch level in a Windows
    environment utilizing the WUA (Windows Update Agent) interface.

    It is based on the Search method of the IUpdateSearcher interface
    found in the WUA API.  It extends the standard TestType as defined
    in the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a wuaupdatesearcher_object and the optional state element
    specifies the metadata to check. Note that WUA can work off of many
    different sources including WSUS, update.microsoft.com, and a local
    cab file.  The content source is specific to a given system
    evaluating a wuaupdatesearcher_test and thus is not defined by this
    test.  The tool being used for evaluation should determine what
    content source is best for the system being assessed and then
    evaluate this test based on that selection.
    """

    class Meta:
        name = "wuaupdatesearcher_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class FileAuditPermissions53Behaviors(FileBehaviors):
    """The FileAuditPermissions53Behaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    fileauditpermissions53_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file. The
    FileAuditPermissions53Behaviors extend the win-def:FileBehaviors and
    therefore include the behaviors defined by that type.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FileAuditPermissionsBehaviors(FileBehaviors):
    """The FileAuditPermissionsBehaviors complex type defines a number of behaviors
    that allow a more detailed definition of the fileauditpermissions_object being
    specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. The
    FileAuditPermissionsBehaviors extend the win-def:FileBehaviors and
    therefore include the behaviors defined by that type.

    :ivar include_group: 'include_group' defines whether the group
        trustee name should be included in the object when the object is
        defined by a group trustee name. For example, the intent of an
        object defined by a group trustee name might be to retrieve all
        the user SIDs that are a member of the group, but not the group
        trustee name itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FileEffectiveRights53Behaviors(FileBehaviors):
    """The FileEffectiveRights53Behaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    fileeffectiverights53_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file. The
    FileEffectiveRights53Behaviors extend the win-def:FileBehaviors and
    therefore include the behaviors defined by that type.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FileEffectiveRightsBehaviors(FileBehaviors):
    """The FileEffectiveRightsBehaviors complex type defines a number of behaviors
    that allow a more detailed definition of the fileeffectiverights_object being
    specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. The
    FileEffectiveRightsBehaviors extend the win-def:FileBehaviors and
    therefore include the behaviors defined by that type.

    :ivar include_group: 'include_group' defines whether the group
        trustee name should be included in the object when the object is
        defined by a group trustee name. For example, the intent of an
        object defined by a group SID might be to retrieve all the user
        trustee names that are members of the group, but not the group
        trustee name itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegkeyAuditPermissions53Behaviors(RegistryBehaviors):
    """The RegkeyAuditPermissions53Behaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    registrykeyauditedpermissions53_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. The
    RegkeyAuditPermissions53Behaviors extend the win-
    def:RegistryBehaviors and therefore include the behaviors defined by
    that type.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegkeyAuditPermissionsBehaviors(RegistryBehaviors):
    """The RegkeyAuditPermissionsBehaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    registrykeyauditedpermissions_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. The
    RegkeyAuditPermissionsBehaviors extend the win-def:RegistryBehaviors
    and therefore include the behaviors defined by that type.

    :ivar include_group: 'include_group' defines whether the group
        trustee name should be included in the object when the object is
        defined by a group trustee name. For example, the intent of an
        object defined by a group trustee name might be to retrieve all
        the user trustee names that are members of the group, but not
        the group trustee name itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegkeyEffectiveRights53Behaviors(RegistryBehaviors):
    """The RegkeyEffectiveRights53Behaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    registrykeyeffectiverights53_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. The
    RegkeyEffectiveRights53Behaviors extend the win-
    def:RegistryBehaviors and therefore include the behaviors defined by
    that type.

    :ivar include_group: 'include_group' defines whether the group SID
        should be included in the object when the object is defined by a
        group SID. For example, the intent of an object defined by a
        group SID might be to retrieve all the user SIDs that are a
        member of the group, but not the group SID itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegkeyEffectiveRightsBehaviors(RegistryBehaviors):
    """The RegkeyEffectiveRightsBehaviors complex type defines a number of
    behaviors that allow a more detailed definition of the
    registrykeyeffectiverights_object being specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. The
    RegkeyEffectiveRightsBehaviors extend the win-def:RegistryBehaviors
    and therefore include the behaviors defined by that type.

    :ivar include_group: 'include_group' defines whether the group
        trustee name should be included in the object when the object is
        defined by a group trustee name. For example, the intent of an
        object defined by a group trustee name might be to retrieve all
        the user trustee names that are members of the group, but not
        the group trustee name itself.
    :ivar resolve_group: The 'resolve_group' behavior defines whether an
        object set defined by a group SID should be resolved to return a
        set that contains all the user SIDs that are a member of that
        group.  Note that all child groups should also be resolved any
        valid domain users that are members of the group should also be
        included.  The intent of this behavior is to end up with a list
        of all individual users from that system that make up the group
        once everything has been resolved.
    """

    include_group: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_group: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Activedirectory57Object(ObjectType):
    """The activedirectory57_object element is used by an active directory test to
    define those objects to evaluated based on a specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An active directory object consists of three
    pieces of information, a naming context, a relative distinguished
    name, and an attribute. Each piece helps identify a specific active
    directory entry. Note that this object supports complex values that
    are in the form of a record. For simple (string based) value
    collection see the activedirectory_object.

    :ivar set:
    :ivar naming_context: Each object in active directory exists under a
        certain naming context (also known as a partition). A naming
        context is defined as a single object in the Directory
        Information Tree (DIT) along with every object in the tree
        subordinate to it. There are three default naming contexts in
        Active Directory: domain, configuration, and schema.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified naming context. It
        contains all the parts of the object's distinguished name except
        those outlined by the naming context. If the xsi:nil attribute
        is set to true, then the object being specified is the higher
        level naming context. In this case, the relative_dn element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every relative dn under a given naming context.
    :ivar attribute: Specifies a named value contained by the object. If
        the xsi:nil attribute is set to true, the attribute element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every attribute under a given relative dn.
    :ivar filter:
    """

    class Meta:
        name = "activedirectory57_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    naming_context: Optional[EntityObjectNamingContextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute: Optional[EntityObjectStringType] = field(
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
class Activedirectory57State(StateType):
    """The activedirectory57_state element defines the different information that
    can be used to evaluate the specified entries in active directory.

    An active directory test will reference a specific instance of this
    state that defines the exact settings that need to be evaluated.
    Please refer to the individual elements in the schema for more
    details about what each represents. Note that this state supports
    complex values that are in the form of a record. For simple (string
    based) value collection see the activedirectory_state.

    :ivar naming_context: Each object in active directory exists under a
        certain naming context (also known as a partition). A naming
        context is defined as a single object in the Directory
        Information Tree (DIT) along with every object in the tree
        subordinate to it. There are three default naming contexts in
        Active Directory: domain, configuration, and schema.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified naming context. It
        contains all the parts of the object's distinguished name except
        those outlined by the naming context.
    :ivar attribute: Specifies a named value contained by the object.
    :ivar object_class: The name of the class of which the object is an
        instance.
    :ivar adstype: The type of information that the specified attribute
        represents.
    :ivar value: The actual value of the specified Active Directory
        attribute. Note that while an Active Directory attribute can
        contain structured data where it is necessary to collect
        multiple related fields that can be described by the 'record'
        datatype, it is not always the case.  It also is possible that
        an Active Directory attribute can contain only a single value or
        an array of values. In these cases, there is not a name to
        uniquely identify the corresponding field which is a requirement
        for fields in the 'record' datatype.  As a result, the name of
        the Active Directory attribute will be used to uniquely identify
        the field and satisfy this requirement.
    """

    class Meta:
        name = "activedirectory57_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    naming_context: Optional[EntityStateNamingContextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    object_class: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    adstype: Optional[EntityStateAdstypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ActivedirectoryObject(ObjectType):
    """The activedirectory_object element is used by an active directory test to
    define those objects to evaluated based on a specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. An active directory object consists of three
    pieces of information, a naming context, a relative distinguished
    name, and an attribute. Each piece helps identify a specific active
    directory entry. Note that this object is paired with a state that
    supports only simple (string based) value collection. For more
    complex values see the activedirectory57_object.

    :ivar set:
    :ivar naming_context: Each object in active directory exists under a
        certain naming context (also known as a partition). A naming
        context is defined as a single object in the Directory
        Information Tree (DIT) along with every object in the tree
        subordinate to it. There are three default naming contexts in
        Active Directory: domain, configuration, and schema.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified naming context. It
        contains all the parts of the object's distinguished name except
        those outlined by the naming context. If the xsi:nil attribute
        is set to true, then the object being specified is the higher
        level naming context. In this case, the relative_dn element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every relative dn under a given naming context.
    :ivar attribute: Specifies a named value contained by the object. If
        the xsi:nil attribute is set to true, the attribute element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every attribute under a given relative dn.
    """

    class Meta:
        name = "activedirectory_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    naming_context: Optional[EntityObjectNamingContextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )


@dataclass
class ActivedirectoryState(StateType):
    """The activedirectory_state element defines the different information that can
    be used to evaluate the specified entries in active directory.

    An active directory test will reference a specific instance of this
    state that defines the exact settings that need to be evaluated.
    Please refer to the individual elements in the schema for more
    details about what each represents. Note that this state supports
    only simple (string based) value collection. For more complex values
    see the activedirectory57_state.

    :ivar naming_context: Each object in active directory exists under a
        certain naming context (also known as a partition). A naming
        context is defined as a single object in the Directory
        Information Tree (DIT) along with every object in the tree
        subordinate to it. There are three default naming contexts in
        Active Directory: domain, configuration, and schema.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified naming context. It
        contains all the parts of the objects distinguished name except
        those outlined by the naming context.
    :ivar attribute: Specifies a named value contained by the object.
    :ivar object_class: The name of the class of which the object is an
        instance.
    :ivar adstype: Specifies the type of information that the specified
        attribute represents.
    :ivar value: The actual value of the specified active directory
        attribute.
    """

    class Meta:
        name = "activedirectory_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    naming_context: Optional[EntityStateNamingContextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    object_class: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    adstype: Optional[EntityStateAdstypeType] = field(
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
class AuditeventpolicyState(StateType):
    """The auditeventpolicy_state element specifies the different system activities
    that can be audited.

    An audit event policy test will reference a specific instance of
    this state that defines the exact settings that need to be
    evaluated. The defined values are found in window's
    POLICY_AUDIT_EVENT_TYPE enumeration and accessed through the
    LsaQueryInformationPolicy when the InformationClass parameters are
    set to PolicyAuditEventsInformation. Please refer to the individual
    elements in the schema for more details about what each represents.

    :ivar account_logon: Audit attempts to log on to or log off of the
        system. Also, audit attempts to make a network connection.
    :ivar account_management: Audit attempts to create, delete, or
        change user or group accounts. Also, audit password changes.
    :ivar detailed_tracking: Audit specific events, such as program
        activation, some forms of handle duplication, indirect access to
        an object, and process exit.  Note that this activitiy is also
        known as process tracking.
    :ivar directory_service_access: Audit attempts to access the
        directory service.
    :ivar logon: Audit attempts to log on to or log off of the system.
        Also, audit attempts to make a network connection.
    :ivar object_access: Audit attempts to access securable objects,
        such as files.
    :ivar policy_change: Audit attempts to change Policy object rules.
    :ivar privilege_use: Audit attempts to use privileges.
    :ivar system: Audit attempts to shut down or restart the computer.
        Also, audit events that affect system security or the security
        log.
    """

    class Meta:
        name = "auditeventpolicy_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    account_logon: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    account_management: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detailed_tracking: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    directory_service_access: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    logon: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    object_access: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    policy_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    privilege_use: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    system: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class AuditeventpolicysubcategoriesState(StateType):
    """The auditeventpolicysubcategories_state element specifies the different
    system activities that can be audited.

    An audit event policy subcategories test will reference a specific
    instance of this state that defines the exact subcategories that
    need to be evaluated. Please refer to the individual elements in the
    schema for more details about what each represents.

    :ivar credential_validation: Audit the events produced during the
        validation of a user's logon credentials. This state corresponds
        with the following GUID specified in ntsecapi.h:
        0cce923f-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Logon: Audit
        Credential Validation
    :ivar kerberos_authentication_service: Audit the events produced by
        Kerberos authentication ticket-granting requests. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0CCE9242-69AE-11D9-BED3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Logon: Audit
        Kerboros Authentication Service
    :ivar kerberos_service_ticket_operations: Audit the events produced
        by Kerberos service ticket requests. This state corresponds with
        the following GUID specified in ntsecapi.h:
        0cce9240-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Logon: Audit
        Kerberos Service Ticket Operations
    :ivar kerberos_ticket_events: Audit the events produced during the
        validation of Kerberos tickets provided for a user account logon
        request.
    :ivar other_account_logon_events: Audit the events produced by
        changes to user accounts that are not covered by other events in
        the Account Logon category. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9241-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Logon: Audit
        Other Account Logon Events
    :ivar application_group_management: Audit the events produced by
        changes to application groups. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9239-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Management:
        Audit Application Group Management
    :ivar computer_account_management: Audit the events produced by
        changes to computer accounts. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9236-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Management:
        Audit Computer Account Management
    :ivar distribution_group_management: Audit the events produced by
        changes to distribution groups. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9238-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Management:
        Audit Distribution Account Management
    :ivar other_account_management_events: Audit the events produced by
        other user account changes that are not covered by other events
        in the Account Management category. This state corresponds with
        the following GUID specified in ntsecapi.h:
        0cce923a-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Management:
        Audit Other Account Management Events
    :ivar security_group_management: Audit the events produced by
        changes to security groups. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9237-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Account Management:
        Audit Security Group Management
    :ivar user_account_management: Audit the events produced by changes
        to user accounts. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce9235-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Account Management: Audit User Account Management
    :ivar dpapi_activity: Audit the events produced when requests are
        made to the Data Protection application interface. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce922d-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Detailed Tracking:
        Audit DPAPI Activity
    :ivar process_creation: Audit the events produced when a process is
        created or starts. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce922b-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Detailed Tracking:
        Audit Process Creation
    :ivar process_termination: Audit the events produced when a process
        ends. This state corresponds with the following GUID specified
        in ntsecapi.h: 0cce922c-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:  Detailed
        Tracking: Audit Process Termination
    :ivar rpc_events: Audit the events produced by inbound remote
        procedure call connections. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce922e-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Detailed Tracking:
        Audit RPC Events
    :ivar directory_service_access: Audit the events produced when a
        Active Directory Domain Services object is accessed. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce923b-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  DS Access: Audit
        Directory Service Access
    :ivar directory_service_changes: Audit the events produced when
        changes are made to Active Directory Domain Services objects.
        This state corresponds with the following GUID specified in
        ntsecapi.h: 0cce923c-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:  DS
        Access: Audit Directory Service Changes
    :ivar directory_service_replication: Audit the events produced when
        two Active Directory Domain Services domain controllers are
        replicated. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce923d-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        DS Access: Audit Directory Service Access
    :ivar detailed_directory_service_replication: Audit the events
        produced by detailed Active Directory Domain Services
        replication between domain controllers. This state corresponds
        with the following GUID specified in ntsecapi.h:
        0cce923e-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  DS Access: Audit
        Detailed Directory Service Replication
    :ivar account_lockout: Audit the events produced by a failed attempt
        to log onto a locked out account. This state corresponds with
        the following GUID specified in ntsecapi.h:
        0cce9217-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Logon/Logoff: Audit
        Account Lockout
    :ivar ipsec_extended_mode: Audit the events produced by Internet Key
        Exchange and Authenticated Internet protocol during Extended
        Mode negotiations. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce921a-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Logon/Logoff: Audit
        IPsec Extended Mode
    :ivar ipsec_main_mode: Audit the events produced by Internet Key
        Exchange and Authenticated Internet protocol during Main Mode
        negotiations. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce9218-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Logof/Logoff: Audit IPsec Main Mode
    :ivar ipsec_quick_mode: Audit the events produced by Internet Key
        Exchange and Authenticated Internet protocol during Quick Mode
        negotiations. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce9219-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Logon/Logoff: Audit IPsec Quick Mode
    :ivar logoff: Audit the events produced by closing a logon session.
        This state corresponds with the following GUID specified in
        ntsecapi.h: 0cce9216-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:
        Logon/Logoff: Audit Logoff
    :ivar logon: Audit the events produced by attempts to log onto a
        user account. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce9215-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Logon/Logoff: Audit Logon
    :ivar network_policy_server: Audit the events produced by RADIUS and
        Network Access Protection user access requests. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9243-69ae-11d9-bed3-505054503030.This state corresponds with
        the following Advanced Audit Policy:  Logon/Logoff: Audit
        Network Policy Server
    :ivar other_logon_logoff_events: Audit the events produced by other
        logon/logoff based events that are not covered in the
        Logon/Logoff category. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce921c-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Logon/Logoff: Audit
        Other Logon/Logoff Events
    :ivar special_logon: Audit the events produced by special logons.
        This state corresponds with the following GUID specified in
        ntsecapi.h: 0cce921b-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:
        Logon/Logoff: Audit Special Logon
    :ivar logon_claims: Audit user and device claims information in the
        user's logon token. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce9247-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Logon/Logoff: Audit
        User / Device Claims
    :ivar application_generated: Audit the events produced by
        applications that use the Windows Auditing API. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9222-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Audit
        Application Generated
    :ivar certification_services: Audit the events produced by
        operations on Active Directory Certificate Services. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9221-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Audit
        Certification Services
    :ivar detailed_file_share: Audit the events produced by attempts to
        access files and folders on a shared folder. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9244-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Audit
        Detailed File Share
    :ivar file_share: Audit the events produced by attempts to access a
        shared folder. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce9224-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Object Access: Audit File Share
    :ivar file_system: Audit the events produced user attempts to access
        file system objects. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce921d-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Audit
        File System
    :ivar filtering_platform_connection: Audit the events produced by
        connections that are allowed or blocked by Windows Filtering
        Platform. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce9226-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Object Access: Audit Filtering Platform Connection
    :ivar filtering_platform_packet_drop: Audit the events produced by
        packets that are dropped by Windows Filtering Platform. This
        state corresponds with the following GUID specified in
        ntsecapi.h: 0cce9225-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:  Object
        Access: Audit Filtering Platform Packet Drop
    :ivar handle_manipulation: Audit the events produced when a handle
        is opened or closed. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce9223-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Handle
        Manipulation
    :ivar kernel_object: Audit the events produced by attempts to access
        the system kernel. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce921f-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Kernel
        Object
    :ivar other_object_access_events: Audit the events produced by the
        management of Task Scheduler jobs or COM+ objects. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9227-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Other
        Object Access Events
    :ivar registry: Audit the events produced by attempts to access
        registry objects. This state corresponds with the following GUID
        specified in ntsecapi.h: 0cce921e-69ae-11d9-bed3-505054503030.
        This state corresponds with the following Advanced Audit Policy:
        Object Access: Audit Registry
    :ivar sam: Audit the events produced by attempts to access Security
        Accounts Manager objects. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9220-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Audit
        SAM
    :ivar removable_storage: Audit events that indicate file object
        access attemps to removable storage. This state corresponds with
        the following GUID specified in ntsecapi.h:
        0cce9245-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access: Audit
        Removable Storage
    :ivar central_access_policy_staging: Audit events that indicate
        permission granted or denied by a proposed policy differs from
        the current central access policy on an object. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9246-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Object Access:
        Central Access Policy Staging
    :ivar audit_policy_change: Audit the events produced by changes in
        security audit policy settings. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce922f-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Policy Change: Audit
        Audit Policy Change
    :ivar authentication_policy_change: Audit the events produced by
        changes to the authentication policy. This state corresponds
        with the following GUID specified in ntsecapi.h:
        0cce9230-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Policy Change: Audit
        Authentication Policy Change
    :ivar authorization_policy_change: Audit the events produced by
        changes to the authorization policy. This state corresponds with
        the following GUID specified in ntsecapi.h:
        0cce9231-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Policy Change: Audit
        Authorization Policy Change
    :ivar filtering_platform_policy_change: Audit the events produced by
        changes to the Windows Filtering Platform. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9233-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Policy Change: Audit
        Filtering Platform Policy Change
    :ivar mpssvc_rule_level_policy_change: Audit the events produced by
        changes to policy rules used by the Windows Firewall. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9232-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Policy Change: Audit
        MPSSVC Rule-Level Policy Change
    :ivar other_policy_change_events: Audit the events produced by other
        security policy changes that are not covered other events in the
        Policy Change category. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9234-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Policy Change: Audit
        Other Policy Change Events
    :ivar non_sensitive_privilege_use: Audit the events produced by the
        use of non-sensitive privileges. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9229-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Privilege Use: Audit
        Non Sensitive Privilege Use
    :ivar other_privilege_use_events: This is currently not used and has
        been reserved by Microsoft for use in the future. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce922a-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Privilege Use: Audit
        Other Privilege Use Events
    :ivar sensitive_privilege_use: Audit the events produced by the use
        of sensitive privileges. This state corresponds with the
        following GUID specified in ntsecapi.h:
        0cce9228-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  Privilege Use: Audit
        Sensitive Privilege Use
    :ivar ipsec_driver: Audit the events produced by the IPsec filter
        driver. This state corresponds with the following GUID specified
        in ntsecapi.h: 0cce9213-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:  System:
        Audit IPsec Driver
    :ivar other_system_events: Audit the events produced by the startup
        and shutdown, security policy processing, and cryptography key
        file and migration operations of the Windows Firewall. This
        state corresponds with the following GUID specified in
        ntsecapi.h: 0cce9214-69ae-11d9-bed3-505054503030. This state
        corresponds with the following Advanced Audit Policy:  System:
        Audit Other System Events
    :ivar security_state_change: Audit the events produced by changes in
        the security state. This state corresponds with the following
        GUID specified in ntsecapi.h:
        0cce9210-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy:  System: Audit
        Security State Change
    :ivar security_system_extension: Audit the events produced by the
        security system extensions or services. This state corresponds
        with the following GUID specified in ntsecapi.h:
        cce9211-69ae-11d9-bed3-505054503030. This state corresponds with
        the following Advanced Audit Policy:  System: Audit Security
        System Extension
    :ivar system_integrity: Audit the events that indicate that the
        integrity security subsystem has been violated. This state
        corresponds with the following GUID specified in ntsecapi.h:
        0cce9212-69ae-11d9-bed3-505054503030. This state corresponds
        with the following Advanced Audit Policy: System: Audit System
        Integrity
    """

    class Meta:
        name = "auditeventpolicysubcategories_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    credential_validation: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    kerberos_authentication_service: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    kerberos_service_ticket_operations: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    kerberos_ticket_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_account_logon_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    application_group_management: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    computer_account_management: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    distribution_group_management: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_account_management_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    security_group_management: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    user_account_management: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dpapi_activity: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    process_creation: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    process_termination: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rpc_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    directory_service_access: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    directory_service_changes: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    directory_service_replication: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detailed_directory_service_replication: Optional[EntityStateAuditType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )
    account_lockout: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ipsec_extended_mode: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ipsec_main_mode: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ipsec_quick_mode: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    logoff: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    logon: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    network_policy_server: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_logon_logoff_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    special_logon: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    logon_claims: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    application_generated: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    certification_services: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detailed_file_share: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_share: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_system: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filtering_platform_connection: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filtering_platform_packet_drop: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    handle_manipulation: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    kernel_object: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_object_access_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    registry: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sam: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    removable_storage: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    central_access_policy_staging: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    audit_policy_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    authentication_policy_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    authorization_policy_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filtering_platform_policy_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mpssvc_rule_level_policy_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_policy_change_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    non_sensitive_privilege_use: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_privilege_use_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sensitive_privilege_use: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ipsec_driver: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    other_system_events: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    security_state_change: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    security_system_extension: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    system_integrity: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CmdletObject(ObjectType):
    """The cmdlet_object element is used by a cmdlet_test to identify the set of
    cmdlets to use and the parameters to provide to them for checking the state of
    a system.

    In order to ensure the consistency of PowerShell cmdlet support
    among OVAL interpreters as well as ensure that the state of a system
    is not changed, every OVAL interpreter must implement the following
    requirements.  An OVAL interpreter must only support the processing
    of the verbs specified in the EntityObjectCmdletVerbType.  If a
    cmdlet verb that is not defined in this enumeration is discovered,
    an error should be reported and the cmdlet must not be executed on
    the system.  While XML Schema validation will enforce this
    requirement, it is strongly recommended that OVAL interpreters
    implement a whitelist of allowed cmdlets.  This can be done using
    constrained runspaces which can limit the PowerShell execution
    environment.  For more information, please see Microsoft's
    documentation on Windows PowerShell Host Application Concepts.
    Furthermore, it is strongly recommended that OVAL interpreters also
    implement PowerShell support with the NoLanguage mode enabled.  The
    NoLanguage mode ensures that scripts that need to be evaluated are
    not allowed in the runspace. For more information about the
    NoLanguage mode, please see Microsoft's documentation on the
    PSLanguageMode enumeration.

    :ivar set:
    :ivar module_name: The name of the module that contains the cmdlet.
    :ivar module_id: The globally unique identifier for the module.
    :ivar module_version: The version of the module that contains the
        cmdlet in the form of MAJOR.MINOR.
    :ivar verb: The cmdlet verb.
    :ivar noun: The cmdlet noun.
    :ivar parameters: A list of properties (name and value pairs) as
        input to invoke the cmdlet. Each property name must be unique.
        When xsi:nill is set to true, parameters are not provided to the
        cmdlet.
    :ivar select: A list of fields (name and value pairs) used as input
        to the Select-Object cmdlet to select specific output
        properties. Each property name must be unique.  Please note that
        the use of the '*' character, to select all properties, is not
        permitted. This is because the value record entity, in the state
        and item, require unique field name values to ensure that any
        query results can be evaluated consistently. This is equivalent
        to piping the output of a cmdlet to the Select-Object cmdlet.
        When xsi:nill is set to true, the Select-Object is not used.
    :ivar filter:
    """

    class Meta:
        name = "cmdlet_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
            "nillable": True,
        },
    )
    module_id: Optional[EntityObjectGuidtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    module_version: Optional[EntityObjectVersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    verb: Optional[EntityObjectCmdletVerbType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    noun: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[EntityObjectRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    select: Optional[EntityObjectRecordType] = field(
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
class CmdletState(StateType):
    """
    The cmdlet_state allows for assertions about the presence of PowerShell cmdlet
    related properties and values obtained from a cmdlet.

    :ivar module_name: The name of the module that contains the cmdlet.
    :ivar module_id: The globally unique identifier for the module.
    :ivar module_version: The version of the module that contains the
        cmdlet in the form of MAJOR.MINOR.
    :ivar verb: The cmdlet verb.
    :ivar noun: The cmdlet noun.
    :ivar parameters: A list of properties (name and value pairs) as
        input to invoke the cmdlet. Each property name must be unique.
    :ivar select: A list of fields (name and value pairs) used as input
        to the Select-Object cmdlet to select specific output
        properties. Each property name must be unique.
    :ivar value: The expected value represented as a set of fields (name
        and value pairs). Each field must be have a unique name.
    """

    class Meta:
        name = "cmdlet_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    module_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    module_id: Optional[EntityStateGuidtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    module_version: Optional[EntityStateVersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    verb: Optional[EntityStateCmdletVerbType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    noun: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    select: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileObject(ObjectType):
    """The file_object element is used by a file test to define the specific
    file(s) to be evaluated.

    The file_object will collect directories and all Windows file types
    (FILE_TYPE_CHAR, FILE_TYPE_DISK, FILE_TYPE_PIPE, FILE_TYPE_REMOTE,
    and FILE_TYPE_UNKNOWN). Each object extends the standard ObjectType
    as defined in the oval-definitions-schema and one should refer to
    the ObjectType description for more information. The common set
    element allows complex objects to be created using filters and set
    logic. Again, please refer to the description of the set element in
    the oval-definitions-schema. A file object defines the path and
    filename or complete filepath of the file(s). In addition, a number
    of behaviors may be provided that help guide the collection of
    objects. Please refer to the FileBehaviors complex type for more
    information about specific behaviors. The set of files to be
    evaluated may be identified with either a complete filepath or a
    path and filename. Only one of these options may be selected. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file.

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
        all the files in the directory). In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar filter:
    """

    class Meta:
        name = "file_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class FileState(StateType):
    """The file_state element defines the different metadata associate with a
    Windows file.

    This includes the path, filename, owner, size, last modified time,
    version, etc. Please refer to the individual elements in the schema
    for more details about what each represents.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar owner: The owner element is a string that contains the name of
        the owner. The name should be specified in the DOMAIN\\username
        format.
    :ivar size: The size element is the size of the file in bytes.
    :ivar a_time: Time of last access of file. Valid on NTFS but not on
        FAT formatted disk drives. The string should represent the
        FILETIME structure which is a 64-bit value representing the
        number of 100-nanosecond intervals since January 1, 1601 (UTC).
    :ivar c_time: Time of creation of file. Valid on NTFS but not on FAT
        formatted disk drives. The string should represent the FILETIME
        structure which is a 64-bit value representing the number of
        100-nanosecond intervals since January 1, 1601 (UTC).
    :ivar m_time: Time of last modification of file. The string should
        represent the FILETIME structure which is a 64-bit value
        representing the number of 100-nanosecond intervals since
        January 1, 1601 (UTC).
    :ivar ms_checksum: The checksum of the file as supplied by
        Microsoft's MapFileAndCheckSum function.
    :ivar version: The version element is the delimited version string
        of the file.
    :ivar type_value: The type element marks whether the file is a
        directory, named pipe, standard file, etc. These types are the
        return values for GetFileType, with the exception of
        FILE_ATTRIBUTE_DIRECTORY which is obtained by looking at
        GetFileAttributesEx. NOTE: Should this entity be split into two
        in future versions of the language as there are other values
        associated with GetFileAttributesEx that are not represented
        here?
    :ivar development_class: The development_class element allows the
        distinction to be made between the GDR development environment
        and the QFE development environment. This field holds the text
        found in front of the mmmmmm-nnnn version, for example
        srv03_gdr.
    :ivar company: This entity defines a company name to be found within
        the version-information structure.
    :ivar internal_name: This entity defines an internal name to be
        found within the version-information structure.
    :ivar language: This entity defines a language to be found within
        the version-information structure.
    :ivar original_filename: This entity defines an original filename to
        be found within the version-information structure.
    :ivar product_name: This entity defines a product name to be found
        within the version-information structure.
    :ivar product_version: This entity defines a product version to be
        found within the version-information structure.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "file_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
    owner: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    m_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ms_checksum: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityStateVersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateFileTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    development_class: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    company: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    internal_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    language: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    original_filename: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    product_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    product_version: Optional[EntityStateVersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Fileauditedpermissions53State(StateType):
    """The fileauditedpermissions53_state element defines the different audit
    permissions that can be associated with a given
    fileauditedpermissions53_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        test for.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar file_read_data: Grants the right to read data from the file.
    :ivar file_write_data: Grants the right to write data to the file.
    :ivar file_append_data: Grants the right to append data to the file.
    :ivar file_read_ea: Grants the right to read extended attributes.
    :ivar file_write_ea: Grants the right to write extended attributes.
    :ivar file_execute: Grants the right to execute a file.
    :ivar file_delete_child: Right to delete a directory and all the
        files it contains (its children), even if the files are read-
        only.
    :ivar file_read_attributes: Grants the right to read file
        attributes.
    :ivar file_write_attributes: Grants the right to change file
        attributes.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "fileauditedpermissions53_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_data: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_data: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_append_data: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_ea: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_ea: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_delete_child: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_attributes: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_attributes: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileauditedpermissionsState(StateType):
    """The fileauditedpermissions_state element defines the different audit
    permissions that can be associated with a given fileauditedpermissions_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        test for.
    :ivar trustee_name: The trustee_name is the unique name associated
        with a particular security identifier (SID). In Windows, trustee
        names are case-insensitive. As a result, it is recommended that
        the case-insensitive operations are used for this entity. In a
        domain environment, trustee names should be identified in the
        form: "domain\\trustee name". For local trustee names use:
        "computer name\\trustee name". For built-in accounts on the
        system, use the trustee name without a domain.
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar file_read_data: Grants the right to read data from the file.
    :ivar file_write_data: Grants the right to write data to the file.
    :ivar file_append_data: Grants the right to append data to the file.
    :ivar file_read_ea: Grants the right to read extended attributes.
    :ivar file_write_ea: Grants the right to write extended attributes.
    :ivar file_execute: Grants the right to execute a file.
    :ivar file_delete_child: Right to delete a directory and all the
        files it contains (its children), even if the files are read-
        only.
    :ivar file_read_attributes: Grants the right to read file
        attributes.
    :ivar file_write_attributes: Grants the right to change file
        attributes.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "fileauditedpermissions_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
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
    trustee_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_data: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_data: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_append_data: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_ea: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_ea: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_delete_child: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_attributes: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_attributes: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Fileeffectiverights53State(StateType):
    """The fileeffectiverights53_state element defines the different rights that
    can be associated with a given fileeffectiverights53_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar file_read_data: Grants the right to read data from the file,
        or if a directory, grants the right to list the contents of the
        directory.
    :ivar file_write_data: Grants the right to write data to the file,
        or if a directory, grants the right to add a file to the
        directory.
    :ivar file_append_data: Grants the right to append data to the file,
        or if a directory, grants the right to add a sub-directory to
        the directory.
    :ivar file_read_ea: Grants the right to read extended attributes.
    :ivar file_write_ea: Grants the right to write extended attributes.
    :ivar file_execute: Grants the right to execute a file, or if a
        directory, the right to traverse the directory.
    :ivar file_delete_child: Right to delete a directory and all the
        files it contains (its children), even if the files are read-
        only.
    :ivar file_read_attributes: Grants the right to read file, or
        directory, attributes.
    :ivar file_write_attributes: Grants the right to change file, or
        directory, attributes.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "fileeffectiverights53_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_data: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_data: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_append_data: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_ea: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_ea: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_delete_child: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_attributes: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_attributes: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FileeffectiverightsState(StateType):
    """The fileeffectiverights_state element defines the different rights that can
    be associated with a given fileeffectiverights_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar trustee_name: The unique name associated with a particular
        security identifier (SID). In Windows, trustee names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, trustee names should be identified in the form:
        "domain\\trustee name". For local trustee names use: "computer
        name\\trustee name". For built-in accounts on the system, use
        the trustee name without a domain.
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar file_read_data: Grants the right to read data from the file,
        or if a directory, grants the right to list the contents of the
        directory.
    :ivar file_write_data: Grants the right to write data to the file,
        or if a directory, grants the right to add a file to the
        directory.
    :ivar file_append_data: Grants the right to append data to the file,
        or if a directory, grants the right to add a sub-directory to
        the directory.
    :ivar file_read_ea: Grants the right to read extended attributes.
    :ivar file_write_ea: Grants the right to write extended attributes.
    :ivar file_execute: Grants the right to execute a file, or if a
        directory, the right to traverse the directory.
    :ivar file_delete_child: Right to delete a directory and all the
        files it contains (its children), even if the files are read-
        only.
    :ivar file_read_attributes: Grants the right to read file, or
        directory, attributes.
    :ivar file_write_attributes: Grants the right to change file, or
        directory, attributes.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "fileeffectiverights_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
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
    trustee_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_data: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_data: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_append_data: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_ea: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_ea: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_delete_child: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_attributes: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_write_attributes: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class InterfaceState(StateType):
    """The interface_state element enumerates the different properties associate
    with a Windows interface.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar name: The name element specifies the name of an interface.
    :ivar index: The index element specifies index that identifies the
        interface.
    :ivar type_value: The type element specifies the type of interface
        which is limited to certain set of values.
    :ivar hardware_addr: The hardware_addr entity is the hardware or MAC
        address of the physical network card. MAC addresses should be
        formatted according to the IEEE 802-2001 standard which states
        that a MAC address is a sequence of six octet values, separated
        by hyphens, where each octet is represented by two hexadecimal
        digits.  Uppercase letters should also be used to represent the
        hexadecimal digits A through F.
    :ivar inet_addr: The inet_addr element specifies the IP address.
        Note that the IP address can be IPv4 or IPv6. If the IP address
        is an IPv6 address, this entity will be expressed as an IPv6
        address prefix using CIDR notation and the netmask entity will
        not be collected.
    :ivar broadcast_addr: The broadcast_addr element specifies the
        broadcast address. A broadcast address is typically the IP
        address with the host portion set to either all zeros or all
        ones. Note that the IP address can be IPv4 or IPv6.
    :ivar netmask: The netmask element specifies the subnet mask for the
        IP address. Note that if the inet_addr entity contains an IPv6
        address prefix, this entity will not be collected.
    :ivar addr_type: The addr_type element specifies the address type or
        state of a specific interface. Each interface can be associated
        with more than one value meaning the addr_type element can occur
        multiple times in a system characteristic item. Note that the
        entity_check attribute associated with EntityStateAddrTypeType
        guides the evaluation of unbounded entities like addr_type.
    """

    class Meta:
        name = "interface_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    index: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateInterfaceTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "",
        },
    )
    hardware_addr: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    inet_addr: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    broadcast_addr: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    netmask: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    addr_type: Optional[EntityStateAddrTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LicenseState(StateType):
    """The license_state element defines the different information that can be
    found in the Windows license registry value.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar name: The name entity corresponds to the license_object name
        entity.
    :ivar type_value: The optional type entity provides the type of data
        that is expected: REG_SZ (0x01) for a string; REG_BINARY (0x03)
        for binary data; REG_DWORD (0x04) for a dword.
    :ivar value: The value entity allows a test to be written against
        the value held within the specified license entry(-ies). If the
        value being tested is of type REG_BINARY, then the datatype
        attribute should be set to 'binary' and the data represented by
        the value entity should follow the xsd:hexBinary form. (each
        binary octet is encoded as two hex digits) If the value being
        tested is of type REG_DWORD, then the datatype attribute should
        be set to 'int' and the value entity should represent the data
        as an integer. If the specified registry key is of type REG_SZ,
        then the datatype should be 'string' and the value entity should
        be a copy of the string. Note that if the intent is to test a
        version number held in the license entry (as a reg_sz) then
        instead of setting the datatype to 'string', the datatype can be
        set to 'version'. This allows tools performing the evaluation to
        know how to perform less than and greater than operations
        correctly.
    """

    class Meta:
        name = "license_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateRegistryTypeType] = field(
        default=None,
        metadata={
            "name": "type",
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
class NtuserObject(ObjectType):
    """The ntuser_object element is used to specify which metadata should be
    collected from a Windows ntuser.dat file.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar key: The key element describes a registry key to be collected.
        Note that the hive portion of the string should not be included,
        as this data is not neccessary for the ntuser test and would
        normally reside in the HKCU hive.
    :ivar name: The name element describes the name assigned to a value
        associated with a specific registry key. If an empty string is
        specified for the name element, the registry key's default value
        should be collected. If the xsi:nil attribute is set to true,
        then the object being specified is the higher level key. In this
        case, the name element should not be collected or used in
        analysis. Setting xsi:nil equal to true on an element is
        different than using a .* pattern match. A .* pattern match says
        to collect every name under a given hive/key. The most likely
        use for xsi:nil within a registry object is when checking for
        the existence of a particular key, without regards to the
        different names associated with it.
    :ivar filter:
    """

    class Meta:
        name = "ntuser_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[NtuserBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityObjectStringType] = field(
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
class NtuserState(StateType):
    """The ntuser_state element defines the different metadata associated with a
    ntuser.dat file.

    This includes the key, name, type, and value. Please refer to the
    individual elements in the schema for more details about what each
    represents.

    :ivar key: This element describes a registry key normally found in
        the HKCU hive to be tested.
    :ivar name: This element describes the name of a value of a registry
        key.
    :ivar sid: This element holds a string that represents the SID of a
        particular user.
    :ivar username: The username entity holds a string that represents
        the name of a particular user. In Windows, user names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, users should be identified in the form:
        "domain\\user name". For local users use: "computer name\\user
        name".
    :ivar account_type: The account_type element describes if the user
        account is a local account or domain account.
    :ivar logged_on: The logged_on element describes if the user account
        is currently logged on to the computer.
    :ivar enabled: The enabled element describes if the user account is
        enabled or disabled.
    :ivar date_modified: Time of last modification of file. The integer
        should represent the FILETIME structure which is a 64-bit value
        representing the number of 100-nanosecond intervals since
        January 1, 1601 (UTC).
    :ivar days_since_modified: The number of days since the ntuser.dat
        file was last modified.  The value should be rounded up to the
        next whole integer.
    :ivar filepath: This element describes the filepath of the
        ntuser.dat file.
    :ivar last_write_time: The last time that the key or any of its
        value entries was modified. The value of this entity represents
        the FILETIME structure which is a 64-bit value representing the
        number of 100-nanosecond intervals since January 1, 1601 (UTC).
        Last write time can be queried on a key or name. When collecting
        only information about a registry key the last write time will
        be the time the key or any of its entiries was written to. When
        collecting only information about a registry name the last write
        time will be the time the name was written to. See the
        RegQueryInfoKey function lpftLastWriteTime.
    :ivar type_value: The type entity allows a test to be written
        against the registy type associated with the specified registry
        key(s). Please refer to the documentation on the
        EntityStateRegistryTypeType for more information about the
        different valid individual types.
    :ivar value: The value entity allows a test to be written against
        the value held within the specified registry key(s). If the
        value being tested is of type REG_BINARY, then the datatype
        attribute should be set to 'binary' and the data represented by
        the value entity should follow the xsd:hexBinary form. (each
        binary octet is encoded as two hex digits) If the value being
        tested is of type REG_DWORD or REG_QWORD, then the datatype
        attribute should be set to 'int' and the value entity should
        represent the data as an integer. If the value being tested is
        of type REG_EXPAND_SZ, then the datatype attribute should be set
        to 'string' and the pre-expanded string should be represented by
        the value entity. If the value being tested is of type
        REG_MULTI_SZ, then only a single string (one of the multiple
        strings) should be tested using the value entity with the
        datatype attribute set to 'string'. In order to test multiple
        values, multiple OVAL registry tests should be used. If the
        specified registry key is of type REG_SZ, then the datatype
        should be 'string' and the value entity should be a copy of the
        string. Note that if the intent is to test a version number held
        in the registry (as a reg_sz) then instead of setting the
        datatype to 'string', the datatype can be set to 'version'. This
        allows tools performing the evaluation to know how to perform
        less than and greater than operations correctly.
    """

    class Meta:
        name = "ntuser_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    username: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    account_type: Optional[EntityStateNtuserAccountTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    logged_on: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    enabled: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    date_modified: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    days_since_modified: Optional[EntityStateIntType] = field(
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
    last_write_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateRegistryTypeType] = field(
        default=None,
        metadata={
            "name": "type",
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
class PeheaderObject(ObjectType):
    """The peheader_object is used by a peheader_test to define the specific
    file(s) whose headers should be evaluated.

    The peheader_object will collect header information from PE files.
    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A peheader_object defines the path and filename
    or complete filepath of the file(s). In addition, a number of
    behaviors may be provided that help guide the collection of objects.
    Please refer to the PEHeaderBehaviors complex type for more
    information about specific behaviors. The set of files whose headers
    should be evaluated may be identified with either a complete
    filepath or a path and filename. Only one of these options may be
    selected. It is important to note that the 'max_depth' and
    'recurse_direction' attributes of the 'behaviors' element do not
    apply to the 'filepath' element, only to the 'path' and 'filename'
    elements.  This is because the 'filepath' element represents an
    absolute path to a particular file and it is not possible to recurse
    over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a PE file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a PE file on the machine.
    :ivar filename: The filename element specifies the name of a PE file
        to evaluate.
    :ivar filter:
    """

    class Meta:
        name = "peheader_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
class PeheaderState(StateType):
    """The peheader_state defines the different metadata associated with the header
    of a PE file.

    Please refer to the individual elements in the schema for more
    details about what each represents. For more information, please see
    the documentation for the IMAGE_FILE_HEADER and
    IMAGE_OPTIONAL_HEADER structures.

    :ivar filepath: The filepath element specifies the absolute path for
        a PE file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a PE file on the machine.
    :ivar filename: The filename element specifies the name of a PE file
        to evaluate.
    :ivar header_signature: The header_signature entity is the signature
        of the header.
    :ivar target_machine_type: The target_machine_type entity is an
        unsigned 16-bit integer (WORD) that specifies the target
        architecture that the file is intended for.
    :ivar number_of_sections: The number_of_sections entity is an
        unsigned 16-bit integer (WORD) that specifies the number of
        sections in the file.
    :ivar time_date_stamp: The time_date_stamp entity is an unsigned
        32-bit integer (DWORD) that specifies the time that the linker
        produced the file. The value is represented as the number of
        seconds since January 1, 1970, 00:00:00.
    :ivar pointer_to_symbol_table: The pointer_to_symbol_table entity is
        an unsigned 32-bit integer (DWORD) that specifies the file
        offset of the COFF symbol table.
    :ivar number_of_symbols: The number_of_symbols entity is an unsigned
        32-bit integer (DWORD) that specifies the number of symbols in
        the COFF symbol table.
    :ivar size_of_optional_header: The size_of_optional_header entity is
        an unsigned 32-bit integer (DWORD) that specifies the size of an
        optional header in bytes.
    :ivar image_file_relocs_stripped: The image_file_relocs_stripped
        entity is a boolean value that specifies if the relocation
        information is stripped from the file.
    :ivar image_file_executable_image: The image_file_executable_image
        entity is a boolean value that specifies if the file is
        executable.
    :ivar image_file_line_nums_stripped: The
        image_file_line_nums_stripped entity is a boolean value that
        specifies if the line numbers are stripped from the file.
    :ivar image_file_local_syms_stripped: The
        image_file_local_syms_stripped entity is a boolean value that
        specifies if the local symbols are stripped from the file.
    :ivar image_file_aggresive_ws_trim: The
        image_file_aggressive_ws_trim entity is a boolean value that
        specifies that the working set should be aggressively trimmed.
    :ivar image_file_large_address_aware: The
        image_file_large_address_aware entity is a boolean value that
        specifies that the application can handle addresses larger than
        2GB.
    :ivar image_file_16bit_machine: The image_file_16bit_machine entity
        is a boolean value that specifies that the computer supports
        16-bit words.
    :ivar image_file_bytes_reversed_lo: The image_file_bytes_reversed_lo
        entity is a boolean value that specifies that the bytes of the
        word are reversed.
    :ivar image_file_32bit_machine: The image_file_32bit_machine entity
        is a boolean value that specifies that the computer supports
        32-bit words.
    :ivar image_file_debug_stripped: The image_file_debug_stripped
        entity is a boolean value that specifies that the debugging
        information is stored separately in a .dbg file.
    :ivar image_file_removable_run_from_swap: The
        image_file_removable_run_from_swap entity is a boolean value
        that specifies that the image is on removable media, copy and
        run from the swap file.
    :ivar image_file_system: The image_file_system entity is a boolean
        value that specifies that the image is a system file.
    :ivar image_file_dll: The image_file_dll entity is a boolean value
        that specifies that the image is a DLL.
    :ivar image_file_up_system_only: The image_file_up_system_only
        entity is a boolean value that specifies that the file should
        only be run on a uniprocessor computer.
    :ivar image_file_bytes_reveresed_hi: The
        image_file_bytes_reversed_hi entity is a boolean value that
        specifies that the bytes of the word are reversed.
    :ivar magic_number: The magic_number entity is an unsigned 16-bit
        integer (WORD) that specifies the state of the image file.
    :ivar major_linker_version: The major_linker_version entity is a
        BYTE that specifies the major version of the linker that
        produced the file.
    :ivar minor_linker_version: The minor_linker_version entity is a
        BYTE that specifies the minor version of the linker that
        produced the file.
    :ivar size_of_code: The size_of_code entity is an unsigned 32-bit
        integer (DWORD) that specifies the total size of all of the code
        sections.
    :ivar size_of_initialized_data: The size_of_initialized_data entity
        is an unsigned 32-bit integer (DWORD) that specifies the total
        size of all of the sections that are composed of initialized
        data.
    :ivar size_of_uninitialized_data: The size_of_uninitialized_data
        entity is an unsigned 32-bit integer (DWORD) that specifies the
        total size of all of the sections that are composed of
        uninitialized data.
    :ivar address_of_entry_point: The address_of_entry_point entity is
        an unsigned 32-bit integer (DWORD) that specifies the address
        where the loader will begin execution.
    :ivar base_of_code: The base_of_code entity is an unsigned 32-bit
        integer (DWORD) that specifies the relative virtual address
        where the file's code section begins.
    :ivar base_of_data: The base_of_data entity is an unsigned 32-bit
        integer (DWORD) that specifies the relative virtual address
        where the file's data section begins.
    :ivar image_base_address: The image_base_address entity is an
        unsigned 32-bit integer (DWORD) that specifies the preferred
        address fo the first byte of the image when it is loaded into
        memory.
    :ivar section_alignment: The section_alignment entity is an unsigned
        32-bit integer (DWORD) that specifies the alignment of the
        sections loaded into memory.
    :ivar file_alignment: The file_alignment entity is an unsigned
        32-bit integer (DWORD) that specifies the alignment of the raw
        data of sections in the image file.
    :ivar major_operating_system_version: The
        major_operating_system_version entity is an unsigned 16-bit
        integer (WORD) that specifies the major version of the operating
        system required to use this executable.
    :ivar minor_operating_system_version: The
        minor_operating_system_version entity is an unsigned 16-bit
        integer (WORD) that specifies the minor version of the operating
        system required to use this executable.
    :ivar major_image_version: The major_image_version entity is an
        unsigned 16-bit integer (WORD) that specifies the major version
        number of the image.
    :ivar minor_image_version: The minor_image_version entity is an
        unsigned 32-bit integer (DWORD) that specifies the minor version
        number of the image.
    :ivar major_subsystem_version: The major_subsystem_version entity is
        an unsigned 16-bit integer (WORD) that specifies the major
        version of the subsystem required to run the executable.
    :ivar minor_susbsystem_version: The minor_subsystem_version entity
        is an unsigned 16-bit integer (WORD) that specifies the minor
        version of the subsystem required to run the executable.
    :ivar size_of_image: The size_of_image entity is an unsigned 32-bit
        integer (DWORD) that specifies the total size of the image
        including all of the headers.
    :ivar size_of_headers: The size_of_headers entity is an unsigned
        32-bit integer (DWORD) that specifies the total combined size of
        the MS-DOS stub, PE header, and the section headers.
    :ivar checksum: The checksum entity is an unsigned 32-bit integer
        (DWORD) that specifies the checksum of the image file.
    :ivar subsystem: The subsystem entity is an unsigned 32-bit integer
        (DWORD) that specifies the type of subsystem that the executable
        uses for its user interface.
    :ivar dll_characteristics: The dll_characteristics entity is an
        unsigned 32-bit integer (DWORD) that specifies the set of flags
        indicating the circumstances under which a DLL's initialization
        function will be called..
    :ivar size_of_stack_reserve: The time_date_stamp entity is an
        unsigned 32-bit integer (DWORD) that specifies the number of
        bytes to reserve for the stack.
    :ivar size_of_stack_commit: The time_date_stamp entity is an
        unsigned 32-bit integer (DWORD) that specifies the number of
        bytes to commit for the stack.
    :ivar size_of_heap_reserve: The time_date_stamp entity is an
        unsigned 32-bit integer (DWORD) that specifies the number of
        bytes to reserve for the local heap.
    :ivar size_of_heap_commit: The time_date_stamp entity is an unsigned
        32-bit integer (DWORD) that specifies the number of bytes to
        commit for the local heap.
    :ivar loader_flags: The loader_flags entity is an unsigned 32-bit
        integer (DWORD) that specifies the loader flags of the header.
    :ivar number_of_rva_and_sizes: The number_of_rva_and_sizes entity is
        an unsigned 32-bit integer (DWORD) that specifies the number of
        directory entries in the remainder of the optional header.
    :ivar real_number_of_directory_entries: The
        real_number_of_directory_entries entity is the real number of
        data directory entries in the remainder of the optional header
        calculated by enumerating the directory entries.
    """

    class Meta:
        name = "peheader_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

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
    header_signature: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    target_machine_type: Optional[EntityStatePeTargetMachineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    number_of_sections: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_date_stamp: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pointer_to_symbol_table: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    number_of_symbols: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_optional_header: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_relocs_stripped: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_executable_image: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_line_nums_stripped: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_local_syms_stripped: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_aggresive_ws_trim: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_large_address_aware: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_16bit_machine: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_bytes_reversed_lo: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_32bit_machine: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_debug_stripped: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_removable_run_from_swap: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_system: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_dll: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_up_system_only: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_file_bytes_reveresed_hi: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    magic_number: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    major_linker_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    minor_linker_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_code: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_initialized_data: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_uninitialized_data: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    address_of_entry_point: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    base_of_code: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    base_of_data: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    image_base_address: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    section_alignment: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_alignment: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    major_operating_system_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    minor_operating_system_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    major_image_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    minor_image_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    major_subsystem_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    minor_susbsystem_version: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_image: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_headers: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    checksum: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subsystem: Optional[EntityStatePeSubsystemType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dll_characteristics: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_stack_reserve: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_stack_commit: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_heap_reserve: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_of_heap_commit: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    loader_flags: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    number_of_rva_and_sizes: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    real_number_of_directory_entries: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PortObject(ObjectType):
    """The port_object element is used by a port test to define the specific
    port(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. A port object defines the local address, port
    number, and protocol of the port(s).

    :ivar set:
    :ivar local_address: This element specifies the local IP address the
        listening port is bound to. Note that the IP address can be IPv4
        or IPv6.
    :ivar local_port: This element specifies the number assigned to the
        local listening port.
    :ivar protocol: This element specifies the type of listening port.
        It is restricted to either TCP or UDP.
    :ivar filter:
    """

    class Meta:
        name = "port_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
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
    protocol: Optional[EntityObjectProtocolType] = field(
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
class PortState(StateType):
    """The port_state element defines the different metadata associate with a
    Windows port.

    This includes the local address, port number, protocol, and pid.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar local_address: This element specifies the local IP address the
        listening port is bound to. Note that the IP address can be IPv4
        or IPv6.
    :ivar local_port: This element specifies the number assigned to the
        local listening port.
    :ivar protocol: This element specifies the type of listening port.
        It is restricted to either TCP or UDP.
    :ivar pid: The id given to the process that is associated with the
        specified listening port.
    :ivar foreign_address: This is the IP address with which the program
        is communicating, or with which it will communicate, in the case
        of a listening server. Note that the IP address can be IPv4 or
        IPv6.
    :ivar foreign_port: This is the TCP or UDP port to which the program
        communicates.
    """

    class Meta:
        name = "port_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
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
    protocol: Optional[EntityStateProtocolType] = field(
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
    foreign_address: Optional[EntityStateIpaddressStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foreign_port: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RegistryObject(ObjectType):
    """
    :ivar set:
    :ivar behaviors:
    :ivar hive: The hive that the registry key belongs to. This is
        restricted to a specific set of values: HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and
        HKEY_USERS.
    :ivar key: The key element describes a registry key to be collected.
        Note that the hive portion of the string should not be included,
        as this data should be found under the hive element. If the
        xsi:nil attribute is set to true, then the object being
        specified is the higher level hive. In this case, the key
        element should not be collected or used in analysis. Setting
        xsi:nil equal to true is different than using a .* pattern
        match. A .* pattern match says to collect every key under a
        given hive.
    :ivar name: The name element describes the name assigned to a value
        associated with a specific registry key. If an empty string is
        specified for the name element, the registry key's default value
        should be collected. If the xsi:nil attribute is set to true,
        then the object being specified is the higher level hive/key. In
        this case, the name element should not be collected or used in
        analysis. Setting xsi:nil equal to true on an element is
        different than using a .* pattern match. A .* pattern match says
        to collect every name under a given hive/key. The most likely
        use for xsi:nil within a registry object is when checking for
        the existence of a particular key, without regards to the
        different names associated with it.
    :ivar filter:
    """

    class Meta:
        name = "registry_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RegistryBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hive: Optional[EntityObjectRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    name: Optional[EntityObjectStringType] = field(
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
class RegistryState(StateType):
    """The registry_state element defines the different metadata associate with a
    Windows registry key.

    This includes the hive, key, name, type, and value. Please refer to
    the individual elements in the schema for more details about what
    each represents.

    :ivar hive: The hive that the registry key belongs to. This is
        restricted to a specific set of values: HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and
        HKEY_USERS.
    :ivar key: This element describes a registry key to be tested. Note
        that the hive portion of the string should not be inclueded, as
        this data should be found under the hive element.
    :ivar name: This element describes the name of a value of a registry
        key. If the xsi:nil attribute is set to true, then the name
        element should not be used in analysis.
    :ivar last_write_time: The last time that the key or any of its
        value entries were modified. The value of this entity represents
        the FILETIME structure which is a 64-bit value representing the
        number of 100-nanosecond intervals since January 1, 1601 (UTC).
        Last write time can be queried on any key, with hives being
        classified as a type of key. When collecting only information
        about a registry hive or key the last write time will be the
        time the key or any of its entries were modified. When
        collecting only information about a registry name the last write
        time will be the time the containing key was modified. Thus when
        collecting information about a registry name, the last write
        time does not correlate directly to the specified name. See the
        RegQueryInfoKey function lpftLastWriteTime.
    :ivar type_value: The type entity allows a test to be written
        against the registy type associated with the specified registry
        key(s). Please refer to the documentation on the
        EntityStateRegistryTypeType for more information about the
        different valid individual types.
    :ivar value: The value entity allows a test to be written against
        the value held within the specified registry key(s). If the
        value being tested is of type REG_BINARY, then the datatype
        attribute should be set to 'binary' and the data represented by
        the value entity should follow the xsd:hexBinary form. (each
        binary octet is encoded as two hex digits) If the value being
        tested is of type REG_DWORD, REG_QWORD, REG_DWORD_LITTLE_ENDIAN,
        REG_DWORD_BIG_ENDIAN, and REG_QWORD_LITTLE_ENDIAN then the
        datatype attribute should be set to 'int' and the value entity
        should represent the data as an unsigned integer. DWORD and
        QWORD values represnt unsigned 32-bit and 64-bit integers,
        respectively. If the value being tested is of type
        REG_EXPAND_SZ, then the datatype attribute should be set to
        'string' and the pre-expanded string should be represented by
        the value entity.  If the value being tested is of type
        REG_MULTI_SZ, then only a single string (one of the multiple
        strings) should be tested using the value entity with the
        datatype attribute set to 'string'. In order to test multiple
        values, multiple OVAL registry tests should be used.  If the
        specified registry key is of type REG_SZ, then the datatype
        should be 'string' and the value entity should be a copy of the
        string.  If the value being tested is of type REG_LINK, then the
        datatype attribute should be set to 'string' and the null-
        terminated Unicode string should be represented by the value
        entity. Note that if the intent is to test a version number held
        in the registry (as a reg_sz) then instead of setting the
        datatype to 'string', the datatype can be set to 'version'. This
        allows tools performing the evaluation to know how to perform
        less than and greater than operations correctly.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "registry_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    hive: Optional[EntityStateRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    last_write_time: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[EntityStateRegistryTypeType] = field(
        default=None,
        metadata={
            "name": "type",
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
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Regkeyauditedpermissions53State(StateType):
    """The regkeyauditedpermissions53_state element defines the different audit
    permissions that can be associated with a given
    regkeyauditedpermissions53_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar hive: This element specifies the hive of a registry key on the
        machine from which to retrieve the SACL.
    :ivar key: This element specifies a registry key on the machine from
        which to retrieve the SACL. Note that the hive portion of the
        string should not be inclueded, as this data should be found
        under the hive element.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar key_query_value:
    :ivar key_set_value:
    :ivar key_create_sub_key:
    :ivar key_enumerate_sub_keys:
    :ivar key_notify:
    :ivar key_create_link:
    :ivar key_wow64_64key:
    :ivar key_wow64_32key:
    :ivar key_wow64_res:
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "regkeyauditedpermissions53_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    hive: Optional[EntityStateRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_query_value: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_set_value: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_sub_key: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_enumerate_sub_keys: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_notify: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_link: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_64key: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_32key: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_res: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RegkeyauditedpermissionsState(StateType):
    """The regkeyauditedpermissions_state element defines the different audit
    permissions that can be associated with a given
    regkeyauditedpermissions_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar hive: This element specifies the hive of a registry key on the
        machine from which to retrieve the SACL.
    :ivar key: This element specifies a registry key on the machine from
        which to retrieve the SACL. Note that the hive portion of the
        string should not be inclueded, as this data should be found
        under the hive element.
    :ivar trustee_name: The unique name associated with a particular
        security identifier (SID). In Windows, trustee names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, trustee names should be identified in the form:
        "domain\\trustee name". For local trustee names use: "computer
        name\\trustee name". For built-in accounts on the system, use
        the trustee name without a domain.
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar key_query_value:
    :ivar key_set_value:
    :ivar key_create_sub_key:
    :ivar key_enumerate_sub_keys:
    :ivar key_notify:
    :ivar key_create_link:
    :ivar key_wow64_64key:
    :ivar key_wow64_32key:
    :ivar key_wow64_res:
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "regkeyauditedpermissions_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    hive: Optional[EntityStateRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_query_value: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_set_value: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_sub_key: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_enumerate_sub_keys: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_notify: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_link: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_64key: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_32key: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_res: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Regkeyeffectiverights53State(StateType):
    """The regkeyeffectiverights53_state element defines the different rights that
    can be associated with a given regkeyeffectiverights53_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar hive: This element specifies the hive of a registry key on the
        machine from which to retrieve the SACL.
    :ivar key: This element specifies a registry key on the machine from
        which to retrieve the SACL. Note that the hive portion of the
        string should not be inclueded, as this data should be found
        under the hive element.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar key_query_value:
    :ivar key_set_value:
    :ivar key_create_sub_key:
    :ivar key_enumerate_sub_keys:
    :ivar key_notify:
    :ivar key_create_link:
    :ivar key_wow64_64key:
    :ivar key_wow64_32key:
    :ivar key_wow64_res:
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "regkeyeffectiverights53_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    hive: Optional[EntityStateRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_query_value: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_set_value: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_sub_key: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_enumerate_sub_keys: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_notify: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_link: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_64key: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_32key: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_res: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RegkeyeffectiverightsState(StateType):
    """The regkeyeffectiverights_state element defines the different rights that
    can be associated with a given regkeyeffectiverights_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar hive: This element specifies the hive of a registry key on the
        machine from which to retrieve the SACL.
    :ivar key: This element specifies a registry key on the machine from
        which to retrieve the SACL. Note that the hive portion of the
        string should not be inclueded, as this data should be found
        under the hive element.
    :ivar trustee_name: The unique name associated with a particular
        security identifier (SID). In Windows, trustee names are case-
        insensitive. As a result, it is recommended that the case-
        insensitive operations are used for this entity. In a domain
        environment, trustee names should be identified in the form:
        "domain\\trustee name". For local trustee names use: "computer
        name\\trustee name". For built-in accounts on the system, use
        the trustee name without a domain.
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    :ivar key_query_value:
    :ivar key_set_value:
    :ivar key_create_sub_key:
    :ivar key_enumerate_sub_keys:
    :ivar key_notify:
    :ivar key_create_link:
    :ivar key_wow64_64key:
    :ivar key_wow64_32key:
    :ivar key_wow64_res:
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.
    """

    class Meta:
        name = "regkeyeffectiverights_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    hive: Optional[EntityStateRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_query_value: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_set_value: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_sub_key: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_enumerate_sub_keys: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_notify: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_create_link: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_64key: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_32key: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key_wow64_res: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ServiceState(StateType):
    """The service_state element defines the different metadata associated with a
    Windows service.

    This includes the service name, display name, description, type,
    start type, current state, controls accepted, start name, path, pid,
    service flag, and dependencies. Please refer to the individual
    elements in the schema for more details about what each represents.

    :ivar service_name: The service_name element specifies the name of
        the service as specified in the Service Control Manager (SCM)
        database.
    :ivar display_name: The display_name element specifies the name of
        the service as specified in tools such as Control
        Panel-&gt;Administrative Tools-&gt;Services.
    :ivar description: The description element specifies the description
        of the service.
    :ivar service_type: The service_type element specifies the type of
        the service.
    :ivar start_type: The start_type element specifies when the service
        should be started.
    :ivar current_state: The current_state element specifies the current
        state of the service.
    :ivar controls_accepted: The controls_accepted element specifies the
        control codes that a service will accept and process.
    :ivar start_name: The start_name element specifies the account under
        which the process should run.
    :ivar path: The path element specifies the path to the binary of the
        service.
    :ivar pid: The pid element specifies the process ID of the service.
    :ivar service_flag: The service_flag element specifies if the
        service is in a system process that must always run (1) or if
        the service is in a non-system process or is not running (0). If
        the service is not running, the pid will be 0. Otherwise, the
        pid will be non-zero.
    :ivar dependencies: The dependencies element specifies the
        dependencies of this service on other services.
    """

    class Meta:
        name = "service_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    service_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    display_name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    description: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_type: Optional[EntityStateServiceTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    start_type: Optional[EntityStateServiceStartTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_state: Optional[EntityStateServiceCurrentStateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    controls_accepted: Optional[EntityStateServiceControlsAcceptedType] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
    )
    start_name: Optional[EntityStateStringType] = field(
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
    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    service_flag: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependencies: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SharedresourceState(StateType):
    """The sharedresource_state element defines the different metadata associated
    with a Windows shared resource.

    This includes the share type, permissions, and max uses. This state
    mirrors the SHARE_INFO_2 structure. Please refer to the individual
    elements in the schema for more details about what each represents.

    :ivar netname: This element specifies the name associated with a
        particular shared resource.
    :ivar shared_type: The type of the shared resource.
    :ivar max_uses: The maximum number of concurrent connections that
        the shared resource can accommodate.
    :ivar current_uses: The number of current connections to the
        resource.
    :ivar local_path: The local path for the shared resource.
    :ivar access_read_permission: Permission to read data from a
        resource and, by default, to execute the resource.
    :ivar access_write_permission: Permission to write data to the
        resource.
    :ivar access_create_permission: Permission to create an instance of
        the resource (such as a file); data can be written to the
        resource as the resource is created.
    :ivar access_exec_permission: Permission to execute the resource.
    :ivar access_delete_permission: Permission to delete the resource.
    :ivar access_atrib_permission: Permission to modify the resource's
        attributes (such as the date and time when a file was last
        modified).
    :ivar access_perm_permission: Permission to modify the permissions
        (read, write, create, execute, and delete) assigned to a
        resource for a user or application.
    :ivar access_all_permission: Permission to read, write, create,
        execute, and delete resources, and to modify their attributes
        and permissions.
    """

    class Meta:
        name = "sharedresource_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    netname: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    shared_type: Optional[EntityStateSharedResourceTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    max_uses: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    current_uses: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    local_path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_read_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_write_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_create_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_exec_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_delete_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_atrib_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_perm_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_all_permission: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SharedresourceauditedpermissionsState(StateType):
    """The sharedresourceauditedpermissions_state element defines the different
    audited permissions that can be associated with a given
    sharedresourceauditedpermissions_object.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar netname: This element specifies the name associated with a
        particular shared resource.
    :ivar trustee_sid: The trustee_sid element is the unique SID that
        associated a user, group, system, or program (such as a Windows
        service).
    :ivar standard_delete: The right to delete the object.
    :ivar standard_read_control: The right to read the information in
        the object's Security Descriptor, not including the information
        in the SACL.
    :ivar standard_write_dac: The right to modify the DACL in the
        object's Security Descriptor.
    :ivar standard_write_owner: The right to change the owner in the
        object's Security Descriptor.
    :ivar standard_synchronize: The right to use the object for
        synchronization. This enables a thread to wait until the object
        is in the signaled state. Some object types do not support this
        access right.
    :ivar access_system_security: Indicates access to a system access
        control list (SACL).
    :ivar generic_read: Read access.
    :ivar generic_write: Write access.
    :ivar generic_execute: Execute access.
    :ivar generic_all: Read, write, and execute access.
    """

    class Meta:
        name = "sharedresourceauditedpermissions_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    netname: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_delete: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_read_control: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_dac: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_write_owner: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    standard_synchronize: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    access_system_security: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_read: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_write: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_execute: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic_all: Optional[EntityStateAuditType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SystemmetricObject(ObjectType):
    """The system metric object element is used by a system metric test to define
    the object to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar index: The index entity provides the system metric index value
        that is desired.
    :ivar filter:
    """

    class Meta:
        name = "systemmetric_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    index: Optional[EntityObjectSystemMetricIndexType] = field(
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
class SystemmetricState(StateType):
    """The system metric state element defines the different information that can
    be found in a Windows system metric value.

    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar index: The index entity corresponds to the systemmetric_object
        index entity.
    :ivar value: The optional value entity provides the value of the
        system metric that is expected.
    """

    class Meta:
        name = "systemmetric_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    index: Optional[EntityStateSystemMetricIndexType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UserrightObject(ObjectType):
    """
    The userright_object is used to collect the SIDs that have been granted a
    specific user right/privilege.

    :ivar set:
    :ivar userright: The userright entity holds a string that represents
        the name of a particular user right/privilege.
    :ivar filter:
    """

    class Meta:
        name = "userright_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    userright: Optional[EntityObjectUserRightType] = field(
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
class UserrightState(StateType):
    """
    :ivar userright: The userright entity holds a string that represents
        the name of a particular user right/privilege.
    :ivar trustee_sid: The trustee_sid element identifies the SID that
        has been granted the specified user right/privilege. The
        trustee_sid element can be included multiple times in a system
        characteristic item in order to record that a user
        right/privilege has been granted to a number of SIDs. Note that
        the entity_check attribute associated with EntityStateStringType
        guides the evaluation of entities like trustee_sid that refer to
        items that can occur an unbounded number of times.
    """

    class Meta:
        name = "userright_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    userright: Optional[EntityStateUserRightType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_sid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class VolumeState(StateType):
    """The volume_state element defines the different metadata associate with a
    storage volume in Windows.

    This includes the rootpath, the file system type, name, and serial
    number, as well as any associated flags. Please refer to the
    individual elements in the schema for more details about what each
    represents. The GetVolumeInformation function as defined by
    Microsoft is also a good place to look for information.

    :ivar rootpath: A string that contains the root directory of the
        volume to be described. A trailing backslash is required. For
        example, you would specify \\\\MyServer\\MyShare as
        "\\\\MyServer\\MyShare\\", or the C drive as "C:\\".
    :ivar file_system: The type of filesystem. For example FAT or NTFS.
    :ivar name: The name of the volume.
    :ivar drive_type: The drive type of the volume.
    :ivar volume_max_component_length: The volume_max_component_length
        element specifies the maximum length, in TCHARs, of a file name
        component that a specified file system supports. A file name
        component is the portion of a file name between backslashes. The
        value that is stored in the variable that
        *lpMaximumComponentLength points to is used to indicate that a
        specified file system supports long names. For example, for a
        FAT file system that supports long names, the function stores
        the value 255, rather than the previous 8.3 indicator. Long
        names can also be supported on systems that use the NTFS file
        system.
    :ivar serial_number: The volume serial number.
    :ivar file_case_sensitive_search: The file system supports case-
        sensitive file names.
    :ivar file_case_preserved_names: The file system preserves the case
        of file names when it places a name on disk.
    :ivar file_unicode_on_disk: The file system supports Unicode in file
        names as they appear on disk.
    :ivar file_persistent_acls: The file system preserves and enforces
        ACLs. For example, NTFS preserves and enforces ACLs, and FAT
        does not.
    :ivar file_file_compression: The file system supports file-based
        compression.
    :ivar file_volume_quotas: The file system supports disk quotas.
    :ivar file_supports_sparse_files: The file system supports sparse
        files.
    :ivar file_supports_reparse_points: The file system supports reparse
        points.
    :ivar file_supports_remote_storage: The file system supports remote
        storage.
    :ivar file_volume_is_compressed: The specified volume is a
        compressed volume; for example, a DoubleSpace volume.
    :ivar file_supports_object_ids: The file system supports object
        identifiers.
    :ivar file_supports_encryption: The file system supports the
        Encrypted File System (EFS).
    :ivar file_named_streams: The file system supports named streams.
    :ivar file_read_only_volume: The specified volume is read-only.
    :ivar file_sequential_write_once: The file system supports one time
        writes in sequential order.
    :ivar file_supports_transactions: The file system supports
        transaction processing.
    :ivar file_supports_hard_links: The file system supports direct
        links to other devices and partitions.
    :ivar file_supports_extended_attributes: The file system supports
        extended attributes.
    :ivar file_supports_open_by_file_id: The file system supports
        fileID.
    :ivar file_supports_usn_journal: The file system supports update
        sequence number journals.
    """

    class Meta:
        name = "volume_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    rootpath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_system: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    drive_type: Optional[EntityStateDriveTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    volume_max_component_length: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    serial_number: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_case_sensitive_search: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_case_preserved_names: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_unicode_on_disk: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_persistent_acls: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_file_compression: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_volume_quotas: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_sparse_files: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_reparse_points: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_remote_storage: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_volume_is_compressed: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_object_ids: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_encryption: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_named_streams: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_read_only_volume: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_sequential_write_once: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_transactions: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_hard_links: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_extended_attributes: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_open_by_file_id: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_supports_usn_journal: Optional[EntityStateBoolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Fileauditedpermissions53Object(ObjectType):
    """The fileauditedpermissions53_object element is used by a file audited
    permissions test to define the objects used to evalutate against the specified
    state.

    The fileauditedpermissions53_object will collect directories and all
    Windows file types (FILE_TYPE_CHAR, FILE_TYPE_DISK, FILE_TYPE_PIPE,
    FILE_TYPE_REMOTE, and FILE_TYPE_UNKNOWN). Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. A fileauditedpermissions53_object is defined
    as a combination of a Windows file and trustee SID. The file
    represents the file to be evaluated while the trustee SID represents
    the account (SID) to check audited permissions of. If multiple files
    or SIDs are matched by either reference, then each possible
    combination of file and SID is a matching file audited permissions
    object. In addition, a number of behaviors may be provided that help
    guide the collection of objects. Please refer to the
    FileAuditPermissions53Behaviors complex type for more information
    about specific behaviors. The set of files to be evaluated may be
    identified with either a complete filepath or a path and filename.
    Only one of these options may be selected. It is important to note
    that the 'max_depth' and 'recurse_direction' attributes of the
    'behaviors' element do not apply to the 'filepath' element, only to
    the 'path' and 'filename' elements.  This is because the 'filepath'
    element represents an absolute path to a particular file and it is
    not possible to recurse over a file.

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
        all the files in the directory). In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the file's Security Descriptor.  The scope is
        limited here to avoid unnecessarily resource intensive searches
        for trustees.  Note that the larger scope of all known trustees
        may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "fileauditedpermissions53_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileAuditPermissions53Behaviors] = field(
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
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class FileauditedpermissionsObject(ObjectType):
    """The fileauditedpermissions_object element is used by a file audited
    permissions test to define the objects used to evalutate against the specified
    state.

    The fileauditedpermissions_object will collect directories and all
    Windows file types (FILE_TYPE_CHAR, FILE_TYPE_DISK, FILE_TYPE_PIPE,
    FILE_TYPE_REMOTE, and FILE_TYPE_UNKNOWN). Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. A fileauditedpermissions_object is defined as
    a combination of a Windows file and trustee name. The file
    represents the file to be evaluated while the trustee name
    represents the account (SID) to check audited permissions of. If
    multiple files or SIDs are matched by either reference, then each
    possible combination of file and SID is a matching file audited
    permissions object. In addition, a number of behaviors may be
    provided that help guide the collection of objects. Please refer to
    the FileAuditPermissionsBehaviors complex type for more information
    about specific behaviors.

    :ivar set:
    :ivar behaviors:
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        evaluate. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level directory object (not
        all the files in the directory). In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar trustee_name: The trustee_name element is the unique name that
        associated a particular SID. A SID can be associated with a
        user, group, or program (such as a Windows service). In Windows,
        trustee names are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. In a domain environment, trustee names should be
        identified in the form: "domain\\trustee name". For local
        trustee names use: "computer name\\trustee name". For built-in
        accounts on the system, use the trustee name without a domain.
    """

    class Meta:
        name = "fileauditedpermissions_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileAuditPermissionsBehaviors] = field(
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
    trustee_name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Fileeffectiverights53Object(ObjectType):
    """The fileeffectiverights53_object element is used by a file effective rights
    test to define the objects used to evalutate against the specified state.

    The fileeffectiverights53_object will collect directories and all
    Windows file types (FILE_TYPE_CHAR, FILE_TYPE_DISK, FILE_TYPE_PIPE,
    FILE_TYPE_REMOTE, and FILE_TYPE_UNKNOWN). Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. A fileeffectiverights53_object is defined as
    a combination of a Windows file and trustee SID. The file represents
    the file to be evaluated while the trustee SID represents the
    account (SID) to check effective rights of. If multiple files or
    SIDs are matched by either reference, then each possible combination
    of file and SID is a matching file effective rights object. In
    addition, a number of behaviors may be provided that help guide the
    collection of objects. Please refer to the
    FileEffectiveRights53Behaviors complex type for more information
    about specific behaviors. The set of files to be evaluated may be
    identified with either a complete filepath or a path and filename.
    Only one of these options may be selected. It is important to note
    that the 'max_depth' and 'recurse_direction' attributes of the
    'behaviors' element do not apply to the 'filepath' element, only to
    the 'path' and 'filename' elements.  This is because the 'filepath'
    element represents an absolute path to a particular file and it is
    not possible to recurse over a file.

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
        all the files in the directory). In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path..
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the file's Security Descriptor.  The scope is
        limited here to avoid unnecessarily resource intensive searches
        for trustees.  Note that the larger scope of all known trustees
        may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "fileeffectiverights53_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileEffectiveRights53Behaviors] = field(
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
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class FileeffectiverightsObject(ObjectType):
    """The fileeffectiverights_object element is used by a file effective rights
    test to define the objects used to evalutate against the specified state.

    The fileeffectiverights_object will collect directories and all
    Windows file types (FILE_TYPE_CHAR, FILE_TYPE_DISK, FILE_TYPE_PIPE,
    FILE_TYPE_REMOTE, and FILE_TYPE_UNKNOWN). Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. A fileeffectiverights_object is defined as a
    combination of a Windows file and trustee name. The file represents
    the file to be evaluated while the trustee name represents the
    account (SID) to check effective rights of. If multiple files or
    SIDs are matched by either reference, then each possible combination
    of file and SID is a matching file effective rights object. In
    addition, a number of behaviors may be provided that help guide the
    collection of objects. Please refer to the
    FileEffectiveRightsBehaviors complex type for more information about
    specific behaviors.

    :ivar set:
    :ivar behaviors:
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of a file to
        evaluate. If the xsi:nil attribute is set to true, then the
        object being specified is the higher level directory object (not
        all the files in the directory). In this case, the filename
        element should not be used during collection and would result in
        the unique set of items being the directories themselves. For
        example, one would set xsi:nil to true if the desire was to test
        the attributes or permissions associated with a directory.
        Setting xsi:nil equal to true is different than using a .*
        pattern match, which says to collect every file under a given
        path.
    :ivar trustee_name: The trustee_name element is the unique name that
        associated a particular SID. A SID can be associated with a
        user, group, or program (such as a Windows service). In Windows,
        trustee names are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. In a domain environment, trustee names should be
        identified in the form: "domain\\trustee name". For local
        trustee names use: "computer name\\trustee name". For built-in
        accounts on the system, use the trustee name without a domain.
    """

    class Meta:
        name = "fileeffectiverights_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileEffectiveRightsBehaviors] = field(
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
    trustee_name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Regkeyauditedpermissions53Object(ObjectType):
    """The regkeyauditedpermissions53_object element is used by a registry key
    audited permissions test to define the objects used to evalutate against the
    specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. A
    regkeyauditedpermissions53_object is defined as a combination of a
    Windows registry key and trustee name. The hive and key elements
    represents the registry key to be evaluated while the trustee name
    represents the account (SID) to check audited permissions of. If
    multiple keys or SIDs are matched by either reference, then each
    possible combination of registry key and SID is a matching registry
    key audited permissions object. In addition, a number of behaviors
    may be provided that help guide the collection of objects. Please
    refer to the RegkeyAuditPermissions53Behaviors complex type for more
    information about specific behaviors.

    :ivar set:
    :ivar behaviors:
    :ivar hive: The hive that the registry key belongs to. This is
        restricted to a specific set of values: HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and
        HKEY_USERS.
    :ivar key: The key element describes a registry key to be collected.
        Note that the hive portion of the string should not be included,
        as this data should be found under the hive element. If the
        xsi:nil attribute is set to true, then the object being
        specified is the higher level hive. In this case, the key
        element should not be collected or used in analysis. Setting
        xsi:nil equal to true is different than using a .* pattern
        match. A .* pattern match says to collect every key under a
        given hive.
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the registry key's Security Descriptor.  The scope
        is limited here to avoid unnecessarily resource intensive
        searches for trustees.  Note that the larger scope of all known
        trustees may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "regkeyauditedpermissions53_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RegkeyAuditPermissions53Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hive: Optional[EntityObjectRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class RegkeyauditedpermissionsObject(ObjectType):
    """The regkeyauditedpermissions_object element is used by a registry key
    audited permissions test to define the objects used to evalutate against the
    specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. A
    regkeyauditedpermissions_object is defined as a combination of a
    Windows registry key and trustee name. The hive and key elements
    represents the registry key to be evaluated while the trustee name
    represents the account (SID) to check audited permissions of. If
    multiple keys or SIDs are matched by either reference, then each
    possible combination of file and SID is a matching file audited
    permissions object. In addition, a number of behaviors may be
    provided that help guide the collection of objects. Please refer to
    the RegkeyAuditPermissionsBehaviors complex type for more
    information about specific behaviors.

    :ivar set:
    :ivar behaviors:
    :ivar hive: The hive that the registry key belongs to. This is
        restricted to a specific set of values: HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and
        HKEY_USERS.
    :ivar key: The key element describes a registry key to be collected.
        Note that the hive portion of the string should not be included,
        as this data should be found under the hive element.
    :ivar trustee_name: The trustee_name element is the unique name that
        associated a particular SID. A SID can be associated with a
        user, group, or program (such as a Windows service). In Windows,
        trustee names are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. In a domain environment, trustee names should be
        identified in the form: "domain\\trustee name". For local
        trustee names use: "computer name\\trustee name". For built-in
        accounts on the system, use the trustee name without a domain.
    """

    class Meta:
        name = "regkeyauditedpermissions_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RegkeyAuditPermissionsBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hive: Optional[EntityObjectRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Regkeyeffectiverights53Object(ObjectType):
    """The regkeyeffectiverights53_object element is used by a registry key
    effective rights test to define the objects used to evalutate against the
    specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. A
    regkeyeffectiverights53_object is defined as a combination of a
    Windows registry and trustee SID. The key entity represents the
    registry key to be evaluated while the trustee SID represents the
    account (SID) to check effective rights of. If multiple files or
    SIDs are matched by either reference, then each possible combination
    of registry key and SID is a matching registry key effective rights
    object. In addition, a number of behaviors may be provided that help
    guide the collection of objects. Please refer to the
    RegkeyEffectiveRights53Behaviors complex type for more information
    about specific behaviors.

    :ivar set:
    :ivar behaviors:
    :ivar hive: The hive that the registry key belongs to. This is
        restricted to a specific set of values: HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and
        HKEY_USERS.
    :ivar key: The key element describes a registry key to be collected.
        Note that the hive portion of the string should not be included,
        as this data should be found under the hive element. If the
        xsi:nil attribute is set to true, then the object being
        specified is the higher level hive. In this case, the key
        element should not be collected or used in analysis. Setting
        xsi:nil equal to true is different than using a .* pattern
        match. A .* pattern match says to collect every key under a
        given hive.
    :ivar trustee_sid: The trustee_sid entity identifies a unique SID
        associated with a user, group, system, or program (such as a
        Windows service).  If an operation other than equals is used to
        identify matching trustees (i.e. not equal, or a pattern match)
        then the resulting matches shall be limited to only the trustees
        referenced in the registry key's Security Descriptor.  The scope
        is limited here to avoid unnecessarily resource intensive
        searches for trustees.  Note that the larger scope of all known
        trustees may be obtained through the use of variables.
    :ivar filter:
    """

    class Meta:
        name = "regkeyeffectiverights53_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RegkeyEffectiveRights53Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hive: Optional[EntityObjectRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    trustee_sid: Optional[EntityObjectStringType] = field(
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
class RegkeyeffectiverightsObject(ObjectType):
    """
    :ivar set:
    :ivar behaviors:
    :ivar hive: The hive that the registry key belongs to. This is
        restricted to a specific set of values: HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, and
        HKEY_USERS.
    :ivar key: The key element describes a registry key to be collected.
        Note that the hive portion of the string should not be included,
        as this data should be found under the hive element.
    :ivar trustee_name: The trustee_name element is the unique name that
        associated a particular SID. A SID can be associated with a
        user, group, or program (such as a Windows service). In Windows,
        trustee names are case-insensitive. As a result, it is
        recommended that the case-insensitive operations are used for
        this entity. In a domain environment, trustee names should be
        identified in the form: "domain\\trustee name". For local
        trustee names use: "computer name\\trustee name". For built-in
        accounts on the system, use the trustee name without a domain.
    """

    class Meta:
        name = "regkeyeffectiverights_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#windows"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[RegkeyEffectiveRightsBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hive: Optional[EntityObjectRegistryHiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    trustee_name: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
