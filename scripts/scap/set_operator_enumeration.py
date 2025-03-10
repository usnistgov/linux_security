from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


class SetOperatorEnumeration(Enum):
    """The SetOperatorEnumeration simple type defines acceptable set operations.

    Set operations are used to take multiple different sets of objects
    within OVAL and merge them into a single unique set. The different
    operators that guide this merge are defined below. For each
    operator, if only a single object has been supplied, then the
    resulting set is simply that complete object.

    :cvar COMPLEMENT: The complement operator is defined in OVAL as a
        relative complement. The resulting unique set contains
        everything that belongs to the first declared set that is not
        part of the second declared set. If A and B are sets (with A
        being the first declared set), then the relative complement is
        the set of elements in A, but not in B, with the duplicates
        removed.
    :cvar INTERSECTION: The intersection of two sets in OVAL results in
        a unique set that contains everything that belongs to both sets
        in the collection, but nothing else. If A and B are sets, then
        the intersection of A and B contains all the elements of A that
        also belong to B, but no other elements, with the duplicates
        removed.
    :cvar UNION: The union of two sets in OVAL results in a unique set
        that contains everything that belongs to either of the original
        sets. If A and B are sets, then the union of A and B contains
        all the elements of A and all elements of B, with the duplicates
        removed.
    """

    COMPLEMENT = "COMPLEMENT"
    INTERSECTION = "INTERSECTION"
    UNION = "UNION"
