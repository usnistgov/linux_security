from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_ldaptype_type import EntityStateLdaptypeType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class LdapState(StateType):
    """The ldap_state element defines the different information that can be used to
    evaluate the specified entries in an LDAP directory.

    An ldap_test will reference a specific instance of this state that
    defines the exact settings that need to be evaluated. Please refer
    to the individual elements in the schema for more details about what
    each represents.

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

    suffix: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    relative_dn: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    attribute: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    object_class: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ldaptype: Optional[EntityStateLdaptypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
