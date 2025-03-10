from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class SubUseEnumType(Enum):
    """This holds the possible values of the @use attribute within an
    &lt;xccdf:sub&gt; element.

    The @use attribute is only applicable with the subType's @idref
    attribute holds the value of the @id of an &lt;xccdf:Value&gt;
    element.

    :cvar VALUE: Replace with the selected &lt;xccdf:value&gt; or
        &lt;xccdf:complex-value&gt; of an &lt;xccdf:Value&gt;.
    :cvar TITLE: Replace with the &lt;xccdf:title&gt; of the
        &lt;xccdf:Value&gt;.
    :cvar LEGACY: Use the context-dependent processing of
        &lt;xccdf:sub&gt; elements outlined in XCCDF 1.1.4.
    """

    VALUE = "value"
    TITLE = "title"
    LEGACY = "legacy"
