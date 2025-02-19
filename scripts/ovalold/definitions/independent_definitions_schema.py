from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


class EntityObjectEngineType(Enum):
    """The EntityObjectEngineType complex type defines a string entity value that
    is restricted to a set of enumerations.

    Each valid enumeration is a valid database engine. The empty string
    is also allowed to support empty elements associated with variable
    references.

    :cvar ACCESS: The access value describes the Microsoft Access
        database engine.
    :cvar DB2: The db2 value describes the IBM DB2 database engine.
    :cvar CACHE: The cache value describes the InterSystems Cache
        database engine.
    :cvar FIREBIRD: The firebird value describes the Firebird database
        engine.
    :cvar FIRSTSQL: The firstsql value describes the FirstSQL database
        engine.
    :cvar FOXPRO: The foxpro value describes the Microsoft FoxPro
        database engine.
    :cvar INFORMIX: The informix value describes the IBM Informix
        database engine.
    :cvar INGRES: The ingres value describes the Ingres database engine.
    :cvar INTERBASE: The interbase value describes the Embarcadero
        Technologies InterBase database engine.
    :cvar LIGHTBASE: The lightbase value describes the Light Infocon
        LightBase database engine.
    :cvar MAXDB: The maxdb value describes the SAP MaxDB database
        engine.
    :cvar MONETDB: The monetdb value describes the MonetDB SQL database
        engine.
    :cvar MIMER: The mimer value describes the Mimer SQL database
        engine.
    :cvar MYSQL: The mysql value describes the MySQL database engine.
    :cvar ORACLE: The oracle value describes the Oracle database engine.
    :cvar PARADOX: The paradox value describes the Paradox database
        engine.
    :cvar PERVASIVE: The pervasive value describes the Pervasive PSQL
        database engine.
    :cvar POSTGRE: The postgre value describes the PostgreSQL database
        engine.
    :cvar SQLBASE: The sqlbase value describes the Unify SQLBase
        database engine.
    :cvar SQLITE: The sqlite value describes the SQLite database engine.
    :cvar SQLSERVER: The sqlserver value describes the Microsoft SQL
        database engine.
    :cvar SYBASE: The sybase value describes the Sybase database engine.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    ACCESS = "access"
    DB2 = "db2"
    CACHE = "cache"
    FIREBIRD = "firebird"
    FIRSTSQL = "firstsql"
    FOXPRO = "foxpro"
    INFORMIX = "informix"
    INGRES = "ingres"
    INTERBASE = "interbase"
    LIGHTBASE = "lightbase"
    MAXDB = "maxdb"
    MONETDB = "monetdb"
    MIMER = "mimer"
    MYSQL = "mysql"
    ORACLE = "oracle"
    PARADOX = "paradox"
    PERVASIVE = "pervasive"
    POSTGRE = "postgre"
    SQLBASE = "sqlbase"
    SQLITE = "sqlite"
    SQLSERVER = "sqlserver"
    SYBASE = "sybase"
    VALUE = ""


class EntityObjectHashTypeType(Enum):
    """The EntityObjectHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.

    :cvar MD5: The MD5 hash algorithm.
    :cvar SHA_1: The SHA-1 hash algorithm.
    :cvar SHA_224: The SHA-224 hash algorithm.
    :cvar SHA_256: The SHA-256 hash algorithm.
    :cvar SHA_384: The SHA-384 hash algorithm.
    :cvar SHA_512: The SHA-512 hash algorithm.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_224 = "SHA-224"
    SHA_256 = "SHA-256"
    SHA_384 = "SHA-384"
    SHA_512 = "SHA-512"
    VALUE = ""


@dataclass
class EntityObjectVariableRefType:
    """The EntityObjectVariableRefType complex type defines a string object entity
    that has a valid OVAL variable id as the value.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


class EntityStateEngineType(Enum):
    """The EntityStateEngineType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a valid database engine. The empty string
    is also allowed to support empty elements associated with variable
    references.

    :cvar ACCESS: The access value describes the Microsoft Access
        database engine.
    :cvar DB2: The db2 value describes the IBM DB2 database engine.
    :cvar CACHE: The cache value describes the InterSystems Cache
        database engine.
    :cvar FIREBIRD: The firebird value describes the Firebird database
        engine.
    :cvar FIRSTSQL: The firstsql value describes the FirstSQL database
        engine.
    :cvar FOXPRO: The foxpro value describes the Microsoft FoxPro
        database engine.
    :cvar INFORMIX: The informix value describes the IBM Informix
        database engine.
    :cvar INGRES: The ingres value describes the Ingres database engine.
    :cvar INTERBASE: The interbase value describes the Embarcadero
        Technologies InterBase database engine.
    :cvar LIGHTBASE: The lightbase value describes the Light Infocon
        LightBase database engine.
    :cvar MAXDB: The maxdb value describes the SAP MaxDB database
        engine.
    :cvar MONETDB: The monetdb value describes the MonetDB SQL database
        engine.
    :cvar MIMER: The mimer value describes the Mimer SQL database
        engine.
    :cvar MYSQL: The mysql value describes the MySQL database engine.
    :cvar ORACLE: The oracle value describes the Oracle database engine.
    :cvar PARADOX: The paradox value describes the Paradox database
        engine.
    :cvar PERVASIVE: The pervasive value describes the Pervasive PSQL
        database engine.
    :cvar POSTGRE: The postgre value describes the PostgreSQL database
        engine.
    :cvar SQLBASE: The sqlbase value describes the Unify SQLBase
        database engine.
    :cvar SQLITE: The sqlite value describes the SQLite database engine.
    :cvar SQLSERVER: The sqlserver value describes the Microsoft SQL
        database engine.
    :cvar SYBASE: The sybase value describes the Sybase database engine.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    ACCESS = "access"
    DB2 = "db2"
    CACHE = "cache"
    FIREBIRD = "firebird"
    FIRSTSQL = "firstsql"
    FOXPRO = "foxpro"
    INFORMIX = "informix"
    INGRES = "ingres"
    INTERBASE = "interbase"
    LIGHTBASE = "lightbase"
    MAXDB = "maxdb"
    MONETDB = "monetdb"
    MIMER = "mimer"
    MYSQL = "mysql"
    ORACLE = "oracle"
    PARADOX = "paradox"
    PERVASIVE = "pervasive"
    POSTGRE = "postgre"
    SQLBASE = "sqlbase"
    SQLITE = "sqlite"
    SQLSERVER = "sqlserver"
    SYBASE = "sybase"
    VALUE = ""


class EntityStateFamilyType(Enum):
    """The EntityStateFamilyType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a high-level family of system operating
    system. The empty string is also allowed to support empty elements
    associated with variable references.

    :cvar CATOS: The catos value describes the Cisco CatOS operating
        system.
    :cvar IOS: The ios value describes the Cisco IOS operating system.
    :cvar MACOS: The macos value describes the Mac operating system.
    :cvar PIXOS: The pixos value describes the Cisco PIX operating
        system.
    :cvar UNDEFINED: The undefined value is to be used when the desired
        family is not available.
    :cvar UNIX: The unix value describes the UNIX operating system.
    :cvar VMWARE_INFRASTRUCTURE: The vmware_infrastructure value
        describes VMWare Infrastructure.
    :cvar WINDOWS: The windows value describes the Microsoft Windows
        operating system.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    CATOS = "catos"
    IOS = "ios"
    MACOS = "macos"
    PIXOS = "pixos"
    UNDEFINED = "undefined"
    UNIX = "unix"
    VMWARE_INFRASTRUCTURE = "vmware_infrastructure"
    WINDOWS = "windows"
    VALUE = ""


class EntityStateHashTypeType(Enum):
    """The EntityStateHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.

    :cvar MD5: The MD5 hash algorithm.
    :cvar SHA_1: The SHA-1 hash algorithm.
    :cvar SHA_224: The SHA-224 hash algorithm.
    :cvar SHA_256: The SHA-256 hash algorithm.
    :cvar SHA_384: The SHA-384 hash algorithm.
    :cvar SHA_512: The SHA-512 hash algorithm.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_224 = "SHA-224"
    SHA_256 = "SHA-256"
    SHA_384 = "SHA-384"
    SHA_512 = "SHA-512"
    VALUE = ""


class EntityStateLdaptypeType(Enum):
    """The EntityStateLdaptypeType complex type restricts a string value to a
    specific set of values that specify the different types of information that an
    ldap attribute can represent.

    The empty string is also allowed to support empty elements
    associated with variable references.

    :cvar LDAPTYPE_ACI_ITEM: ACI Item, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.1
    :cvar LDAPTYPE_ACCESS_POINT: Access Point, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.2
    :cvar LDAPTYPE_ATTRIBUTE_TYPE_DESCRIP_STRING: Attribute Type
        Description, corresponding to OID 1.3.6.1.4.1.1466.115.121.1.3
    :cvar LDAPTYPE_AUDIO: Audio, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.4
    :cvar LDAPTYPE_BINARY: Binary, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.5
    :cvar LDAPTYPE_BIT_STRING: Bit String, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.6
    :cvar LDAPTYPE_BOOLEAN: Boolean, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.7
    :cvar LDAPTYPE_CERTIFICATE: Certificate, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.8
    :cvar LDAPTYPE_CERTIFICATE_LIST: Certificate List, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.9
    :cvar LDAPTYPE_CERTIFICATE_PAIR: Certificate Pair, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.10
    :cvar LDAPTYPE_COUNTRY_STRING: Country String, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.11
    :cvar LDAPTYPE_DN_STRING: DN, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.12
    :cvar LDAPTYPE_DATA_QUALITY_SYNTAX: Data Quality Syntax,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.13
    :cvar LDAPTYPE_DELIVERY_METHOD: Delivery Method, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.14
    :cvar LDAPTYPE_DIRECTORY_STRING: Directory String, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.15
    :cvar LDAPTYPE_DIR_CONTENT_RULE_DESCRIPTION: DIT Content Rule
        Description, corresponding to OID 1.3.6.1.4.1.1466.115.121.1.16
    :cvar LDAPTYPE_DIT_STRUCTURE_RULE_DESCRIPTION: DIT Structure Rule
        Description, corresponding to OID 1.3.6.1.4.1.1466.115.121.1.17
    :cvar LDAPTYPE_DL_SUBMIT_PERMISSION: DL Submit Permission,
        corresponding to OID Y  1.3.6.1.4.1.1466.115.121.1.18
    :cvar LDAPTYPE_DSA_QUALITY_SYNTAX: DSA Quality Syntax, corresponding
        to OID 1.3.6.1.4.1.1466.115.121.1.19
    :cvar LDAPTYPE_DSE_TYPE: DSE Type, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.20
    :cvar LDAPTYPE_ENHANCED_GUIDE: Enhanced Guide, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.21
    :cvar LDAPTYPE_FAX_TEL_NUMBER: Facsimile Telephone Number,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.22
    :cvar LDAPTYPE_FAX: Fax, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.23
    :cvar LDAPTYPE_GENERALIZED_TIME: Generalized Time, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.24
    :cvar LDAPTYPE_GUIDE: Guide, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.25
    :cvar LDAPTYPE_IA5_STRING: IA5 String, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.26
    :cvar LDAPTYPE_INTEGER: INTEGER, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.27
    :cvar LDAPTYPE_JPEG: JPEG, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.28
    :cvar LDAPTYPE_LDAP_SYNTAX_DESCRIPTION: LDAP Syntax Description,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.54
    :cvar LDAPTYPE_LDAP_SCHEMA_DEFINITION: LDAP Schema Definition,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.56
    :cvar LDAPTYPE_LDAP_SCHEMA_DESCRIPTION: LDAP Schema Description,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.57
    :cvar LDAPTYPE_MASTER_AND_SHADOW_ACCESS_POINTS: Master And Shadow
        Access Points, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.29
    :cvar LDAPTYPE_MATCHING_RULE_DESCRIPTION: Matching Rule Description,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.30
    :cvar LDAPTYPE_MATCHING_RULE_USE_DESCRIPTION: Matching Rule Use
        Description, corresponding to OID 1.3.6.1.4.1.1466.115.121.1.31
    :cvar LDAPTYPE_MAIL_PREFERENCE: Mail Preference, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.32
    :cvar LDAPTYPE_MHS_OR_ADDRESS: MHS OR Address, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.33
    :cvar LDAPTYPE_MODIFY_RIGHTS: Modify Rights, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.55
    :cvar LDAPTYPE_NAME_AND_OPTIONAL_UID: Name And Optional UID,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.34
    :cvar LDAPTYPE_NAME_FORM_DESCRIPTION: Name Form Description,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.35
    :cvar LDAPTYPE_NUMERIC_STRING: Numeric String, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.36
    :cvar LDAPTYPE_OBJECT_CLASS_DESCRIP_STRING: Object Class
        Description, corresponding to OID 1.3.6.1.4.1.1466.115.121.1.37
    :cvar LDAPTYPE_OCTET_STRING: Octet String, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.40
    :cvar LDAPTYPE_OID: OID, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.38
    :cvar LDAPTYPE_MAILBOX: Other Mailbox, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.39
    :cvar LDAPTYPE_POSTAL_ADDRESS: Postal Address, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.41
    :cvar LDAPTYPE_PROTOCOL_INFORMATION: Protocol Information,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.42
    :cvar LDAPTYPE_PRESENTATION_ADDRESS: Presentation Address,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.43
    :cvar LDAPTYPE_PRINTABLE_STRING: Printable String, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.44
    :cvar LDAPTYPE_SUBSTRING_ASSERTION: Substring Assertion,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.58
    :cvar LDAPTYPE_SUBTREE_SPECIFICATION: Subtree Specification,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.45
    :cvar LDAPTYPE_SUPPLIER_INFORMATION: Supplier Information,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.46
    :cvar LDAPTYPE_SUPPLIER_OR_CONSUMER: Supplier Or Consumer,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.47
    :cvar LDAPTYPE_SUPPLIER_AND_CONSUMER: Supplier And Consumer,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.48
    :cvar LDAPTYPE_SUPPORTED_ALGORITHM: Supported Algorithm,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.49
    :cvar LDAPTYPE_TELEPHONE_NUMBER: Telephone Number, corresponding to
        OID 1.3.6.1.4.1.1466.115.121.1.50
    :cvar LDAPTYPE_TELEX_TERMINAL_ID: Teletex Terminal Identifier,
        corresponding to OID 1.3.6.1.4.1.1466.115.121.1.51
    :cvar LDAPTYPE_TELEX_NUMBER: Telex Number, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.52
    :cvar LDAPTYPE_UTC_TIME: UTC Time, corresponding to OID
        1.3.6.1.4.1.1466.115.121.1.53
    :cvar LDAPTYPE_TIMESTAMP: The data is of a time stamp in seconds.
    :cvar LDAPTYPE_EMAIL: The data is of an e-mail message.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    LDAPTYPE_ACI_ITEM = "LDAPTYPE_ACI_ITEM"
    LDAPTYPE_ACCESS_POINT = "LDAPTYPE_ACCESS_POINT"
    LDAPTYPE_ATTRIBUTE_TYPE_DESCRIP_STRING = (
        "LDAPTYPE_ATTRIBUTE_TYPE_DESCRIP_STRING"
    )
    LDAPTYPE_AUDIO = "LDAPTYPE_AUDIO"
    LDAPTYPE_BINARY = "LDAPTYPE_BINARY"
    LDAPTYPE_BIT_STRING = "LDAPTYPE_BIT_STRING"
    LDAPTYPE_BOOLEAN = "LDAPTYPE_BOOLEAN"
    LDAPTYPE_CERTIFICATE = "LDAPTYPE_CERTIFICATE"
    LDAPTYPE_CERTIFICATE_LIST = "LDAPTYPE_CERTIFICATE_LIST"
    LDAPTYPE_CERTIFICATE_PAIR = "LDAPTYPE_CERTIFICATE_PAIR"
    LDAPTYPE_COUNTRY_STRING = "LDAPTYPE_COUNTRY_STRING"
    LDAPTYPE_DN_STRING = "LDAPTYPE_DN_STRING"
    LDAPTYPE_DATA_QUALITY_SYNTAX = "LDAPTYPE_DATA_QUALITY_SYNTAX"
    LDAPTYPE_DELIVERY_METHOD = "LDAPTYPE_DELIVERY_METHOD"
    LDAPTYPE_DIRECTORY_STRING = "LDAPTYPE_DIRECTORY_STRING"
    LDAPTYPE_DIR_CONTENT_RULE_DESCRIPTION = (
        "LDAPTYPE_DIR_CONTENT_RULE_DESCRIPTION"
    )
    LDAPTYPE_DIT_STRUCTURE_RULE_DESCRIPTION = (
        "LDAPTYPE_DIT_STRUCTURE_RULE_DESCRIPTION"
    )
    LDAPTYPE_DL_SUBMIT_PERMISSION = "LDAPTYPE_DL_SUBMIT_PERMISSION"
    LDAPTYPE_DSA_QUALITY_SYNTAX = "LDAPTYPE_DSA_QUALITY_SYNTAX"
    LDAPTYPE_DSE_TYPE = "LDAPTYPE_DSE_TYPE"
    LDAPTYPE_ENHANCED_GUIDE = "LDAPTYPE_ENHANCED_GUIDE"
    LDAPTYPE_FAX_TEL_NUMBER = "LDAPTYPE_FAX_TEL_NUMBER"
    LDAPTYPE_FAX = "LDAPTYPE_FAX"
    LDAPTYPE_GENERALIZED_TIME = "LDAPTYPE_GENERALIZED_TIME"
    LDAPTYPE_GUIDE = "LDAPTYPE_GUIDE"
    LDAPTYPE_IA5_STRING = "LDAPTYPE_IA5_STRING"
    LDAPTYPE_INTEGER = "LDAPTYPE_INTEGER"
    LDAPTYPE_JPEG = "LDAPTYPE_JPEG"
    LDAPTYPE_LDAP_SYNTAX_DESCRIPTION = "LDAPTYPE_LDAP_SYNTAX_DESCRIPTION"
    LDAPTYPE_LDAP_SCHEMA_DEFINITION = "LDAPTYPE_LDAP_SCHEMA_DEFINITION"
    LDAPTYPE_LDAP_SCHEMA_DESCRIPTION = "LDAPTYPE_LDAP_SCHEMA_DESCRIPTION"
    LDAPTYPE_MASTER_AND_SHADOW_ACCESS_POINTS = (
        "LDAPTYPE_MASTER_AND_SHADOW_ACCESS_POINTS"
    )
    LDAPTYPE_MATCHING_RULE_DESCRIPTION = "LDAPTYPE_MATCHING_RULE_DESCRIPTION"
    LDAPTYPE_MATCHING_RULE_USE_DESCRIPTION = (
        "LDAPTYPE_MATCHING_RULE_USE_DESCRIPTION"
    )
    LDAPTYPE_MAIL_PREFERENCE = "LDAPTYPE_MAIL_PREFERENCE"
    LDAPTYPE_MHS_OR_ADDRESS = "LDAPTYPE_MHS_OR_ADDRESS"
    LDAPTYPE_MODIFY_RIGHTS = "LDAPTYPE_MODIFY_RIGHTS"
    LDAPTYPE_NAME_AND_OPTIONAL_UID = "LDAPTYPE_NAME_AND_OPTIONAL_UID"
    LDAPTYPE_NAME_FORM_DESCRIPTION = "LDAPTYPE_NAME_FORM_DESCRIPTION"
    LDAPTYPE_NUMERIC_STRING = "LDAPTYPE_NUMERIC_STRING"
    LDAPTYPE_OBJECT_CLASS_DESCRIP_STRING = (
        "LDAPTYPE_OBJECT_CLASS_DESCRIP_STRING"
    )
    LDAPTYPE_OCTET_STRING = "LDAPTYPE_OCTET_STRING"
    LDAPTYPE_OID = "LDAPTYPE_OID"
    LDAPTYPE_MAILBOX = "LDAPTYPE_MAILBOX"
    LDAPTYPE_POSTAL_ADDRESS = "LDAPTYPE_POSTAL_ADDRESS"
    LDAPTYPE_PROTOCOL_INFORMATION = "LDAPTYPE_PROTOCOL_INFORMATION"
    LDAPTYPE_PRESENTATION_ADDRESS = "LDAPTYPE_PRESENTATION_ADDRESS"
    LDAPTYPE_PRINTABLE_STRING = "LDAPTYPE_PRINTABLE_STRING"
    LDAPTYPE_SUBSTRING_ASSERTION = "LDAPTYPE_SUBSTRING_ASSERTION"
    LDAPTYPE_SUBTREE_SPECIFICATION = "LDAPTYPE_SUBTREE_SPECIFICATION"
    LDAPTYPE_SUPPLIER_INFORMATION = "LDAPTYPE_SUPPLIER_INFORMATION"
    LDAPTYPE_SUPPLIER_OR_CONSUMER = "LDAPTYPE_SUPPLIER_OR_CONSUMER"
    LDAPTYPE_SUPPLIER_AND_CONSUMER = "LDAPTYPE_SUPPLIER_AND_CONSUMER"
    LDAPTYPE_SUPPORTED_ALGORITHM = "LDAPTYPE_SUPPORTED_ALGORITHM"
    LDAPTYPE_TELEPHONE_NUMBER = "LDAPTYPE_TELEPHONE_NUMBER"
    LDAPTYPE_TELEX_TERMINAL_ID = "LDAPTYPE_TELEX_TERMINAL_ID"
    LDAPTYPE_TELEX_NUMBER = "LDAPTYPE_TELEX_NUMBER"
    LDAPTYPE_UTC_TIME = "LDAPTYPE_UTC_TIME"
    LDAPTYPE_TIMESTAMP = "LDAPTYPE_TIMESTAMP"
    LDAPTYPE_EMAIL = "LDAPTYPE_EMAIL"
    VALUE = ""


@dataclass
class EntityStateVariableRefType:
    """The EntityStateVariableRefType complex type defines a string state entity
    that has a valid OVAL variable id as the value.

    The empty string is also allowed to support empty elements
    associated with variable references.
    """


class EntityStateWindowsViewType(Enum):
    """The EntityStateWindowsViewType restricts a string value to a specific set of values: 32-bit and 64-bit. These values describe the different values possible for the windows view behavior.

    :cvar VALUE_32_BIT: Indicates the 32_bit windows view.
    :cvar VALUE_64_BIT: Indicates the 64_bit windows view.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"
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


class FileBehaviorsWindowsView(Enum):
    VALUE_32_BIT = "32_bit"
    VALUE_64_BIT = "64_bit"


class LdapBehaviorsScope(Enum):
    BASE = "BASE"
    ONE = "ONE"
    SUBTREE = "SUBTREE"


@dataclass
class Environmentvariable58Object:
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
        true, the process ID shall be the tool's running process.
    :ivar name: This element describes the name of an environment
        variable.
    :ivar filter:
    """

    class Meta:
        name = "environmentvariable58_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class Environmentvariable58State:
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

    pid: Optional[str] = field(
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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Environmentvariable58Test:
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
class EnvironmentvariableObject:
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

    set: Optional[str] = field(
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


@dataclass
class EnvironmentvariableState:
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

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnvironmentvariableTest:
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
class FamilyObject:
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
class FamilyTest:
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
class Filehash58Test:
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
class FilehashTest:
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
class Ldap57Test:
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
class LdapTest:
    """The LDAP test is used to check information about specific entries in an LDAP
    directory.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references an ldap_object
    and the optional state element, ldap_state, specifies the metadata
    to check. Note that this test supports only simple (string based)
    value collection. For more complex values see the ldap57_test.
    """

    class Meta:
        name = "ldap_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

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
class Sql57Test:
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
class SqlTest:
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
class Textfilecontent54Test:
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
class TextfilecontentTest:
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
class UnknownTest:
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
class VariableTest:
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
class XmlfilecontentTest:
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
class FamilyState:
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
class Filehash58State:
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
        },
    )
    hash_type: Optional[EntityStateHashTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    hash: Optional[str] = field(
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
class FilehashState:
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
        },
    )
    md5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sha1: Optional[str] = field(
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
class Ldap57State:
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

    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    object_class: Optional[str] = field(
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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LdapState:
    """The ldap_state element defines the different information that can be used to
    evaluate the specified entries in an LDAP directory.

    An ldap_test will reference a specific instance of this state that
    defines the exact settings that need to be evaluated. Please refer
    to the individual elements in the schema for more details about what
    each represents. Note that this state supports only simple (string
    based) value collection. For more complex values see the
    ldap57_state.

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

    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    attribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    object_class: Optional[str] = field(
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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Sql57Object:
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

    set: Optional[str] = field(
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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class Sql57State:
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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SqlObject:
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

    set: Optional[str] = field(
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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SqlState:
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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sql: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Textfilecontent54State:
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
        the pattern.
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
        },
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: Optional[str] = field(
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
class TextfilecontentState:
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
        },
    )
    line: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    subexpression: Optional[str] = field(
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
class VariableObject:
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

    set: Optional[str] = field(
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
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class VariableState:
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
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class XmlfilecontentState:
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
        },
    )
    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    value_of: Optional[str] = field(
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
class Filehash58Object:
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

    set: Optional[str] = field(
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
        },
    )
    hash_type: Optional[EntityObjectHashTypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class FilehashObject:
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

    set: Optional[str] = field(
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
        },
    )


@dataclass
class Ldap57Object:
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

    set: Optional[str] = field(
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
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class LdapObject:
    """The ldap_object element is used by an LDAP test to define the objects to be
    evaluated based on a specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. Note that this object is paired with a state
    that supports only simple (string based) value collection. For more
    complex values see the ldap57_object.

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

    set: Optional[str] = field(
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
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    relative_dn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    attribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )


@dataclass
class TextfilecontentObject:
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

    set: Optional[str] = field(
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
        },
    )
    line: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class XmlfilecontentObject:
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

    set: Optional[str] = field(
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
        },
    )
    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class Textfilecontent54Object:
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
        the pattern.  The first match is given an instance value of 1,
        the second match is given an instance value of 2, and so on.
        Note that the main purpose of this entity is to provide
        uniqueness for different textfilecontent_items that results from
        multiple matches of a given pattern against the same file. Most
        likely this entity will be defined as greater than or equal to 1
        which would result in the object representing the set of all
        matches of the pattern.
    :ivar filter:
    """

    class Meta:
        name = "textfilecontent54_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[str] = field(
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
        },
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    instance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    filter: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
