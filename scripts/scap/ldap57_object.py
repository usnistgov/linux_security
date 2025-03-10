from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.ldap_behaviors import LdapBehaviors
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Ldap57Object(ObjectType2):
    """The ldap57_object element is used by an LDAP test to define the objects to
    be evaluated based on a specified state.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema. Note that this object supports complex values
    that are in the form of a record. For simple (string based) value
    collection see the ldap_object.

    :ivar set:
    :ivar behaviors:
    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an object inside the specified suffix. It contains all
        of the parts of the object's distinguished name except those
        outlined by the suffix. If the xsi:nil attribute is set to true,
        then the object being specified is the higher level suffix. In
        this case, the relative_dn element should not be collected or
        used in analysis. Setting xsi:nil equal to true is different
        than using a .* pattern match, which says to collect every
        relative distinguished name under a given suffix.
    :ivar attribute: Specifies a named value contained by the object. If
        the xsi:nil attribute is set to true, the attribute element
        should not be collected or used in analysis. Setting xsi:nil
        equal to true is different than using a .* pattern match, which
        says to collect every attribute under a given relative
        distinguished name.
    :ivar filter:
    """

    class Meta:
        name = "ldap57_object"
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
    behaviors: Optional[LdapBehaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    suffix: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    relative_dn: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    attribute: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
