from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_engine_type import EntityStateEngineType
from scap.entity_state_record_type import EntityStateRecordType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
            
        },
    )
    version: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    connection_string: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sql: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    result: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
