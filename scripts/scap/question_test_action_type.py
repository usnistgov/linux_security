from dataclasses import dataclass, field
from typing import Optional

from scap.item_base_type import ItemBaseType
from scap.test_action_condition_type import TestActionConditionType
from scap.text_type_3 import TextType3

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionTestActionType(ItemBaseType):
    """The QuestionTestActionType type defines structures that are used to hold
    handlers for non-standard results (UNKNOWN, NOT_TESTED, NOT_APPLICABLE, and
    ERROR) received from a referenced question.

    All children of question_test_action extend this type.

    :ivar title: The title element contains a descriptive heading for
        this set of handlers.
    :ivar when_unknown: The when_unknown element contains processing
        instructions for when the received result is UNKNOWN.
    :ivar when_not_tested: The when_not_tested element contains
        processing instructions for when the received result is
        NOT_TESTED.
    :ivar when_not_applicable: The when_not_applicable element contains
        processing instructions for when the received result is
        NOT_APPLICABLE.
    :ivar when_error: The when_error element contains processing
        instructions for when the received result is ERROR.
    :ivar question_ref: The question_ref attribute contains the id value
        of a question element.
    :ivar id: Each item is required to have a unique identifier that
        conforms to the definition of NCName in the Recommendation
        "Namespaces in XML 1.0", i.e., all XML 1.0 names that do not
        contain colons.
    """

    title: Optional[TextType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_unknown: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_not_tested: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_not_applicable: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    when_error: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    question_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:testaction:[1-9][0-9]*",
        },
    )
