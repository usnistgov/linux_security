from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.oval_definitions_schema import (
    EntityObjectIntType,
    EntityObjectStringType,
    EntityStateAnySimpleType,
    EntityStateIntType,
    EntityStateRecordType,
    EntityStateStringType,
    Filter,
    ObjectRefType,
    ObjectType,
    Set,
    StateRefType,
    StateType,
    TestType,
)

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


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


class FileBehaviorsWindowsView(Enum):
    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"


class LdapBehaviorsScope(Enum):
    BASE = "BASE"
    ONE = "ONE"
    SUBTREE = "SUBTREE"


@dataclass
class EntityObjectEngineType(EntityObjectStringType):
    """The EntityObjectEngineType complex type defines a string entity value that
    is restricted to a set of enumerations.

    Each valid enumeration is a valid database engine. The empty string
    is also allowed to support empty elements associated with variable
    references.
    """


@dataclass
class EntityObjectHashTypeType(EntityObjectStringType):
    """The EntityObjectHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityObjectShellType(EntityObjectStringType):
    """The EntityObjectShellType complex type defines a string entity value that is
    restricted to a set of command shells.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityObjectVariableRefType(EntityObjectStringType):
    """The EntityObjectVariableRefType complex type defines a string object entity
    that has a valid OVAL variable id as the value.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityStateEngineType(EntityStateStringType):
    """The EntityStateEngineType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a valid database engine. The empty string
    is also allowed to support empty elements associated with variable
    references.
    """


@dataclass
class EntityStateFamilyType(EntityStateStringType):
    """The EntityStateFamilyType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a high-level family of system operating
    system. The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityStateHashTypeType(EntityStateStringType):
    """The EntityStateHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityStateLdaptypeType(EntityStateStringType):
    """The EntityStateLdaptypeType complex type restricts a string value to a
    specific set of values that specify the different types of information that an
    ldap attribute can represent.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityStateShellType(EntityStateStringType):
    """The EntityStateShellType complex type defines a string entity value that is
    restricted to a set of command shells.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityStateVariableRefType(EntityStateStringType):
    """The EntityStateVariableRefType complex type defines a string state entity
    that has a valid OVAL variable id as the value.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityStateWindowsViewType(EntityStateStringType):
    """The EntityStateWindowsViewType restricts a string value to a specific set of values: 32-bit and 64-bit. These values describe the different values possible for the windows view behavior."""


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
        for this attribute to mean anything. Also note that on Windows,
        the 'symlink' value is equivalent to the 'junction' recurse
        value in win-def:FileBehaviors. Note that this behavior only
        applies with the equality operation on the path entity.
    :ivar recurse_direction: 'recurse_direction' defines the direction
        to recurse, either 'up' to parent directories, or 'down' into
        child directories. The default value is 'none' for no recursion.
        Note that this behavior only applies with the equality operation
        on the path entity.
    :ivar recurse_file_system: 'recurse_file_system' defines the file
        system limitation of any searching and applies to all operations
        as specified on the path or filepath entity. The value of
        'local' limits the search scope to local file systems (as
        opposed to file systems mounted from an external system).  The
        value of 'defined' keeps any recursion within the file system
        that the file_object (path+filename or filepath) has specified.
        For example, on Windows, if the path specified was "C:\\", you
        would search only the C: drive, not other filesystems mounted to
        descendant paths. Similarly, on UNIX, if the path specified was
        "/", you would search only the filesystem mounted there, not
        other filesystems mounted to descendant paths. The value of
        'defined' only applies when an equality operation is used for
        searching because the path or filepath entity must explicitly
        define a file system. The default value is 'all' meaning to
        search all available file systems for data collection. Note that
        in most cases it is recommended that the value of 'local' be
        used to ensure that file system searching is limited to only the
        local file systems. Searching 'all' file systems may have
        performance implications.
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
    windows_view: FileBehaviorsWindowsView = field(
        default=FileBehaviorsWindowsView.VALUE_64_BIT,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LdapBehaviors:
    """
    The LdapBehaviors complex type defines a number of behaviors that allow a more
    detailed definition of the ldap_object being specified.

    :ivar scope: 'scope' defines the depth from the base distinguished
        name to which the search should occur. The base distinguished
        name is the starting point of the search and is composed of the
        specified suffix and relative distinguished name. A value of
        'BASE' indicates to search only the entry at the base
        distinguished name, a value of 'ONE' indicates to search all
        entries one level under the base distinguished name - but NOT
        including the base distinguished name, and a value of 'SUBTREE'
        indicates to search all entries at all levels under, and
        including, the specified base distinguished name. The default
        value is 'BASE'.
    """

    scope: LdapBehaviorsScope = field(
        default=LdapBehaviorsScope.BASE,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Environmentvariable58Object(ObjectType):
    """The environmentvariable58_object element is used by an
    environmentvariable58_test to define the specific environment variable(s) and
    process IDs to be evaluated.

    If a tool is unable to collect the environment variables of another
    process, an error must be reported.  Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. Again, please refer to the description of the
    set element in the oval-definitions-schema.

    :ivar set:
    :ivar pid: The process ID of the process from which the environment
        variable should be retrieved. If the xsi:nil attribute is set to
        true, the process ID shall be the tool's running process; for
        scanners with no process ID (e.g., an agentless network
        scanner), no corresponding items will exist.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar filter:
    """

    class Meta:
        name = "environmentvariable58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
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
class Environmentvariable58State(StateType):
    """
    The environmentvariable58_state element contains three entities that are used
    to check the name of the specified environment variable, the process ID of the
    process from which the environment variable was retrieved, and the value
    associated with the environment variable.

    :ivar pid: The process ID of the process from which the environment
        variable was retrieved.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    pid: Optional[EntityStateIntType] = field(
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
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Environmentvariable58Test(TestType):
    """The environmentvariable58_test element is used to check an environment
    variable for the specified process, which is identified by its process ID, on
    the system .

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    environmentvariable_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "environmentvariable58_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class EnvironmentvariableObject(ObjectType):
    """The environmentvariable_object element is used by an environment variable
    test to define the specific environment variable(s) to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar name: This element describes the name of an environment
        variable.
    """

    class Meta:
        name = "environmentvariable_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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


@dataclass
class EnvironmentvariableState(StateType):
    """
    The environmentvariable_state element contains two entities that are used to
    check the name of the specified environment variable and the value associated
    with it.

    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    name: Optional[EntityStateStringType] = field(
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
class EnvironmentvariableTest(TestType):
    """The environmentvariable_test element is used to check an environment
    variable found on the system.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    environmentvariable_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "environmentvariable_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class FamilyObject(ObjectType):
    """The family_object element is used by a family test to define those objects
    to evaluate based on a specified state.

    There is actually only one object relating to family and this is the
    system as a whole. Therefore, there are no child entities defined.
    Any OVAL Test written to check the family will reference the same
    family_object which is basically an empty object element.
    """

    class Meta:
        name = "family_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )


@dataclass
class FamilyTest(TestType):
    """The family_test element is used to check the family a certain system belongs
    to.

    This test basically allows the high level system types (window,
    unix, ios, etc.) to be tested. It extends the standard TestType as
    defined in the oval-definitions-schema and one should refer to the
    TestType description for more information. The required object
    element references a family_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "family_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class Filehash58Test(TestType):
    """The file hash test is used to check a specific hash type associated with a
    specified file.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    filehash58_object and the optional state element specifies an
    expected hash value.
    """

    class Meta:
        name = "filehash58_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class FilehashTest(TestType):
    """The file hash test is used to check the hashes associated with a specified
    file.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    filehash_object and the optional state element specifies the
    different hashes to check.
    """

    class Meta:
        name = "filehash_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class Ldap57Test(TestType):
    """The LDAP test is used to check information about specific entries in an LDAP
    directory.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an ldap57_object
    and the optional state element, ldap57_state, specifies the metadata
    to check. Note that this test supports complex values that are in
    the form of a record. For simple (string based) value collection see
    the ldap_test.
    """

    class Meta:
        name = "ldap57_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class LdapTest(TestType):
    """The LDAP test is used to check information about specific entries in an LDAP
    directory.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an ldap_object
    and the optional state element, ldap_state, specifies the metadata
    to check.
    """

    class Meta:
        name = "ldap_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class ShellcommandTest(TestType):
    """The shellcommand_test is used to check the values produced by the running of
    the 'command' (or script, but not an external script file) found in the object
    'command' element. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description for more
    information. The required object element references a shellcommand_object and
    the optional state element references a shellcommand_state that specifies the
    information to check. Since this test runs the command string supplied in the
    object command element, the content author should avoid writing command strings
    that may produce large amounts of output or that may be fragile causing errors
    and thus produce large amounts of error output.

    The command should produce well formed output that will result in one item stdout_line element for each line of output via STDOUT by the object evaluation.  Similarly, in the item, for any output to STDERR, a stderr_line element will be created.
    IMPORTANT! - Since this test requires the running of code supplied by content and since OVAL interpreters commonly run with elevated privileges, significant responsibilty falls to the content author to DO NO HARM to the target system.  This also requires that any content stream that employs this test MUST be from a known trusted source and be digitally signed.  The use of any executables that are not supplied by the installed operating system is highly discouraged.
    """

    class Meta:
        name = "shellcommand_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class Sql512Test(TestType):
    """The sql512 test is used to check information stored in a database.

    It extends the standard TestType as defined in the oval-definitions-schema and one should refer to the TestType description for more information.
    This test should only be performed by the OVAL interpreter if the content is 'trusted', such as being digitally signed by a trusted content author.
    The OVAL interpeter will provide all authentication capabilities to the SQL DMBS target.
    The OVAL interpeter will query the target system and find all applicable DBMS instances and databases (refer to sql512 object elements for more information on instances and databases) .
    Using Microsoft SQL Server as an example, below is sample of what the OVAL intepreter will gather from a target.
    Target Host: Host1
    SQL Server Instances:
    SQLEXPRESS (version 13.0.6450.1 )
    Databases:
    master
    model
    msdb
    tempdb
    userdb1
    userdb2
    SQLSERVER (version 16.0.4135.4)
    Databases:
    master
    model
    msdb
    tempdb
    testdb1
    testdb2
    Content can then be created that targets one or more versions, and within those versions, queries could be run against one or more instances and one ore more databases.
    """

    class Meta:
        name = "sql512_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class Sql57Test(TestType):
    """The sql test is used to check information stored in a database.

    It is often the case that applications store configuration settings
    in a database as opposed to a file. This test has been designed to
    enable those settings to be tested. It extends the standard TestType
    as defined in the oval-definitions-schema and one should refer to
    the TestType description for more information. The required object
    element references a wmi_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "sql57_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class SqlTest(TestType):
    """The sql test is used to check information stored in a database.

    It is often the case that applications store configuration settings
    in a database as opposed to a file. This test has been designed to
    enable those settings to be tested. It extends the standard TestType
    as defined in the oval-definitions-schema and one should refer to
    the TestType description for more information. The required object
    element references a wmi_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "sql_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class Textfilecontent54Test(TestType):
    """The textfilecontent54_test element is used to check the contents of a text
    file (aka a configuration file) by looking at individual blocks of text.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    textfilecontent54_object and the optional state element specifies
    the metadata to check.
    """

    class Meta:
        name = "textfilecontent54_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class TextfilecontentTest(TestType):
    """The textfilecontent_test element is used to check the contents of a text
    file (aka a configuration file) by looking at individual lines.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    textfilecontent_object and the optional state element specifies the
    metadata to check.
    """

    class Meta:
        name = "textfilecontent_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class UnknownTest(TestType):
    """An unknown_test acts as a placeholder for tests whose implementation is
    unknown.

    This test always evaluates to a result of 'unknown'. Any information
    that is known about the test should be held in the notes child
    element that is available through the extension of the abstract test
    element. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. Note that for an unknown_test, the required
    check attribute that is part of the extended TestType should be
    ignored during evaluation and hence can be set to any valid value.
    """

    class Meta:
        name = "unknown_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )


@dataclass
class VariableTest(TestType):
    """The variable test allows the value of a variable to be compared to a defined
    value.

    As an example one might use this test to validate that a variable
    being passed in from an external source falls within a specified
    range. It extends the standard TestType as defined in the oval-
    definitions-schema and one should refer to the TestType description
    for more information. The required object element references a
    variable_object and the optional state element specifies the value
    to check.
    """

    class Meta:
        name = "variable_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class XmlfilecontentTest(TestType):
    """The xmlfilecontent_test element is used to explore the contents of an xml
    file.

    This test allows specific pieces of an xml document specified using
    xpath to be tested. It extends the standard TestType as defined in
    the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a xmlfilecontent_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "xmlfilecontent_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class YamlfilecontentTest(TestType):
    """The yamlfilecontent_test element is used to explore the contents of an YAML
    file.

    This test allows specific pieces of an YAML document specified using
    YAML Path to be tested. It extends the standard TestType as defined
    in the oval-definitions-schema and one should refer to the TestType
    description for more information. The required object element
    references a yamlfilecontent_object and the optional state element
    specifies the metadata to check.
    """

    class Meta:
        name = "yamlfilecontent_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
class Textfilecontent54Behaviors(FileBehaviors):
    """The Textfilecontent54Behaviors complex type defines a number of behaviors
    that allow a more detailed definition of the textfilecontent54_object being
    specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file. The
    Textfilecontent54Behaviors extend the ind-def:FileBehaviors and
    therefore include the behaviors defined by that type.

    :ivar ignore_case: 'ignore_case' indicates whether case should be
        considered when matching system values against the regular
        expression provided by the pattern entity. This behavior is
        intended to align with the Perl regular expression 'i' modifier:
        if true, case will be ignored.  If false, case will not be
        ignored. The default is false.
    :ivar multiline: 'multiline' enables multiple line semantics in the
        regular expression provided by the pattern entity. This behavior
        is intended to align with the Perl regular expression 'm'
        modifier: if true, the '^' and '$' metacharacters will match
        both at the beginning/end of a string, and immediately
        after/before newline characters.  If false, they will match only
        at the beginning/end of a string.  The default is true.
    :ivar singleline: 'singleline' enables single line semantics in the
        regular expression provided by the pattern entity. This behavior
        is intended to align with the Perl regular expression 's'
        modifier: if true, the '.' metacharacter will match newlines. If
        false, it will not.  The default is false.
    """

    ignore_case: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    multiline: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    singleline: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FamilyState(StateType):
    """The family_state element contains a single entity that is used to check the
    family associated with the system.

    The family is a high-level classification of system types.

    :ivar family: This element describes the high-level system OS type
        to test against. Please refer to the definition of the
        EntityFamilyType for more information about the possible
        values..
    """

    class Meta:
        name = "family_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    family: Optional[EntityStateFamilyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Filehash58Object(ObjectType):
    """The filehash58_object element is used by a file hash test to define the
    specific file(s) to be evaluated.

    The filehash58_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema. A
    filehash58_object defines the path and filename of the file(s). In
    addition, a number of behaviors may be provided that help guide the
    collection of objects. Please refer to the FileBehaviors complex
    type for more information about specific behaviors. The set of files
    to be evaluated may be identified with either a complete filepath or
    a path and filename. Only one of these options may be selected. It
    is important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path entity specifies the directory component of the
        absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of the file.
    :ivar hash_type: The hash_type entity specifies the hash algorithm
        to use when collecting the hash for each of the specifed files.
    :ivar filter:
    """

    class Meta:
        name = "filehash58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    hash_type: Optional[EntityObjectHashTypeType] = field(
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
class Filehash58State(StateType):
    """
    The filehash58_state element contains entities that are used to check the file
    path, name, hash_type, and hash associated with a specific file.

    :ivar filepath: The filepath entity specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path entity specifies the directory component of the
        absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of the file.
    :ivar hash_type: The hash_type entity specifies the hash algorithm
        to use when collecting the hash for each of the specifed files.
    :ivar hash: The hash entity specifies the result of applying the
        hash algorithm to the file.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "filehash58_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    hash_type: Optional[EntityStateHashTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hash: Optional[EntityStateStringType] = field(
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
class FilehashObject(ObjectType):
    """The filehash_object element is used by a file hash test to define the
    specific file(s) to be evaluated.

    The filehash_object will only collect regular files on UNIX systems
    and FILE_TYPE_DISK files on Windows systems. Each object extends the
    standard ObjectType as defined in the oval-definitions-schema and
    one should refer to the ObjectType description for more information.
    The common set element allows complex objects to be created using
    filters and set logic. Again, please refer to the description of the
    set element in the oval-definitions-schema. A filehash_object
    defines the path and filename of the file(s). In addition, a number
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
    :ivar filename: The filename element specifies the name of the file.
    """

    class Meta:
        name = "filehash_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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


@dataclass
class FilehashState(StateType):
    """
    The filehash_state element contains entities that are used to check the file
    path, name, and the different hashes associated with a specific file.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar md5: The md5 element is the md5 hash of the file.
    :ivar sha1: The sha1 element is the sha1 hash of the file.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "filehash_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    md5: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sha1: Optional[EntityStateStringType] = field(
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
class Ldap57Object(ObjectType):
    """The ldap57_object element is used by an LDAP test to define the objects to
    be evaluated based on a specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. Note that this object supports complex values
    that are in the form of a record. For simple (string based) value
    collection see the ldap_object.

    :ivar set:
    :ivar behaviors:
    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified suffix. It contains all
        of the parts of the object's distinguished name except those
        outlined by the suffix. If the xsi:nil attribute is set to true,
        then the object being specified is the higher level suffix. In
        this case, the relative_dn element should not be collected or
        used in analysis. Setting xsi:nil equal to true is different
        than using a .* pattern match, which says to collect every
        relative distinguished name under a given suffix.
    :ivar attribute: Specifies a named value contained by the object. If
        the xsi:nil attribute is set to true, the attribute element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every attribute under a given relative
        distinguished name.
    :ivar filter:
    """

    class Meta:
        name = "ldap57_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[LdapBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    suffix: Optional[EntityObjectStringType] = field(
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
class Ldap57State(StateType):
    """The ldap57_state element defines the different information that can be used
    to evaluate the specified entries in an LDAP directory.

    An ldap57_test will reference a specific instance of this state that
    defines the exact settings that need to be evaluated. Please refer
    to the individual elements in the schema for more details about what
    each represents. Note that this state supports complex values that
    are in the form of a record. For simple (string based) value
    collection see the ldap_state.

    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified suffix. It contains all
        of the parts of the object's distinguished name except those
        outlined by the suffix.
    :ivar attribute: Specifies a named value contained by the object.
    :ivar object_class: The name of the class of which the object is an
        instance.
    :ivar ldaptype: Specifies the type of information that the specified
        attribute represents.
    :ivar value: The actual value of the specified LDAP attribute. Note
        that while an LDAP attribute can contain structured data where
        it is necessary to collect multiple related fields that can be
        described by the 'record' datatype, it is not always the case.
        It also is possible that an LDAP attribute can contain only a
        single value or an array of values. In these cases, there is not
        a name to uniquely identify the corresponding field which is a
        requirement for fields in the 'record' datatype.  As a result,
        the name of the LDAP attribute will be used to uniquely identify
        the field and satisfy this requirement.
    """

    class Meta:
        name = "ldap57_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    suffix: Optional[EntityStateStringType] = field(
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
    ldaptype: Optional[EntityStateLdaptypeType] = field(
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
class LdapObject(ObjectType):
    """The ldap_object element is used by an LDAP test to define the objects to be
    evaluated based on a specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified suffix. It contains all
        of the parts of the object's distinguished name except those
        outlined by the suffix. If the xsi:nil attribute is set to true,
        then the object being specified is the higher level suffix. In
        this case, the relative_dn element should not be collected or
        used in analysis. Setting xsi:nil equal to true is different
        than using a .* pattern match, which says to collect every
        relative distinguished name under a given suffix.
    :ivar attribute: Specifies a named value contained by the object. If
        the xsi:nil attribute is set to true, the attribute element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every attribute under a given relative
        distinguished name.
    """

    class Meta:
        name = "ldap_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[LdapBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    suffix: Optional[EntityObjectStringType] = field(
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
class LdapState(StateType):
    """The ldap_state element defines the different information that can be used to
    evaluate the specified entries in an LDAP directory.

    An ldap_test will reference a specific instance of this state that
    defines the exact settings that need to be evaluated. Please refer
    to the individual elements in the schema for more details about what
    each represents.

    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified suffix. It contains all
        of the parts of the object's distinguished name except those
        outlined by the suffix.
    :ivar attribute: Specifies a named value contained by the object.
    :ivar object_class: The name of the class of which the object is an
        instance.
    :ivar ldaptype: Specifies the type of information that the specified
        attribute represents.
    :ivar value: The actual value of the specified LDAP attribute.
    """

    class Meta:
        name = "ldap_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    suffix: Optional[EntityStateStringType] = field(
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
    ldaptype: Optional[EntityStateLdaptypeType] = field(
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
class ShellcommandObject(ObjectType):
    """The shellcommand_object is used by a shellcommand_test to define a shell to
    use (e.g. sh, bash, ksh, etc.), a command (or shell script) to be run, and a
    pattern to filter result lines.

    The default shell is bash.  Each object extends the standard
    ObjectType as defined in the oval-definitions-schema and one should
    refer to the ObjectType description for more information. The common
    set element allows complex objects to be created using filters and
    set logic. The evaluation of the object should always produce one
    item. If the command execution does not produce output, an item
    should still be created with the exit_status (AKA process exit
    code), a stdout entity with a status of 'does not exist', and any
    STDERR from the execution captured in stderr_line entities.

    :ivar set:
    :ivar shell: The shell entity defines the specific shell to use
        (e.g. bash, csh, ksh, etc.). Any tool collecting information for
        this object will need to know the shell in order to use it
        properly.
    :ivar command: The command element specifies the command string to
        be run on the target system.  Since this command string will be
        executed on the target system and since OVAL interpreters
        commonly run with elevated privileges, significant responsibilty
        falls to the content author to DO NO HARM.  This also requires
        that any content stream that employs this test MUST be from a
        known trusted source and be digitally signed.  The use of
        executables that are not supplied by the installed operating
        system is highly discouraged.
    :ivar pattern: The 'pattern' is a regular expression that identifies
        lines in 'command' results that are to produce OVAL items.   Any
        result line via STDOUT that matches the pattern is kept as an
        item stdout_line element.  Any that do not are discarded.  If
        the pattern element is empty or does not exist, all results
        lines are kept. A subexpression (using parentheses) can call out
        a piece of the matched stdout_line to test. For example, the
        pattern abc(.*)xyz would look for a block of text in the output
        that starts with abc and ends with xyz, with the subexpression
        being all the characters that exist in between. The value of the
        subexpression can then be tested using the subexpression entity
        of a shellcommand_state. Note that if the pattern, starting at
        the same point in the line, matches more than one block of text,
        then it matches the longest. For example, given output with
        abcdefxyzxyzabc, then the pattern abc(.*)xyz would match the
        block abcdefxyzxyz. Subexpressions also match the longest
        possible substrings, subject to the constraint that the whole
        match be as long as possible, with subexpressions starting
        earlier in the pattern taking priority over ones starting later.
        Note that when using regular expressions, OVAL supports a common
        subset of the regular expression character classes, operations,
        expressions and other lexical tokens defined within Perl 5's
        regular expression specification. For more information on the
        supported regular expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html.
    :ivar filter:
    """

    class Meta:
        name = "shellcommand_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    shell: Optional[EntityObjectShellType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    command: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pattern: Optional[EntityObjectStringType] = field(
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
class ShellcommandState(StateType):
    """The shellcommand_state contains the entities that are used to check the
    values returned by the shellcommand_object.

    Note that the state entities shell, command, and pattern are echoed,
    verbatim, from the same elements in the associated
    shellcommand_object.

    :ivar shell: The 'shell' element contains the shell used to perform
        the command and must match the value in the associated object,
        verbatim.
    :ivar command: The 'command' element specifies the command string to
        be run on the target system and must match the same element in
        the associated shellcommand_object, verbatim.
    :ivar pattern: The 'pattern' is a regular expression that identifies
        lines in 'command' results that are to produce OVAL items and
        must match the same element in the associated
        shellcommand_object, verbatim.
    :ivar exit_status: The 'exit_status' entity represents the exist
        status returned by the system for the execution of the object
        command.
    :ivar stdout_line: The 'stdout_line' entity represents a line from
        the STDOUT output of a successful run of the command string that
        matched the specified object pattern.
    :ivar subexpression: The subexpression entity represents a value to
        test against the subexpression in the specified pattern. If
        multiple subexpressions are specified in the pattern, this value
        is tested against all of them. For example, if the pattern
        abc(.*)mno(.*)xyp was supplied, and the state specifies a
        subexpression value of enabled, then the test would check that
        both (or at least one, none, etc. depending on the entity_check
        attribute) of the subexpressions have a value of enabled.
    :ivar stderr_line: The 'stderr_line' element contains any and all
        output to STDERR from a run of the object command.  Each line of
        STDERR should create an additional 'stderr_line' element.
    """

    class Meta:
        name = "shellcommand_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    shell: Optional[EntityStateShellType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    command: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    pattern: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exit_status: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    stdout_line: list[EntityStateAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    stderr_line: list[EntityStateStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Sql512Object(ObjectType):
    """The sql512_object element is used by a sql512 test to define the specific
    database and query to be evaluated.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar engine: The engine entity defines the specific database engine
        to use. Any tool looking to collect information about this
        object will need to know the engine in order to use the
        appropriate drivers to establish a connection.
    :ivar version: The version entity defines the specific version of
        the database engine to use. The version shall be reported in the
        format provided by the dbms application, which may differ
        slightly across dbms products, but should generally be in the
        foramt of X.Y.Z Below are some examples, but make sure to refer
        to DBMS system documentation for complete/current methods to
        determine versions For Microsoft SQL Server, the version can be
        obtained with 'SELECT SERVERPROPERTY('productversion')' For
        Oracle DBMS, the version can be obtained with 'SELECT * FROM
        V$VERSION;' For MySQL and MariaDB, the version can be obtained
        with 'SELECT version();' Usage of regular expressions is
        recommended in order to match on a primary version or multiple
        versions of the dbms.
    :ivar instance: The instance entity defines the specific instance
        name to be used when connecting to the correct database, where
        instance refers to the running instance of the DMBS software
        itself. This could be a separate installation of binaries (such
        as with MS SQL Server), or just a set of running processes used
        to manage the DBMS. The OVAL interpreter will automatically
        determine the list of available instances on the target. When a
        pattern or string is entered, the OVAL interpeter will consider
        any matching instance as in scope for analysis.
    :ivar database: The database entity defines the specific database
        name to be used when connecting to the specified instance, where
        a database is defined as a collection of tables within a DBMS
        instance. When a pattern or string is entered, the OVAL
        interpeter will perform the query against any matching
        databases. If the xsi:nil attribute is set to true, then the
        OVAL interpreter will perform the query once per instance.  This
        is primarily useful for queries that gather instance
        configuration settings, such as SQL Servers SERVERPROPERTY data.
        See https://learn.microsoft.com/en-
        us/sql/t-sql/functions/serverproperty-transact-sql?view=sql-
        server-ver16 Example: SELECT SERVERPROPERTY('IsClustered') AS
        [is_clustered]
    :ivar sql: The sql entity defines a query used to identify the
        object(s) to test against. Any valid SQL query is usable with
        one exception, all fields must be named in the SELECT portion of
        the query. For example, SELECT name, number FROM ... is valid.
        However, SELECT * FROM ... is not valid. This is because the
        record element in the state and item require a unique field name
        value to ensure that any query results can be evaluated
        consistently. If the xsi:nil attribute is set to true, then no
        query is executed and only the existance of the specified
        instance and database will be considered.
    :ivar filter:
    """

    class Meta:
        name = "sql512_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    engine: Optional[EntityObjectEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    database: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    sql: Optional[EntityObjectStringType] = field(
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
class Sql512State(StateType):
    """
    The sql512_state element contains two entities that are used to check the name
    of the specified field and the value associated with it.

    :ivar engine: The engine entity defines a specific database engine.
    :ivar version: The version entity defines a specific version of a
        given database engine.
    :ivar instance: The instance entity defines the specific instance
        name to be used when connecting to the correct database.
    :ivar database: The database entity defines the specific database
        name to be used when connecting to the specified instance.
    :ivar sql: the sql entity defines a query used to identify the
        object(s) to test against.
    :ivar result: The result entity specifies how to test objects in the
        result set of the specified SQL statement.
    """

    class Meta:
        name = "sql512_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    engine: Optional[EntityStateEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    database: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityStateStringType] = field(
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
class Sql57Object(ObjectType):
    """The sql57_object element is used by a sql test to define the specific
    database and query to be evaluated.

    Connection information is supplied allowing the tool to connect to
    the desired database and a query is supplied to call out the desired
    setting. Each object extends the standard ObjectType as defined in
    the oval-definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar engine: The engine entity defines the specific database engine
        to use. Any tool looking to collect information about this
        object will need to know the engine in order to use the
        appropriate drivers to establish a connection.
    :ivar version: The version entity defines the specific version of
        the database engine to use. This is also important in
        determining the correct driver to use for establishing a
        connection.
    :ivar connection_string: The connection_string entity defines
        specific connection parameters to be used in connecting to the
        database. This will help a tool connect to the correct database.
    :ivar sql: The sql entity defines a query used to identify the
        object(s) to test against. Any valid SQL query is usable with
        one exception, all fields must be named in the SELECT portion of
        the query. For example, SELECT name, number FROM ... is valid.
        However, SELECT * FROM ... is not valid. This is because the
        record element in the state and item require a unique field name
        value to ensure that any query results can be evaluated
        consistently.
    :ivar filter:
    """

    class Meta:
        name = "sql57_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    engine: Optional[EntityObjectEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityObjectStringType] = field(
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
class Sql57State(StateType):
    """
    The sql57_state element contains two entities that are used to check the name
    of the specified field and the value associated with it.

    :ivar engine: The engine entity defines a specific database engine.
    :ivar version: The version entity defines a specific version of a
        given database engine.
    :ivar connection_string: The connection_string entity defines a set
        of parameters that help identify the connection to the database.
    :ivar sql: the sql entity defines a query used to identify the
        object(s) to test against.
    :ivar result: The result entity specifies how to test objects in the
        result set of the specified SQL statement.
    """

    class Meta:
        name = "sql57_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    engine: Optional[EntityStateEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityStateStringType] = field(
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
class SqlObject(ObjectType):
    """The sql_object element is used by a sql test to define the specific database
    and query to be evaluated.

    Connection information is supplied allowing the tool to connect to
    the desired database and a query is supplied to call out the desired
    setting. Each object extends the standard ObjectType as defined in
    the oval-definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar engine: The engine entity defines the specific database engine
        to use. Any tool looking to collect information about this
        object will need to know the engine in order to use the
        appropriate drivers to establish a connection.
    :ivar version: The version entity defines the specific version of
        the database engine to use. This is also important in
        determining the correct driver to use for establishing a
        connection.
    :ivar connection_string: The connection_string entity defines
        specific connection parameters to be used in connecting to the
        database. This will help a tool connect to the correct database.
    :ivar sql: The sql entity defines a query used to identify the
        object(s) to test against. Any valid SQL query is usable with
        one exception, at most one field is allowed in the SELECT
        portion of the query. For example SELECT name FROM ... is valid,
        as is SELECT 'true' FROM ..., but SELECT name, number FROM ...
        is not valid. This is because the result element in the data
        section is only designed to work against a single field.
    """

    class Meta:
        name = "sql_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    engine: Optional[EntityObjectEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SqlState(StateType):
    """
    The sql_state element contains two entities that are used to check the name of
    the specified field and the value associated with it.

    :ivar engine: The engine entity defines a specific database engine.
    :ivar version: The version entity defines a specific version of a
        given database engine.
    :ivar connection_string: The connection_string entity defines a set
        of parameters that help identify the connection to the database.
    :ivar sql: the sql entity defines a query used to identify the
        object(s) to test against.
    :ivar result: The result entity specifies how to test objects in the
        result set of the specified SQL statement. Only one comparable
        field is allowed. So if the SQL statement look like 'SELECT name
        FROM ...', then a result entity with a value of 'Fred' would
        test the set of 'name' values returned by the SQL statement
        against the value 'Fred'.
    """

    class Meta:
        name = "sql_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    engine: Optional[EntityStateEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityStateStringType] = field(
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
class Textfilecontent54State(StateType):
    """
    The textfilecontent54_state element contains entities that are used to check
    the file path and name, as well as the text block in question and the value of
    the subexpressions.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename entity represents the name of a file.
    :ivar pattern: The pattern entity represents a regular expression
        that is used to define a block of text.
    :ivar instance: The instance entity calls out a specific match of
        the pattern. This can only be a positive integer.
    :ivar text: The text entity represents the block of text that
        matched the specified pattern.
    :ivar subexpression: The subexpression entity represents a value to
        test against the subexpression in the specified pattern. If
        multiple subexpressions are specified in the pattern, this value
        is tested against all of them. For example, if the pattern
        abc(.*)mno(.*)xyp was supplied, and the state specifies a
        subexpression value of enabled, then the test would check that
        both (or at least one, none, etc. depending on the entity_check
        attribute) of the subexpressions have a value of enabled.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "textfilecontent54_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    pattern: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    text: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: Optional[EntityStateAnySimpleType] = field(
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
class TextfilecontentObject(ObjectType):
    """The textfilecontent_object element is used by a text file content test to
    define the specific line(s) of a file(s) to be evaluated.

    The textfilecontent_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar line: The line element represents a line in the file and is
        represented using a regular expression. A single subexpression
        can be called out using parentheses. The value of this
        subexpression can then be checked using a textfilecontent_state.
        Note that when using regular expressions, OVAL supports a common
        subset of the regular expression character classes, operations,
        expressions and other lexical tokens defined within Perl 5's
        regular expression specification. For more information on the
        supported regular expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html.
    """

    class Meta:
        name = "textfilecontent_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    line: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TextfilecontentState(StateType):
    """
    The textfilecontent_state element contains entities that are used to check the
    file path and name, as well as the line in question and the value of the
    specific subexpression.

    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar line: The line element represents a line in the file that was
        collected.
    :ivar subexpression: Each subexpression in the regular expression of
        the line element is then tested against the value specified in
        the subexpression element.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "textfilecontent_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    line: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: Optional[EntityStateAnySimpleType] = field(
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
class VariableObject(ObjectType):
    """
    :ivar set:
    :ivar var_ref: The id of the variable you want.
    :ivar filter:
    """

    class Meta:
        name = "variable_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    var_ref: Optional[EntityObjectVariableRefType] = field(
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
class VariableState(StateType):
    """
    The variable_state element contains two entities that are used to check the
    var_ref of the specified varible and the value associated with it.

    :ivar var_ref: The id of the variable.
    :ivar value: The value of the variable.
    """

    class Meta:
        name = "variable_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    var_ref: Optional[EntityStateVariableRefType] = field(
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
class XmlfilecontentObject(ObjectType):
    """The xmlfilecontent_object element is used by a xml file content test to
    define the specific piece of an xml file(s) to be evaluated.

    The xmlfilecontent_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema. The
    set of files to be evaluated may be identified with either a
    complete filepath or a path and filename. Only one of these options
    may be selected. It is important to note that the 'max_depth' and
    'recurse_direction' attributes of the 'behaviors' element do not
    apply to the 'filepath' element, only to the 'path' and 'filename'
    elements.  This is because the 'filepath' element represents an
    absolute path to a particular file and it is not possible to recurse
    over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar xpath: Specifies an XPath 1.0 expression to evaluate against
        the XML file specified by the filename entity.  This XPath 1.0
        expression must evaluate to a list of zero or more text values
        which will be accessible in OVAL via instances of the value_of
        entity.  Any results from evaluating the XPath 1.0 expression
        other than a list of text strings (e.g., a nodes set) is
        considered an error.  The intention is that the text values be
        drawn from instances of a single, uniquely named element or
        attribute.  However, an OVAL interpreter is not required to
        verify this, so the author should define the XPath expression
        carefully.  Note that "equals" is the only valid operator for
        the xpath entity.
    :ivar filter:
    """

    class Meta:
        name = "xmlfilecontent_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    xpath: Optional[EntityObjectStringType] = field(
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
class XmlfilecontentState(StateType):
    """
    The xmlfilecontent_state element contains entities that are used to check the
    file path and name, as well as the xpath used and the value of the this xpath.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar xpath: Specifies an XPath 1.0 expression to evaluate against
        the XML file specified by the filename entity.  This XPath 1.0
        expression must evaluate to a list of zero or more text values
        which will be accessible in OVAL via instances of the value_of
        entity.  Any results from evaluating the XPath 1.0 expression
        other than a list of text strings (e.g., a nodes set) is
        considered an error.  The intention is that the text values be
        drawn from instances of a single, uniquely named element or
        attribute.  However, an OVAL interpreter is not required to
        verify this, so the author should define the XPath expression
        carefully.  Note that "equals" is the only valid operator for
        the xpath entity.
    :ivar value_of: The value_of element checks the value(s) of the text
        node(s) or attribute(s) found.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "xmlfilecontent_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    xpath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value_of: Optional[EntityStateAnySimpleType] = field(
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
class YamlfilecontentObject(ObjectType):
    """The yamlfilecontent_object element is used by a YAML file content test to
    define the specific piece of an YAML file(s) to be evaluated.

    The yamlfilecontent_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema. The
    set of files to be evaluated may be identified with either a
    complete filepath or a path and filename. Only one of these options
    may be selected. It is important to note that the 'max_depth' and
    'recurse_direction' attributes of the 'behaviors' element do not
    apply to the 'filepath' element, only to the 'path' and 'filename'
    elements.  This is because the 'filepath' element represents an
    absolute path to a particular file and it is not possible to recurse
    over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar content: The content element specifies the YAML document body.
        It also could reference a variable containing the document using
        var_ref attribute. Note that "equals" is the only valid operator
        for the content entity.
    :ivar yamlpath: Specifies an YAML Path expression to evaluate
        against the YAML file specified by the filename entity. This
        YAML Path expression must evaluate to a sequence or a map (part
        of a map) of scalar values which will be accessible in OVAL via
        instances of the value entity. Any results from evaluating the
        YAML Path expression other than a sequence (or a map) of scalar
        values (e.g. sequence of sequences, sequence of maps, map of
        maps etc.) are considered as incorrect, so the author should
        define the YAML Path expression carefully. Note that "equals" is
        the only valid operator for the yamlpath entity.
    :ivar filter:
    """

    class Meta:
        name = "yamlfilecontent_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    content: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    yamlpath: Optional[EntityObjectStringType] = field(
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
class YamlfilecontentState(StateType):
    """
    The yamlfilecontent_state element contains entities that are used to check the
    file path and name, as well as the YAML Path used and the value of the this
    YAML Path.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar content: The content element specifies the YAML document body.
        Note that "equals" is the only valid operator for the content
        entity.
    :ivar yamlpath: Specifies an YAML Path expression to evaluate
        against the YAML file specified by the filename entity. Note
        that "equals" is the only valid operator for the yamlpath
        entity.
    :ivar value: The value entity specifies how to test objects in the
        value set of the specified YAML Path. To define tests for a
        single scalar value or a list of scalar values (where there is
        no key to associate), set the name attribute of the field
        element to '#'. Due to the limitation of the record type field
        names could not contain uppercase letters, they should be
        converted to the lowercase and escaped using the '^' symbol (the
        '^' symbol should be escaped as well). For example, to check a
        value associated with 'myCamelCase^Key' set the name attribute
        of the field to 'my^camel^case^^^key'. The check is entirely
        controlled by operator attributes of the field element.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "yamlfilecontent_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
    content: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    yamlpath: Optional[EntityStateStringType] = field(
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
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Textfilecontent54Object(ObjectType):
    """The textfilecontent54_object element is used by a textfilecontent_test to
    define the specific block(s) of text of a file(s) to be evaluated.

    The textfilecontent54_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema. The
    set of files to be evaluated may be identified with either a
    complete filepath or a path and filename. Only one of these options
    may be selected. It is important to note that the 'max_depth' and
    'recurse_direction' attributes of the 'behaviors' element do not
    apply to the 'filepath' element, only to the 'path' and 'filename'
    elements.  This is because the 'filepath' element represents an
    absolute path to a particular file and it is not possible to recurse
    over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of a file.
    :ivar pattern: The pattern entity defines a chunk of text in a file
        and is represented using a regular expression. A subexpression
        (using parentheses) can call out a piece of the text block to
        test. For example, the pattern abc(.*)xyz would look for a block
        of text in the file that starts with abc and ends with xyz, with
        the subexpression being all the characters that exist in
        between. The value of the subexpression can then be tested using
        the subexpression entity of a textfilecontent54_state. Note that
        if the pattern, starting at the same point in the file, matches
        more than one block of text, then it matches the longest. For
        example, given a file with abcdefxyzxyzabc, then the pattern
        abc(.*)xyz would match the block abcdefxyzxyz. Subexpressions
        also match the longest possible substrings, subject to the
        constraint that the whole match be as long as possible, with
        subexpressions starting earlier in the pattern taking priority
        over ones starting later. Note that when using regular
        expressions, OVAL supports a common subset of the regular
        expression character classes, operations, expressions and other
        lexical tokens defined within Perl 5's regular expression
        specification. For more information on the supported regular
        expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html.
    :ivar instance: The instance entity calls out a specific match of
        the pattern. It can have any integer value. If the value is a
        non-negative integer, the index of the specific match of the
        pattern is counted from the beginning of the set of matches of
        that pattern in the targeted file. The first match is given an
        instance value of 1, the second match is given an instance value
        of 2, and so on. For non-negative values, the 'less than' and
        'less than or equal' operations imply the the object is
        operating only on non-negative values. Frequently, this entity
        will be defined as 'greater than or equal' to 1 or 'greater
        than' 0, either of which results in the object representing the
        set of all matches of the pattern. Negative values are used to
        simplify collection of pattern match occurrences counting
        backwards from the final match in the targeted file. To find the
        final match, use an instance of -1; the penultimate match is
        found using an instance value of -2, and so on. For negative
        values, the 'greater than' and 'greater than or equal'
        operations imply the object is operating only on negative
        values. For example, searching for instances greater than or
        equal to -2 would yield only the last two maches. Note that the
        main purpose of the instance item entity is to provide
        uniqueness for different textfilecontent_items that results from
        multiple matches of a given pattern against the same file, and
        they will always have positive values.
    :ivar filter:
    """

    class Meta:
        name = "textfilecontent54_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[Textfilecontent54Behaviors] = field(
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
    pattern: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[EntityObjectIntType] = field(
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
