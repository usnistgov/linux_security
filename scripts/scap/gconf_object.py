from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class GconfObject(ObjectType2):
    """The gconf_object element is used by a gconf_test to define the preference
    keys to collect and the sources from which to collect the preference keys.

    Each object extends the standard ObjectType as defined in the oval-
    definitions-schema and one should refer to the ObjectType
    description for more information. The common set element allows
    complex objects to be created using filters and set logic. Again,
    please refer to the description of the set element in the oval-
    definitions-schema.

    :ivar set:
    :ivar key: This is the preference key to check.
    :ivar source: The source element specifies the source from which to
        collect the preference key. The source is represented by the
        absolute path to a GConf XML file as XML is the current backend
        for GConf.  Note that other backends may become available in the
        future. If the xsi:nil attribute is set to 'true', the
        preference key is looked up using the GConf daemon. Otherwise,
        the preference key is looked up using the values specified in
        this entity.
    :ivar filter:
    """

    class Meta:
        name = "gconf_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    key: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    source: Optional[EntityObjectStringType] = field(
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
