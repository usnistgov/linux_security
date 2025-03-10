from dataclasses import dataclass

from scap.object_type_2 import ObjectType2

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class FamilyObject(ObjectType2):
    """The family_object element is used by a family test to define those objects
    to evaluate based on a specified state.

    There is actually only one object relating to family and this is the
    system as a whole. Therefore, there are no child entities defined.
    Any OVAL Test written to check the family will reference the same
    family_object which is basically an empty object element.
    """

    class Meta:
        name = "family_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )
