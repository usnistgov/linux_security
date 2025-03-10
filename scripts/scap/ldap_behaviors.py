from dataclasses import dataclass, field

from scap.ldap_behaviors_scope import LdapBehaviorsScope

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
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
