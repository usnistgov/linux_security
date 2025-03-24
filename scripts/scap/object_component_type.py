from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ObjectComponentType:
    """The ObjectComponentType complex type defines a specific value or set of
    values on the local system to obtain.

    The required object_ref attribute provides a reference to an
    existing OVAL Object declaration. The referenced OVAL Object
    specifies a set of OVAL Items to collect. Note that an OVAL Object
    might identify 0, 1, or many OVAL Items on a system. If no items are
    found on the system then an error should be reported when
    determining the value of an ObjectComponentType. If 1 or more OVAL
    Items are found then each OVAL Item will be considered and the
    ObjectComponentType may have one or more values. The required
    item_field attribute specifies the name of the entity whose value
    will be retrieved from each OVAL Item collected by the referenced
    OVAL Object. For example, if the object_ref references a win-
    def:file_object, the item_field may specify the 'version' entity as
    the field to use as the value of the ObjectComponentType. Note that
    an OVAL Item may have 0, 1, or many entities whose name matches the
    specified item_field value. If an entity is not found with a name
    that matches the value of the item_field an error should be reported
    when determining the value of an ObjectComponentType. If 1 or more
    matching entities are found in a single OVAL Item the value of the
    ObjectComponentType is the list of the values from each of the
    matching entities. The optional record_field attribute specifies the
    name of a field in a record entity in an OVAL Item. The record_field
    attribute allows the value of a specific field to be retrieved from
    an entity with a datatype of 'record'. If a field with a matching
    name attribute value is not found in the referenced OVAL Item entity
    an error should be reported when determining the value of the
    ObjectComponentType.
    """

    def evaluate_component(self, data):
        print("Object Component Evaluation")
        return data["objects"][self.object_ref].evaluate_object(data)

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    item_field: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    record_field: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )
