from dataclasses import dataclass, field

from scap.filter import Filter
from scap.set_operator_enumeration import SetOperatorEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Set:
    """The set element enables complex objects to be described.

    It is a recursive element in that each set element can contain
    additional set elements as children. Each set element defines
    characteristics that produce a matching unique set of items. This
    set of items is defined by one or two references to OVAL Objects
    that provide the criteria needed to collect a set of system items.
    These items can have one or more filters applied to allow a subset
    of those items to be specifically included or excluded from the
    overall set of items. The set element's object_reference refers to
    an existing OVAL Object. The set element's filter element provides a
    reference to an existing OVAL State and includes an optional action
    attribute. The filter's action attribute allows the author to
    specify whether matching items should be included or excluded from
    the overall set. The default filter action is to exclude all
    matching items. In other words, the filter can be thought of
    filtering items out by default. Each filter is applied to the items
    identified by each OVAL Object before the set_operator is applied.
    For example, if an object_reference points to an OVAL Object that
    identifies every file in a certain directory, a filter might be set
    up to limit the object set to only those files with a size less than
    10 KB. If multiple filters are provided, then each filter is applied
    to the set of items identified by the OVAL Object. Care must be
    taken to ensure that conflicting filters are not applied. It is
    possible to exclude all items with a size of 10 KB and then include
    only items with a size of 10 KB. This example would result in the
    empty set. The required set_operator attribute defines how different
    child sets are combined to form the overall unique set of objects.
    For example, does one take the union of different sets or the
    intersection? For a description of the valid values please refer to
    the SetOperatorEnumeration simple type.
    """

    def evaluate_set(self,data):
        print(f"Set: {self}")
        checks = []
        #operator = self.set_operator.value
        for set in self.set:
            checks.append("[ $(" + set.evaluate_set(data) + ") ]")
        for obj in self.object_reference:
            checks.append("[ $(" + data["objects"][obj].evaluate_object(data) + ") ]")
        # Since all sets seem to not use the operators, we will default to UNION
        checks = " && ".join(checks)
        #if operator == SetOperatorEnumeration.UNION:
        #print(f"Evaluated statement: {checks}")
        return checks

    class Meta:
        name = "set"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    set: list["Set"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    object_reference: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
            "max_occurs": 2,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    set_operator: SetOperatorEnumeration = field(
        default=SetOperatorEnumeration.UNION,
        metadata={
            "type": "Attribute",
        },
    )
