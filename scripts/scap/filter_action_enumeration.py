from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


class FilterActionEnumeration(Enum):
    """
    The FilterActionEnumeration simple type defines the different options for
    filtering sets of items.

    :cvar EXCLUDE: The exclude value specifies that all items that match
        the filter shall be excluded from set that the filter is applied
        to.
    :cvar INCLUDE: The include value specifies that only items that
        match the filter shall be included in the set that the filter is
        applied to.
    """

    EXCLUDE = "exclude"
    INCLUDE = "include"
