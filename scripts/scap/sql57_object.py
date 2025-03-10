from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_engine_type import EntityObjectEngineType
from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Sql57Object(ObjectType2):
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
            
        },
    )
    version: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    connection_string: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    sql: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
