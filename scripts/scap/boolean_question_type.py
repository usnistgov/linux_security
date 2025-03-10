from dataclasses import dataclass, field
from typing import Optional

from scap.boolean_question_model_type import BooleanQuestionModelType
from scap.question_type import QuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestionType(QuestionType):
    """
    The BooleanQuestionType type defines a question with valid responses of either
    {TRUE, FALSE} or {YES, NO}.

    :ivar default_answer: The default_answer attribute specifies the
        default value of the boolean_question. Its value may be set to
        true or false.
    :ivar model: The model attribute specifies whether the response
        should be from the set {True, False} or the set {YES, NO}. If
        the value of this attribute is not set, then it defaults to
        MODEL_YES_NO (i.e. response can either be YES or NO).
    """

    default_answer: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    model: BooleanQuestionModelType = field(
        default=BooleanQuestionModelType.MODEL_YES_NO,
        metadata={
            "type": "Attribute",
        },
    )
