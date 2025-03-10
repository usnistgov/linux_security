from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class CheckEnumeration(Enum):
    """The CheckEnumeration simple type defines acceptable check values, which are
    used to determine the final result of something based on the results of
    individual components.

    When used to define the relationship between objects and states,
    each check value defines how many of the matching objects (items
    except those with a status of does not exist) must satisfy the given
    state for the test to return true. When used to define the
    relationship between instances of a given entity, the different
    check values defines how many instances must be true for the entity
    to return true. When used to define the relationship between
    entities and multiple variable values, each check value defines how
    many variable values must be true for the entity to return true.

    :cvar ALL: A value of 'all' means that a final result of true is
        given if all the individual results under consideration are
        true.
    :cvar AT_LEAST_ONE: A value of 'at least one' means that a final
        result of true is given if at least one of the individual
        results under consideration is true.
    :cvar NONE_EXIST: A value of 'none exists' means that a test
        evaluates to true if no matching object exists that satisfy the
        data requirements.
    :cvar NONE_SATISFY: A value of 'none satisfy' means that a final
        result of true is given if none the individual results under
        consideration are true.
    :cvar ONLY_ONE: A value of 'only one' means that a final result of
        true is given if one and only one of the individual results
        under consideration are true.
    """

    ALL = "all"
    AT_LEAST_ONE = "at least one"
    NONE_EXIST = "none exist"
    NONE_SATISFY = "none satisfy"
    ONLY_ONE = "only one"
