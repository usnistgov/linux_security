from dataclasses import dataclass

from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class State(StateType):
    """The state element is an abstract element that is meant to be extended (via
    substitution groups) by the states found in the component schemas.

    An actual state element is not valid. The use of this abstract class
    simplifies the OVAL schema by allowing individual states to inherit
    the optional notes child element, and the id and operator attributes
    from the base StateType. Please refer to the description of the
    StateType complex type for more information. An OVAL State is a
    collection of one or more characteristics pertaining to a specific
    object type. The OVAL State is used by an OVAL Test to determine if
    a unique set of items identified on a system meet certain
    characteristics.
    """

    class Meta:
        name = "state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"
