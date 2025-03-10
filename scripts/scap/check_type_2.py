from dataclasses import dataclass, field
from typing import Optional

from scap.check_content_ref_type import CheckContentRefType
from scap.check_content_type import CheckContentType
from scap.check_export_type import CheckExportType
from scap.check_import_type import CheckImportType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class CheckType2:
    """Data type for the &lt;xccdf:check&gt; element.

    The &lt;xccdf:check&gt; element identifies instructions for tests to
    determine compliance with the &lt;xccdf:Rule&gt; as well as
    parameters controlling the reporting of those test results. The
    &lt;xccdf:check&gt; element must have at least one child element.

    :ivar check_import: Identifies a value to be retrieved from the
        checking system during testing of a target system. This
        element's body must be empty within an &lt;xccdf:check&gt;.
        After the associated check results have been collected, the
        result structure returned by the checking engine is processed to
        collect the named information. This information is then recorded
        in the check-import element in the corresponding &lt;xccdf:rule-
        result&gt;.
    :ivar check_export: A mapping from an &lt;xccdf:Value&gt; element to
        a checking system variable (i.e., external name or id for use by
        the checking system). This supports export of tailoring values
        from the XCCDF processing environment to the checking system.
    :ivar check_content_ref: Points to code for a detached check in
        another location that uses the language or system specified by
        the &lt;xccdf:check&gt; element’s @system attribute. If multiple
        &lt;xccdf:check-content-ref&gt; elements appear, they represent
        alternative locations from which a benchmark consumer may obtain
        the check content. Benchmark consumers should process the
        alternatives in the order in which they appear in the XML. The
        first &lt;xccdf:check-content-ref&gt; from which content can be
        successfully retrieved should be used.
    :ivar check_content: Holds the actual code of a check, in the
        language or system specified by the &lt;xccdf:check&gt;
        element’s @system attribute. If both &lt;xccdf:check-content-
        ref&gt; and &lt;xccdf:check-content&gt; elements appear in a
        single &lt;xccdf:check&gt; element, benchmark consumers should
        use the &lt;xccdf:check-content&gt; element only if none of the
        references can be resolved to provide content.
    :ivar system: The URI for a checking system. If the checking system
        uses XML namespaces, then the system attribute for the system
        should be its namespace.
    :ivar negate: If set to true, the final result of the
        &lt;xccdf:check&gt; is negated according to the truth table
        given below.
    :ivar id: Unique identifier for this element. Optional, but must be
        globally unique if present.
    :ivar selector: This may be referenced from &lt;xccdf:Profile&gt;
        selection elements or used during manual tailoring to refine the
        application of the &lt;xccdf:Rule&gt;. If no selector values are
        specified for a given &lt;xccdf:Rule&gt; by
        &lt;xccdf:Profile&gt; elements or manual tailoring, all
        &lt;xccdf:check&gt; elements with non-empty @selector attributes
        are ignored. If an &lt;xccdf:Rule&gt; has multiple
        &lt;xccdf:check&gt; elements with the same @selector attribute,
        each must employ a different checking system, as identified by
        the @system attribute of the &lt;xccdf:check&gt; element.
    :ivar multi_check: Applicable in cases where multiple checks are
        executed to determine compliance with a single
        &lt;xccdf:Rule&gt;. This situation can arise when an
        &lt;xccdf:check&gt; includes an &lt;xccdf:check-content-ref&gt;
        element that does not include a @name attribute. The default
        behavior of a nameless &lt;xccdf:check-content-ref&gt; is to
        execute all checks in the referenced check content location and
        AND their results together into a single &lt;xccdf:rule-
        result&gt; using the AND truth table below. This corresponds to
        a @multi-check attribute value of “false”. If, however, the
        @multi-check attribute is set to "true" and a nameless
        &lt;xccdf:check-content-ref&gt; is used, the &lt;xccdf:Rule&gt;
        produces a separate &lt;xccdf:rule-result&gt; for each check.
    :ivar base:
    """

    class Meta:
        name = "checkType"

    check_import: list[CheckImportType] = field(
        default_factory=list,
        metadata={
            "name": "check-import",
            "type": "Element",
            
        },
    )
    check_export: list[CheckExportType] = field(
        default_factory=list,
        metadata={
            "name": "check-export",
            "type": "Element",
            
        },
    )
    check_content_ref: list[CheckContentRefType] = field(
        default_factory=list,
        metadata={
            "name": "check-content-ref",
            "type": "Element",
            
        },
    )
    check_content: Optional[CheckContentType] = field(
        default=None,
        metadata={
            "name": "check-content",
            "type": "Element",
            
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    multi_check: bool = field(
        default=False,
        metadata={
            "name": "multi-check",
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
