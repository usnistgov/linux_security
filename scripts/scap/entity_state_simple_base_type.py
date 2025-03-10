from dataclasses import dataclass, field

from scap.check_enumeration import CheckEnumeration
from scap.entity_simple_base_type import EntitySimpleBaseType
from scap.existence_enumeration import ExistenceEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateSimpleBaseType(EntitySimpleBaseType):
    """The EntityStateSimpleBaseType complex type is an abstract type that extends
    the EntitySimpleBaseType and is used by some entities within an OVAL State.

    The optional check_existence attribute specifies how to interpret
    the status of corresponding item entities when performing an item-
    state comparison. The default value for this attribute is
    'at_least_one_exists' indicating that by default an item comparison
    may evaluate to true only if at least one corresponding item entity
    has a status of 'exists'. For example, if a value of 'none_exist' is
    given, then the comparison can evaluate to true only if there are
    one or more corresponding item entities, each with a status of 'does
    not exist'. The optional entity_check attribute specifies how to
    handle multiple item entities with the same name in the OVAL Systems
    Characteristics file. For example, suppose we are dealing with a
    Group Test and an entity in the state is related to the user.  It is
    very likely that when the information about the group is collected
    off of the system (and represented in the OVAL System
    Characteristics file) that there will be multiple users associated
    with the group (i.e. multiple 'user' item entities associated with
    the same 'user' state entity).  If the OVAL State defines the value
    of the user entity to equal 'Fred', then the entity_check attribute
    determines if all values for 'user' item entities must be equal to
    'Fred', or at least one value must be equal to 'Fred', etc.  Note
    that with the exception of the 'none_satisfy' check value, the
    entity_check attribute can only affect the result of the test if the
    corresponding OVAL Item allows more than one occurrence of the
    entity (e.g. 'maxOccurs' is some value greater than one). The
    entity_check and var_check attributes are considered together when
    evaluating a single state entity. When a variable identifies more
    than one value and multiple item entities with the same name exist,
    for a single state entity, a many-to-many comparison must be
    conducted.  In this situation, there are many values for the state
    entity that must be compared to many item entities.  Each item
    entity is compared to the state entity. For each item entity, an
    interim result is calculated by using the var_check attribute to
    combine the result of comparing each variable value with a single
    system value. Then these interim results are combined for each
    system value using the entity_check attribute.
    """

    entity_check: CheckEnumeration = field(
        default=CheckEnumeration.ALL,
        metadata={
            "type": "Attribute",
        },
    )
    check_existence: ExistenceEnumeration = field(
        default=ExistenceEnumeration.AT_LEAST_ONE_EXISTS,
        metadata={
            "type": "Attribute",
        },
    )
