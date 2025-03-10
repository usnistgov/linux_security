from dataclasses import dataclass, field

from scap.entity_state_simple_base_type import EntityStateSimpleBaseType
from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateEvrstringType(EntityStateSimpleBaseType):
    """The EntityStateEVRStringType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This type
    represents the epoch, version, and release fields, for an RPM
    package, as a single version string. It has the form "EPOCH:VERSION-
    RELEASE". Note that a null epoch (or '(none)' as returned by rpm) is
    equivalent to '0' and would hence have the form 0:VERSION-RELEASE.
    Comparisons involving this datatype should follow the algorithm of
    librpm's rpmvercmp() function.
    """

    class Meta:
        name = "EntityStateEVRStringType"

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.EVR_STRING,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
