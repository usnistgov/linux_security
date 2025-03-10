from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


class EntityItemEngineType(Enum):
    """The EntityItemEngineType complex type defines a string entity value that is
    restricted to an enumeration.

    Each valid entry in the enumeration is a valid database engine.

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
        detailed error reporting.
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
