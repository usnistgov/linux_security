from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


class BooleanQuestionModelType(Enum):
    """
    The BooleanQuestionModelType type provides the acceptable models (i.e. set of
    acceptable responses) for a boolean_question.

    :cvar MODEL_YES_NO: MODEL_YES_NO represents a response set of {YES,
        NO}.
    :cvar MODEL_TRUE_FALSE: MODEL_TRUE_FALSE represents a response set
        of {TRUE, FALSE}.
    """

    MODEL_YES_NO = "MODEL_YES_NO"
    MODEL_TRUE_FALSE = "MODEL_TRUE_FALSE"
