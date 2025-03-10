from dataclasses import dataclass, field

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class CheckContentType:
    """Data type for the &lt;xccdf:check-content&gt; element.

    The body of this element holds the actual code of a check, in the
    language or system specified by the &lt;xccdf:check&gt; element’s
    @system attribute. The body of this element may be any XML, but
    cannot contain any XCCDF elements. XCCDF tools do not process its
    content directly but instead pass the content directly to checking
    engines.
    """

    class Meta:
        name = "checkContentType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
