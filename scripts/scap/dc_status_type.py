from dataclasses import dataclass, field

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class DcStatusType:
    """
    Data type element for the &lt;xccdf:dc-status&gt; element, which holds status
    information about its parent element using the Dublin Core format, expressed as
    elements of the DCMI Simple DC Element specification.
    """

    class Meta:
        name = "dc-statusType"

    purl_org_dc_elements_1_1_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://purl.org/dc/elements/1.1/",
        },
    )
