from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_engine_type import EntityItemEngineType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class SqlItem:
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
            
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    connection_string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sql: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    result: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
