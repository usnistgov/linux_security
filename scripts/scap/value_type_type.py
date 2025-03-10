from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class ValueTypeType(Enum):
    """Allowed data types for &lt;xccdf:Value&gt; elements, string, numeric, and
    boolean.

    A tool may choose any convenient form to store an
    &lt;xccdf:Value&gt; element’s &lt;xccdf:value&gt; element, but the
    @type conveys how the value should be treated for user input
    validation purposes during tailoring processing. The @type may also
    be used to give additional guidance to the user or to validate the
    user’s input. For example, if an &lt;xccdf:value&gt; element’s @type
    attribute is “number”, then a tool might choose to reject user
    tailoring input that is not composed of digits. In the case of a
    list of values, the @type applies to all elements of the list
    individually. Note that checking systems may have their own
    understanding of data types that may not be identical to the typing
    indicated in XCCDF

    :cvar NUMBER: A numeric value. This may be decimal or integer.
    :cvar STRING: Any character data
    :cvar BOOLEAN: True/false
    """

    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
