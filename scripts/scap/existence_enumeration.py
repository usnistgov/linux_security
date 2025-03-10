from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class ExistenceEnumeration(Enum):
    """The ExistenceEnumeration simple type defines acceptable existence values,
    which are used to determine a result based on the existence of individual
    components.

    The main use for this is for a test regarding the existence of
    objects on the system. Its secondary use is for a state regarding
    the existence of entities in corresponding items.

    :cvar ALL_EXIST: When used in the context of an OVAL state entity's
        check_existence attribute, a value of 'all_exist' means that
        every item entity for an object defined by the description
        exists on the system. When used in the context of an OVAL test's
        check_existence attribute, this value is equivalent to
        'at_least_one_exists' because non-existent items have no impact
        upon evaluation.
    :cvar ANY_EXIST: A value of 'any_exist' means that zero or more
        objects defined by the description exist on the system.
    :cvar AT_LEAST_ONE_EXISTS: A value of 'at_least_one_exists' means
        that at least one object defined by the description exists on
        the system.
    :cvar NONE_EXIST: A value of 'none_exist' means that none of the
        objects defined by the description exist on the system.
    :cvar ONLY_ONE_EXISTS: A value of 'only_one_exists' means that only
        one object defined by the description exists on the system.
    """

    ALL_EXIST = "all_exist"
    ANY_EXIST = "any_exist"
    AT_LEAST_ONE_EXISTS = "at_least_one_exists"
    NONE_EXIST = "none_exist"
    ONLY_ONE_EXISTS = "only_one_exists"
