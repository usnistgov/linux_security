from dataclasses import dataclass, field
from typing import Optional

from scap.instructions_type import InstructionsType
from scap.item_base_type import ItemBaseType
from scap.question_text_type import QuestionTextType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionType(ItemBaseType):
    """
    The QuestionType complex type defines a structure to describe a question and
    any instructions to help in determining an answer.

    :ivar question_text: The question_text element provides the text of
        the question to pose.
    :ivar instructions: An optional instructions element may be included
        to hold additional instructions to assist the user in
        determining the answer to the question.
    :ivar id: Each item is required to have a unique identifier that
        conforms to the definition of NCName in the Recommendation
        "Namespaces in XML 1.0", i.e., all XML 1.0 names that do not
        contain colons.
    """

    question_text: list[QuestionTextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        },
    )
    instructions: Optional[InstructionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        },
    )
