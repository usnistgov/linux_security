from dataclasses import dataclass, field

from scap.substitution_text_type import SubstitutionTextType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionTextType:
    """
    The QuestionTextType complex type defines a structure to hold the text and
    variables that comprise a question's text.
    """

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": SubstitutionTextType,
                    "namespace": "http://scap.nist.gov/schema/ocil/2.0",
                },
            ),
        },
    )
