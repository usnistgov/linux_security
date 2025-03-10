from dataclasses import dataclass

from scap.object_type_2 import ObjectType2

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class ApparmorstatusObject(ObjectType2):
    """The apparmorstatus_object element is used by an apparmorstatus test to
    define the different information about the current AppArmor polciy.

    There is actually only one object relating to AppArmor Status and
    this is the system as a whole. Therefore, there are no child
    entities defined. Any OVAL Test written to check AppArmor status
    will reference the same apparmorstatus_object which is basically an
    empty object element.
    """

    class Meta:
        name = "apparmorstatus_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"
