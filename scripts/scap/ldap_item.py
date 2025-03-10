from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_ldaptype_type import EntityItemLdaptypeType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class LdapItem:
    """This element holds information about specific entries in the LDAP directory.

    It extends the standard ItemType as defined in the oval-system-
    characteristics schema and one should refer to the ItemType
    description for more information.

    :ivar suffix: Each object in an LDAP directory exists under a
        certain suffix (also known as a naming context). A suffix is
        defined as a single object in the Directory Information Tree
        (DIT) with every object in the tree subordinate to it.
    :ivar relative_dn: The relative_dn field is used to uniquely
        identify an item inside the specified suffix. It contains all of
        the parts of the item's distinguished name except those outlined
        by the suffix. If the xsi:nil attribute is set to true, then the
        item being represented is the higher level suffix.
    :ivar attribute: Specifies a named value contained by the object.
    :ivar object_class: The name of the class of which the object is an
        instance.
    :ivar ldaptype: Specifies the type of information that the specified
        attribute represents.
    :ivar value: The actual value of the specified LDAP attribute.
    """

    class Meta:
        name = "ldap_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    suffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    relative_dn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    attribute: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    object_class: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ldaptype: Optional[EntityItemLdaptypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
