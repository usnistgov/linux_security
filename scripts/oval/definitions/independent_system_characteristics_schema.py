from dataclasses import dataclass, field
from typing import Optional

from oval.definitions.oval_system_characteristics_schema import (
    EntityItemAnySimpleType,
    EntityItemIntType,
    EntityItemRecordType,
    EntityItemStringType,
    ItemType,
)

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class EntityItemEngineType(EntityItemStringType):
    """The EntityItemEngineType complex type defines a string entity value that is
    restricted to an enumeration.

    Each valid entry in the enumeration is a valid database engine.
    """


@dataclass
class EntityItemFamilyType(EntityItemStringType):
    """The EntityItemFamilyType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a high-level family of system operating
    system.
    """


@dataclass
class EntityItemHashTypeType(EntityItemStringType):
    """The EntityItemHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


@dataclass
class EntityItemLdaptypeType(EntityItemStringType):
    """The EntityItemLdaptypeType complex type restricts a string value to a
    specific set of values that specify the different types of information that an
    ldap attribute can represent.

    The empty string value is permitted here to allow for detailed error
    reporting.
    """


@dataclass
class EntityItemShellType(EntityItemStringType):
    """The EntityItemShellType restricts a string value to a specific set of shell
    commands.

    The empty string is also allowed to support empty elements
    associated with error conditions.
    """


@dataclass
class EntityItemVariableRefType(EntityItemStringType):
    """
    The EntityItemVariableRefType complex type defines a string item entity that
    has a valid OVAL variable id as the value.
    """


@dataclass
class EntityItemWindowsViewType(EntityItemStringType):
    """The EntityItemWindowsViewType restricts a string value to a specific set of values: 32-bit and 64-bit. These values describe the different values possible for the windows view behavior."""


@dataclass
class Environmentvariable58Item(ItemType):
    """
    This item stores information about an environment variable, the process ID of
    the process from which it was retrieved, and its corresponding value.

    :ivar pid: The process ID of the process from which the environment
        variable was retrieved.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable58_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    pid: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityItemAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnvironmentvariableItem(ItemType):
    """
    This item stores information about environment variables and their values.

    :ivar name: This element describes the name of an environment
        variable.
    :ivar value: The actual value of the specified environment variable.
    """

    class Meta:
        name = "environmentvariable_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    name: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[EntityItemAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FamilyItem(ItemType):
    """
    This element stores high level system OS type, otherwise known as the family.

    :ivar family: This element describes the high level system OS type,
        otherwise known as the family.
    """

    class Meta:
        name = "family_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    family: Optional[EntityItemFamilyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Filehash58Item(ItemType):
    """
    This element stores a hash value associated with a specific file.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar hash_type: Identifier for the hash algorithm used to calculate
        the hash.
    :ivar hash: The result of applying the hash algorithm to the file.
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "filehash58_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

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
        },
    )
    hash_type: Optional[EntityItemHashTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hash: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FilehashItem(ItemType):
    """
    This element stores the different hash values associated with a specific file.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file.
    :ivar md5: The md5 hash of the file
    :ivar sha1: The sha1 hash of the file
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "filehash_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

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
        },
    )
    md5: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sha1: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Ldap57Item(ItemType):
    """This element holds information about specific entries in the LDAP directory.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an item inside the specified suffix. It contains all of
        the parts of the item's distinguished name except those outlined
        by the suffix. If the xsi:nil attribute is set to true, then the
        item being represented is the higher level suffix.
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
        a name to uniquely identify the corresponding field(s) which is
        a requirement for fields in the 'record' datatype.  As a result,
        the name of the LDAP attribute will be used to uniquely identify
        the field(s) and satisfy this requirement. If the LDAP attribute
        contains a single value, the 'record' will have a single field
        identified by the name of the LDAP attribute. If the LDAP
        attribute contains an array of values, the 'record' will have
        multiple fields all identified by the name of the LDAP
        attribute.
    """

    class Meta:
        name = "ldap57_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    suffix: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    object_class: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ldaptype: Optional[EntityItemLdaptypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[EntityItemRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LdapItem(ItemType):
    """This element holds information about specific entries in the LDAP directory.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an item inside the specified suffix. It contains all of
        the parts of the item's distinguished name except those outlined
        by the suffix. If the xsi:nil attribute is set to true, then the
        item being represented is the higher level suffix.
    :ivar attribute: Specifies a named value contained by the object.
    :ivar object_class: The name of the class of which the object is an
        instance.
    :ivar ldaptype: Specifies the type of information that the specified
        attribute represents.
    :ivar value: The actual value of the specified LDAP attribute.
    """

    class Meta:
        name = "ldap_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    suffix: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    object_class: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ldaptype: Optional[EntityItemLdaptypeType] = field(
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
class ShellcommandItem(ItemType):
    """The shellcommand_item stores information retrieved from the local system
    that results from the running of the command or embedded script in the
    associated object command element.

    The evaluation of the object should always produce one item.  If the
    object evaluation does not produce output via STDOUT that should
    result in an item, one should be created with a status of 'does not
    exist'.  This facilitates that capture of the exit_status and stderr
    from the system call.

    :ivar shell: The shell element contains the shell used (e.g. bash or
        powershell) to perform the command and should be taken,
        verbatim, from the associated object 'shell' element.
    :ivar command: The command element specifies the command string that
        was run on the target system and should be taken, verbatim, from
        the associated object 'command' element..
    :ivar pattern: The pattern element is simply an echo of the same
        element in the OVAL object and is supplied in the item to aid in
        end user interpretation and should be taken, verbatim, from the
        associated object 'pattern' element..
    :ivar exit_status: The exit_status entity represents the exist
        status returned by the system for the execution of the object
        command. OVAL Item status should match the exit status of the
        system call.
    :ivar stdout_line: The stdout_line entity contains a line from the
        STDOUT output of a successful run of the command string that
        matched the specified object pattern.  Each line created by the
        execution of the object command should create an item
        'stdout_line' element.
    :ivar subexpression: The subexpression entity represents the value
        of a subexpression in the specified pattern.  If multiple
        subexpressions are specified in the pattern, then multiple
        entities are presented.  Note that the textfilecontent_state in
        the definition schema only allows a single subexpression entity.
        This means that the test will check that all (or at least one,
        none, etc.) the subexpressions pass the same check.  This means
        that the order of multiple subexpression entities in the item
        does not matter.
    :ivar stderr_line: The 'stderr_line' element contains a single line
        of any output from STDERR.
    """

    class Meta:
        name = "shellcommand_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    shell: Optional[EntityItemShellType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    command: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    pattern: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    exit_status: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    stdout_line: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    stderr_line: list[EntityItemStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Sql512Item(ItemType):
    """
    The sql512_item outlines information collected from a database via an SQL
    query.

    :ivar engine: The engine entity identifies the specific database
        engine used to connect to the database.
    :ivar version: The version entity identifies the version of the
        database engine used to connect to the database.
    :ivar instance: The instance entity defines the specific instance
        name to be used when connecting to the correct database.
    :ivar database: The database entity defines the specific database
        name to be used when connecting to the specified instance.
    :ivar sql: The sql entity holds the specific query used to identify
        the object(s) in the database.
    :ivar result: The result entity holds the results of the specified
        SQL statement.
    """

    class Meta:
        name = "sql512_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    engine: Optional[EntityItemEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    database: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: list[EntityItemRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Sql57Item(ItemType):
    """
    The sql57_item outlines information collected from a database via an SQL query.

    :ivar engine: The engine entity identifies the specific database
        engine used to connect to the database.
    :ivar version: The version entity identifies the version of the
        database engine used to connect to the database.
    :ivar connection_string: The connection_string entity defines
        connection parameters used to connect to the specific database.
    :ivar sql: The sql entity holds the specific query used to identify
        the object(s) in the database.
    :ivar result: The result entity holds the results of the specified
        SQL statement.
    """

    class Meta:
        name = "sql57_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    engine: Optional[EntityItemEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: list[EntityItemRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SqlItem(ItemType):
    """
    The sql_item outlines information collected from a database via an SQL query.

    :ivar engine: The engine entity identifies the specific database
        engine used to connect to the database.
    :ivar version: The version entity identifies the version of the
        database engine used to connect to the database.
    :ivar connection_string: The connection_string entity defines
        connection parameters used to connect to the specific database.
    :ivar sql: The sql entity holds the specific query used to identify
        the object(s) in the database.
    :ivar result: The result entity specifies the result(s) of the given
        SQL query against the database.
    """

    class Meta:
        name = "sql_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    engine: Optional[EntityItemEngineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class TextfilecontentItem(ItemType):
    """
    The textfilecontent_item looks at the contents of a text file (aka a
    configuration file) by looking at individual lines.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of the file
        (without the path) that is being represented.
    :ivar pattern: The pattern entity represents a regular expression
        that is used to define a block of text.  Subexpression notation
        (parenthesis) is used to call out a value(s) to test against.
        For example, the pattern abc(.*)xyz would look for a block of
        text in the file that starts with abc and ends with xyz, with
        the subexpression being all the characters that exist inbetween.
        Note that if the pattern can match more than one block of text
        starting at the same point, then it matches the longest.
        Subexpressions also match the longest possible substrings,
        subject to the constraint that the whole match be as long as
        possible, with subexpressions starting earlier in the pattern
        taking priority over ones starting later.
    :ivar instance: The instance entity calls out which match of the
        pattern is being represented by this item.  The first match is
        given an instance value of 1, the second match is given an
        instance value of 2, and so on.  The main purpose of this entity
        is too provide uniqueness for different textfilecontent_items
        that results from multiple matches of a given pattern against
        the same file.
    :ivar line: The line element represents a line in the file and is
        represented using a regular expression.
    :ivar text: The text entity represents the block of text that
        matched the specified pattern.
    :ivar subexpression: The subexpression entity represents the value
        of a subexpression in the specified pattern.  If multiple
        subexpressions are specified in the pattern, then multiple
        entities are presented.  Note that the textfilecontent_state in
        the definition schema only allows a single subexpression entity.
        This means that the test will check that all (or at least one,
        none, etc.) the subexpressions pass the same check.  This means
        that the order of multiple subexpression entities in the item
        does not matter.
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "textfilecontent_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

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
        },
    )
    pattern: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[EntityItemIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    line: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    text: Optional[EntityItemAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class VariableItem(ItemType):
    """
    This item stores information about OVAL Variables and their values.

    :ivar var_ref: The id of the variable.
    :ivar value: The value of the variable. If a variable represents and
        array of values, then multiple value elements should exist.
    """

    class Meta:
        name = "variable_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    var_ref: Optional[EntityItemVariableRefType] = field(
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
class XmlfilecontentItem(ItemType):
    """
    This item stores results from checking the contents of an xml file.

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
        node(s) or attribute(s) found. How this is used is entirely
        controlled by operator attributes.
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "xmlfilecontent_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

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
        },
    )
    xpath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value_of: list[EntityItemAnySimpleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class YamlfilecontentItem(ItemType):
    """
    This item stores results from checking the contents of an YAML file.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar content: The content element specifies the YAML document body.
    :ivar yamlpath: Specifies an YAML Path expression to evaluate
        against the YAML file specified by the filename entity.
    :ivar value: The value entity holds the target(s) of the specified
        YAML Path. A single scalar value or a list of scalar values
        (where there is no key to associate) would have the name
        attribute of the field element set to '#'. Due to the limitation
        of the record type field names could not contain uppercase
        letters, they will be converted to the lowercase and escaped
        using the '^' symbol (the '^' symbol would be escaped as well).
        For example 'myCamelCase^Key' would be collected as
        'my^camel^case^^^key'.
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "yamlfilecontent_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

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
        },
    )
    content: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    yamlpath: Optional[EntityItemStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: list[EntityItemRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
