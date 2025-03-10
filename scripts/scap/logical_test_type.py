from dataclasses import dataclass, field
from typing import Optional

from scap.check_fact_ref import CheckFactRef
from scap.fact_ref import FactRef
from scap.operator_enumeration_2 import OperatorEnumeration2

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class LogicalTestType:
    """The logical-test element appears as a child of a platform element, and may
    also be nested to create more complex logical tests.

    The content consists of one or more elements:
    fact-ref, check-fact-ref, and logical-test children are permitted. The operator to be applied, and
    optional negation of the test, are given as attributes.

    :ivar logical_test: Definition of complex logical test using AND,
        OR, and/or negate operators. Evaluates to a TRUE, FALSE, or
        ERROR result.
    :ivar fact_ref: A reference to a bound form of a WFN; the reference
        always evaluates to a boolean result. The bound name contained
        within a fact-ref is meant to describe a possible set of
        products and is not meant to identify a unique product class.
    :ivar check_fact_ref: A reference to a check that always evaluates
        to TRUE, FALSE, or ERROR. Examples of types of checks are OVAL
        and OCIL checks.
    :ivar operator: The operator applied to the results of evaluating
        the fact-ref, check-fact-ref, and logical-test elements. The
        permitted operators are "AND" and "OR".
    :ivar negate: Whether the result of applying the operator should be
        negated. Possible values are "TRUE" and "FALSE". This does not
        apply if the initial result is ERROR.
    """

    logical_test: list["LogicalTestType"] = field(
        default_factory=list,
        metadata={
            "name": "logical-test",
            "type": "Element",
            
        },
    )
    fact_ref: list[FactRef] = field(
        default_factory=list,
        metadata={
            "name": "fact-ref",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
        },
    )
    check_fact_ref: list[CheckFactRef] = field(
        default_factory=list,
        metadata={
            "name": "check-fact-ref",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
        },
    )
    operator: Optional[OperatorEnumeration2] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    negate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
