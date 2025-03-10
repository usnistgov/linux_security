from dataclasses import dataclass

from scap.choice_question_type import ChoiceQuestionType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestion(ChoiceQuestionType):
    """A choice_question is a type of question element with one or more acceptable
    answers specified by the author.

    One of these specified answers will be given as the response.
    Acceptable answers are specified either explicitly using the choice
    element or implicitly using the choice_group_ref element to
    reference a choice_group element. Choices are presented in the order
    in which they are provided. All the choices in a choice_group are
    inserted in the order in which they appear within the choice_group.
    """

    class Meta:
        name = "choice_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
