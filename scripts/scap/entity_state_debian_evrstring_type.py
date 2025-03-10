from dataclasses import dataclass, field

from scap.entity_state_simple_base_type import EntityStateSimpleBaseType
from scap.simple_datatype_enumeration import SimpleDatatypeEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateDebianEvrstringType(EntityStateSimpleBaseType):
    """The EntityStateDebianEVRStringType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the attributes found in the EntityStateSimpleBaseType. This type represents the epoch, upstream_version, and debian_revision fields, for a Debian package, as a single version string. It has the form "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Note that a null epoch (or '(none)' as returned by dpkg) is equivalent to '0' and would hence have the form 0:UPSTREAM_VERSION-DEBIAN_REVISION. Comparisons involving this datatype should follow the algorithm outlined in Chapter 5 of the "Debian Policy Manual" (https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version). An implementation of this is the cmpversions() function in dpkg's enquiry.c.
    """

    class Meta:
        name = "EntityStateDebianEVRStringType"

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.DEBIAN_EVR_STRING,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
