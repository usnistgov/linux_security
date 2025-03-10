from dataclasses import dataclass, field
from typing import Optional

from scap.question_type import QuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionType(QuestionType):
    """
    The StringQuestionType type defines a question that requires a string answer.

    :ivar default_answer: An optional default value may be specified as
        the answer.
    """

    default_answer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
