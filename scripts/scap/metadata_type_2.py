from dataclasses import dataclass, field

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class MetadataType2:
    """Data type that supports inclusion of metadata about a document or element.

    This is particularly useful for facilitating the discovery and
    retrieval of XCCDF checklists from public repositories. When used,
    the contents of the &lt;xccdf:metadata&gt; element are expressed in
    XML. The &lt;xccdf:Benchmark&gt; element's metadata should contain
    information formatted using the Dublin Core Metadata Initiative
    (DCMI) Simple DC Element specification, as described in [DCES] and
    [DCXML]. Benchmark consumers should be prepared to process Dublin
    Core metadata in the &lt;xccdf:metadata&gt; element. Other metadata
    schemes, including ad-hoc elements, are also allowed, both in the
    &lt;xccdf:Benchmark&gt; and in other elements.
    """

    class Meta:
        name = "metadataType"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
