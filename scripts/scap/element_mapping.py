from dataclasses import dataclass

from scap.element_map_type import ElementMapType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class ElementMapping(ElementMapType):
    """The element_mapping element is used in documenting which tests, objects,
    states, and system characteristic items are associated with each other.

    It provides a way to explicitly and programatically associate the
    test, object, state, and item definitions.
    """

    class Meta:
        name = "element_mapping"
        namespace = "http://oval.mitre.org/XMLSchema/oval-common-5"
