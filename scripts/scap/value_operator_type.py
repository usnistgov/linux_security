from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class ValueOperatorType(Enum):
    """This type enumerates allowed values of the @operator property of
    &lt;xccdf:Value&gt; elements.

    The specific interpretation of these operators depends on the
    checking system used.
    """

    EQUALS = "equals"
    NOT_EQUAL = "not equal"
    GREATER_THAN = "greater than"
    LESS_THAN = "less than"
    GREATER_THAN_OR_EQUAL = "greater than or equal"
    LESS_THAN_OR_EQUAL = "less than or equal"
    PATTERN_MATCH = "pattern match"
