from dataclasses import dataclass

from scap.object_type_2 import ObjectType2

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ObjectAbstract(ObjectType2):
    """The object element is an abstract element that is meant to be extended (via
    substitution groups) by the objects found in the component schemas.

    An actual object element is not valid. The use of this abstract
    element simplifies the OVAL schema by allowing individual objects to
    inherit any common elements and attributes from the base ObjectType.
    Please refer to the description of the ObjectType complex type for
    more information. An object is used to identify a set of items to
    collect.  The author of a schema object must define sufficient
    object entities to allow a user to identify a unique item to be
    collected. A simple object typically results in a single file,
    process, etc being identified.  But through the use of pattern
    matches, sets, and variables, multiple matching items can be
    identified.  The set of items matching the object can then be used
    by an OVAL test and compared against an OVAL state.
    """

    class Meta:
        name = "object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"
