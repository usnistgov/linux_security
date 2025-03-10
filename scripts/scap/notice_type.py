from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class NoticeType:
    """Data type for an &lt;xccdf:notice&gt; element.

    &lt;xccdf:notice&gt; elements are used to include legal notices
    (licensing information, terms of use, etc.), copyright statements,
    warnings, and other advisory notices about this
    &lt;xccdf:Benchmark&gt; and its use. This information may be
    expressed using XHTML or may be a simply text expression. Each
    &lt;xccdf:notice&gt; element must have a unique identifier.

    :ivar id: The unique identifier for this &lt;xccdf:notice&gt;.
    :ivar base:
    :ivar lang:
    :ivar content:
    """

    class Meta:
        name = "noticeType"

    id: Optional[str] = field(
        default=None,
        metadata={
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
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
