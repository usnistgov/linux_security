from dataclasses import dataclass, field

from scap.filter_action_enumeration import FilterActionEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Filter:
    """The filter element provides a reference to an existing OVAL State and
    includes an optional action attribute.

    The action attribute is used to specify whether items that match the
    referenced OVAL State will be included in the resulting set or
    excluded from the resulting set.
    """

    class Meta:
        name = "filter"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:ste:[1-9][0-9]*",
        },
    )
    action: FilterActionEnumeration = field(
        default=FilterActionEnumeration.EXCLUDE,
        metadata={
            "type": "Attribute",
        },
    )
