from dataclasses import dataclass

from scap.object_type_2 import ObjectType2

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class UnameObject(ObjectType2):
    """The uname_object element is used by an uname test to define those objects to
    evaluated based on a specified state.

    There is actually only one object relating to uname and this is the
    system as a whole. Therefore, there are no child entities defined.
    Any OVAL Test written to check uname will reference the same
    uname_object which is basically an empty object element.
    """

    class Meta:
        name = "uname_object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"
