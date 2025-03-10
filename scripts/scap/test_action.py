from dataclasses import dataclass

from scap.item_base_type import ItemBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestAction(ItemBaseType):
    """
    This is a common base element for the question_test_action element.
    """

    class Meta:
        name = "test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
