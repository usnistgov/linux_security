from dataclasses import dataclass

from scap.choice_question_test_action_type import ChoiceQuestionTestActionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionTestAction(ChoiceQuestionTestActionType):
    """
    A choice_question_test_action element references a choice_question and includes
    handlers for the various choices set out in the choice_question.
    """

    class Meta:
        name = "choice_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
