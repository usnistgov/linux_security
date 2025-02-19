from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class FactRefType:
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TextType:
    """
    This type allows the xml:lang attribute to associate a specific language with
    an element's string content.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


class OperatorEnumeration(Enum):
    """The OperatorEnumeration simple type defines acceptable operators.

    Each operator defines how to evaluate multiple arguments.
    """

    AND = "AND"
    OR = "OR"


@dataclass
class CpefactRefType(FactRefType):
    """
    A reference to a CPE Name that always evaluates to a Boolean result.
    """

    class Meta:
        name = "CPEFactRefType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[cC][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        },
    )


@dataclass
class CheckFactRefType(FactRefType):
    """A reference to a check that always evaluates to a TRUE, FALSE, or ERROR
    result.

    The CheckFactRefType complex type is used to define an element for
    holding information about an individual check. It includes a
    checking system specification URI, string content identifying the
    check content to invoke, and an external reference. The checking
    system specification should be the URI that uniquely identifies a
    revision of a check system language, and the id-ref will be an
    identifier of a test written in that language. The external
    reference should be used to point to the content in which the check
    identifier is defined.
    """

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-ref",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CheckFactRef(CheckFactRefType):
    class Meta:
        name = "check-fact-ref"
        namespace = "http://cpe.mitre.org/language/2.0"


@dataclass
class FactRef(CpefactRefType):
    class Meta:
        name = "fact-ref"
        namespace = "http://cpe.mitre.org/language/2.0"


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
            "namespace": "",
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
    operator: Optional[OperatorEnumeration] = field(
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


@dataclass
class LogicalTest(LogicalTestType):
    class Meta:
        name = "logical-test"
        namespace = "http://cpe.mitre.org/language/2.0"


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

    title: list[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    remark: list[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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


@dataclass
class PlatformType(PlatformBaseType):
    """
    :ivar id: A locally unique name for the platform. There is no
        defined format for this id; however, it must be unique within
        the containing CPE Applicability Language document.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlatformConfiguration(PlatformBaseType):
    class Meta:
        name = "platform-configuration"
        namespace = "http://cpe.mitre.org/language/2.0"


@dataclass
class Platform(PlatformType):
    class Meta:
        name = "platform"
        namespace = "http://cpe.mitre.org/language/2.0"


@dataclass
class PlatformSpecificationType:
    class Meta:
        name = "platformSpecificationType"

    platform: list[Platform] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
            "min_occurs": 1,
        },
    )


@dataclass
class PlatformSpecification(PlatformSpecificationType):
    """
    This element is the root element of a CPE Applicability Language XML document
    and therefore acts as a container for child platform definitions.
    """

    class Meta:
        name = "platform-specification"
        namespace = "http://cpe.mitre.org/language/2.0"
