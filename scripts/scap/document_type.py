from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class DocumentType:
    """
    The DocumentType type describes structures used to provide document-level
    information, including title, descriptions, and notices.

    :ivar title: The title element provides a title for this document.
    :ivar description: Each description element contains part of an
        overall description for the entire document. (Note that
        questionnaires contain their own description for questionnaire
        specific descriptions.) TODO: Consider changing this to XHTML
        structured text in the next revision.
    :ivar notice: Each notice element contains a notice or warning to
        the user of this document. TODO: Consider changing this to XHTML
        structured text in the next revision.
    """

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        },
    )
    description: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    notice: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
