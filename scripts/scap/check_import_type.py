from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class CheckImportType:
    """Data type for the &lt;xccdf:check-import&gt; element, which specifies a
    value that the &lt;xccdf:Benchmark&gt; author wishes to retrieve from the
    checking system during testing of a target system.

    The @import-name attribute identifies some structure in the checking
    system that is then retrieved. The mapping from the values of this
    attribute to specific checking system structures is beyond the scope
    of the XCCDF specification. When the &lt;xccdf:check-import&gt;
    element appears in the context of an &lt;xccdf:Rule&gt;, then it
    should be empty and any content must be ignored. When the
    &lt;xccdf:check-import&gt; element appears in the context of an
    &lt;xccdf:rule-result&gt;, then its body holds the imported value.

    :ivar import_name: An identifier indicating some structure in the
        checking system to be collected.
    :ivar import_xpath: An XPath that is used to select specific values
        or structures from the imported structure. This allows further
        refinement of the collected data if the imported value takes the
        form of XML structures.
    :ivar content:
    """

    class Meta:
        name = "checkImportType"

    import_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "import-name",
            "type": "Attribute",
            "required": True,
        },
    )
    import_xpath: Optional[str] = field(
        default=None,
        metadata={
            "name": "import-xpath",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
