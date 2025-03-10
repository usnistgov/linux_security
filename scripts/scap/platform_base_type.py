from dataclasses import dataclass, field
from typing import Optional

from scap.logical_test import LogicalTest
from scap.text_type_1 import TextType1

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class PlatformBaseType:
    """The description or qualifications of a particular IT platform type.

    The platform is defined by the logical-test child element.

    :ivar title: A human-readable title for a platform. To support uses
        intended for multiple languages, the title element supports the
        ‘xml:lang’ attribute. At most one title element can appear for
        each language.
    :ivar remark: An additional description. To support uses intended
        for multiple languages, the remark element supports the
        ‘xml:lang’ attribute. There can be multiple remarks for a single
        language.
    :ivar logical_test: Definition of test using logical operators (AND,
        OR, negate).
    """

    title: list[TextType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    remark: list[TextType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    logical_test: Optional[LogicalTest] = field(
        default=None,
        metadata={
            "name": "logical-test",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
            "required": True,
        },
    )
