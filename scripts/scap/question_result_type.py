from dataclasses import dataclass, field
from typing import Optional

from scap.user_response_type import UserResponseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionResultType:
    """
    The QuestionResultType complex type defines structures that hold information
    about a question and the response to it.

    :ivar question_ref: The question_ref attribute contains the id of a
        question.
    :ivar response: The response attribute classifies the response. If
        the answer to the question is standard, the response is set to
        ANSWERED (the default). If, however, the answer is exceptional
        (UNKNOWN, NOT_APPLICABLE, etc.) then this attribute will be set
        to the corresponding exceptional result.
    """

    question_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        },
    )
    response: UserResponseType = field(
        default=UserResponseType.ANSWERED,
        metadata={
            "type": "Attribute",
        },
    )
