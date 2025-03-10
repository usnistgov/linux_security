from dataclasses import dataclass, field
from typing import Optional, Union

from scap.lang_value import LangValue
from scap.sub_type import SubType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileNoteType:
    """Type for an &lt;xccdf:profile-note&gt; within an &lt;xccdf:Rule&gt;.

    This element contains text that describes special aspects of an
    &lt;xccdf:Rule&gt; relative to one or more &lt;xccdf:Profile&gt;
    elements. This allows an author to document things within
    &lt;xccdf:Rule&gt; elements that are specific to a given
    &lt;xccdf:Profile&gt;. This information might then be displayed to a
    reader based on the selection of a particular &lt;xccdf:Profile&gt;.
    The body text may include XHTML mark-up as well as &lt;xccdf:sub&gt;
    elements.

    :ivar lang:
    :ivar tag: The identifier of this note.
    :ivar content:
    """

    class Meta:
        name = "profileNoteType"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": SubType,
                    
                },
            ),
        },
    )
