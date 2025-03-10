from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_ldaptype_type import EntityStateLdaptypeType
from scap.entity_state_record_type import EntityStateRecordType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Ldap57State(StateType):
    """The ldap57_state element defines the different information that can be used
    to evaluate the specified entries in an LDAP directory.

    An ldap57_test will reference a specific instance of this state that
    defines the exact settings that need to be evaluated. Please refer
    to the individual elements in the schema for more details about what
    each represents. Note that this state supports complex values that
    are in the form of a record. For simple (string based) value
    collection see the ldap_state.

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
    :ivar value: The actual value of the specified LDAP attribute. Note
        that while an LDAP attribute can contain structured data where
        it is necessary to collect multiple related fields that can be
        described by the 'record' datatype, it is not always the case.
        It also is possible that an LDAP attribute can contain only a
        single value or an array of values. In these cases, there is not
        a name to uniquely identify the corresponding field which is a
        requirement for fields in the 'record' datatype.  As a result,
        the name of the LDAP attribute will be used to uniquely identify
        the field and satisfy this requirement.
    """

    class Meta:
        name = "ldap57_state"
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
    value: Optional[EntityStateRecordType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
