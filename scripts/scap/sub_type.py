from dataclasses import dataclass, field

from scap.idref_type import IdrefType
from scap.sub_use_enum_type import SubUseEnumType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class SubType(IdrefType):
    """The type used for &lt;xccdf:sub&gt; elements.

    The &lt;xccdf:sub&gt; element identifies replacement content that
    should appear in place of the &lt;xccdf:sub&gt; element during text
    substitution. The subType consists of a regular idrefType with an
    additional @use attribute to dictate the behavior of the
    &lt;xccdf:sub&gt; element under substitution. When the @idref is to
    an &lt;xccdf:Value&gt;, the @use attribute indicates whether the
    &lt;xccdf:Value&gt; element's title or value should replace the
    &lt;xccdf:sub&gt; element. The @use attribute is ignored when the
    @idref is to an &lt;xccdf:plain-text&gt; element; the body of the
    &lt;xccdf:plain-text&gt; element is always used to replace the
    &lt;xccdf:sub&gt; element.

    :ivar use: Dictates the nature of the content inserted under text
        substitution processing.
    """

    class Meta:
        name = "subType"

    use: SubUseEnumType = field(
        default=SubUseEnumType.VALUE,
        metadata={
            "type": "Attribute",
        },
    )
