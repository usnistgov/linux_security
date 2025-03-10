from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemGconfTypeType(Enum):
    """The EntityItemGconfTypeType complex type restricts a string value to the
    seven values GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
    GCONF_VALUE_BOOL, GCONF_VALUE_SCHEMA, GCONF_VALUE_LIST, and GCONF_VALUE_PAIR
    that specify the type of the value associated with a GConf preference key.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar GCONF_VALUE_STRING: The GCONF_VALUE_STRING type is used to
        describe a preference key that has a string value.
    :cvar GCONF_VALUE_INT: The GCONF_VALUE_INT type is used to describe
        a preference key that has a integer value.
    :cvar GCONF_VALUE_FLOAT: The GCONF_VALUE_FLOAT type is used to
        describe a preference key that has a float value.
    :cvar GCONF_VALUE_BOOL: The GCONF_VALUE_BOOL type is used to
        describe a preference key that has a boolean value.
    :cvar GCONF_VALUE_SCHEMA: The GCONF_VALUE_SCHEMA type is used to
        describe a preference key that has a schema value. The actual
        value will be the default value as specified in the GConf
        schema.
    :cvar GCONF_VALUE_LIST: The GCONF_VALUE_LIST type is used to
        describe a preference key that has a list of values. The actual
        values will be one of the primitive GConf datatypes
        GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
        GCONF_VALUE_BOOL, and GCONF_VALUE_SCHEMA. Note that all of the
        values associated with a GCONF_VALUE_LIST are required to have
        the same type.
    :cvar GCONF_VALUE_PAIR: The GCONF_VALUE_PAIR type is used to
        describe a preference key that has a pair of values. The actual
        values will consist of the primitive GConf datatypes
        GCONF_VALUE_STRING, GCONF_VALUE_INT, GCONF_VALUE_FLOAT,
        GCONF_VALUE_BOOL, and GCONF_VALUE_SCHEMA. Note that the values
        associated with a GCONF_VALUE_PAIR are not required to have the
        same type.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    GCONF_VALUE_STRING = "GCONF_VALUE_STRING"
    GCONF_VALUE_INT = "GCONF_VALUE_INT"
    GCONF_VALUE_FLOAT = "GCONF_VALUE_FLOAT"
    GCONF_VALUE_BOOL = "GCONF_VALUE_BOOL"
    GCONF_VALUE_SCHEMA = "GCONF_VALUE_SCHEMA"
    GCONF_VALUE_LIST = "GCONF_VALUE_LIST"
    GCONF_VALUE_PAIR = "GCONF_VALUE_PAIR"
    VALUE = ""
