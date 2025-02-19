from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from oval.definitions.sources.oval_common_schema import (
    CheckEnumeration,
    ClassEnumeration,
    ExistenceEnumeration,
    GeneratorType,
    MessageType,
    OperatorEnumeration,
)
from oval.definitions.sources.oval_definitions_schema import OvalDefinitions
from oval.definitions.sources.oval_system_characteristics_schema import (
    OvalSystemCharacteristics,
)
from oval.definitions.sources.xmldsig_core_schema import Signature

__NAMESPACE__ = "urn:oval:v6:results"


class ContentEnumeration(Enum):
    """The ContentEnumeration defines the valid values for the directives
    controlling the amount of expected depth found in the results document.

    Each directive specified at the top of an OVAL Results document
    defines how much information should be included in the document for
    each of the different result types.  The amount of content that is
    expected with each value is defined by Schematron statements
    embedded throughout the OVAL Results Schema.  Currently, the
    enumeration defines two values: thin and full.  Please refer to the
    documentation of each individual value of this enumeration for more
    information about what each means.

    :cvar THIN: A value of 'thin' means only the minimal amount of
        information will be provided. This is the id associated with an
        evaluated OVAL Definition and the result of the evaluation. The
        criteria child element of a definition should not be present
        when providing thin results. In addition, system characteristic
        information for the objects used by the given definition should
        not be presented.
    :cvar FULL: A value of 'full' means that very detailed information
        will be provided allowing in-depth reports to be generated from
        the results. In addition to the results of the evaluated
        definition, the results of all extended definitions and tests
        included in the criteria as well as the actual information
        collected off the system must be presented.
    """

    THIN = "thin"
    FULL = "full"


class ResultEnumeration(Enum):
    """
    The ResultEnumeration defines the acceptable result values for the
    DefinitionType, CriteriaType, CriterionType, ExtendDefinitionType, TestType,
    and TestedItemType constructs.

    :cvar TRUE: When evaluating a definition or test, a result value of
        'true' means that the characteristics being evaluated match the
        information represented in the system characteristic document.
        When evaluating a tested_item, and a state exists, a result
        value of 'true' indicates that the item matches the state.
    :cvar FALSE: When evaluating a definition or test, a result value of
        'false' means that the characteristics being evaluated do not
        match the information represented in the system characteristic
        document.  When evaluating a tested_item, and a state exists, a
        result value of 'false' indicates that the item does not match
        the state.
    :cvar UNKNOWN: When evaluating a definition or test, a result value
        of 'unknown' means that the characteristics being evaluated
        cannot be found in the system characteristic document (or the
        characteristics can be found but collected object flag is 'not
        collected'). For example, assume that a definition tests a file,
        but data pertaining to that file cannot be found and is not
        recorded in the System Characteristics document. The lack of an
        item (in the system_data section) for this file in the System
        Characteristics document means that no attempt was made to
        collect information about the file. In this situation, there is
        no way of knowing what the result would be if the file was
        collected. Note that finding a collected_object element in the
        system characteristic document is not the same as finding a
        matching element of the system. When evaluating an OVAL Test,
        the lack of a matching object on a system (for example, file not
        found) does not cause a result of unknown since an test
        considers both the state of an item and its existence. In this
        case the test result would be based on the existence check
        specified by the check_existence attribute on the test.  When
        evaluating a tested_item, and a state exists, a result value of
        'unknown' indicates that it could not be determined whether or
        not the item and state match. For example, if a registry_object
        with a hive equal to HKEY_LOCAL_MACHINE, a key with the xsi:nil
        attribute set to 'true', and a name with the xsi:nil attribute
        set to 'true' was collected and compared against a
        registry_state with key entity equal to 'SOFTWARE', the
        tested_item result would be 'unknown' because an assertion of
        whether or not the item matches the state could not be
        determined since the key entity of the item was not collected.
    :cvar ERROR: When evaluating a definition or test, a result value of
        'error' means that the characteristics being evaluated exist in
        the system characteristic document but there was an error either
        collecting information or in performing analysis. For example,
        if there was an error returned by an api when trying to
        determine if an object exists on a system. Another example would
        be: xsi:nil might be set on an object entity, but then the
        entity is compared to a state entity with a value, thus
        producing an error.  When evaluating a tested_item, and a state
        exists, a result value of 'error' indicates that there was
        either an error collecting the item or there was an error
        analyzing the item against the state. For example, a tested_item
        will receive a result value of 'error' if an attempt is made to
        compare a state entity against an item entity that has a status
        of 'error'.
    :cvar NOT_EVALUATED: When evaluating a definition or test, a result
        value of 'not evaluated' means that a choice was made not to
        evaluate the given definition or test. The actual result is not
        known since if evaluation had occurred the result could have
        been either true or false.  When evaluating a tested_item, a
        result value of 'not evaluated' indicates that a state was not
        specified and is equivalent to an existence check.
    :cvar NOT_APPLICABLE: When evaluating a definition or test, a result
        value of 'not applicable' means that the definition or test
        being evaluated is not valid on the given platform. For example,
        trying to collect Linux RPM information on a Windows system is
        not possible and so a result of not applicable is used.  Another
        example would be in trying to collect RPM information on a linux
        system that does not have the RPM packaging system installed.
    """

    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    ERROR = "error"
    NOT_EVALUATED = "not evaluated"
    NOT_APPLICABLE = "not applicable"


@dataclass
class TestedVariableType:
    """The TestedVariableType complex type holds the value of a variable used
    during the evaluation of a test.

    Of special importance are the values of any external variables used
    since these values are not captured in either the definition or
    system characteristic documents. If a variable is represented by a
    collection of values, then multiple elements of TestedVariableType,
    each with the same variable_id attribute, would exist. The required
    variable_id attribute is the unique id of the variable that was
    used.
    """

    value: Optional[object] = field(default=None)
    variable_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )


@dataclass
class CriterionType:
    """The CriterionType complex type identifies a specific test that is included
    in the definition's criteria.

    The optional applicability_check attribute provides a Boolean flag
    that when true indicates that the criterion is being used to
    determine whether the OVAL Definition applies to a given system. The
    required test_ref attribute is the actual id of the included test.
    The required version attribute is the specific version of the OVAL
    Test used during analysis. The optional variable_instance attribute
    differentiates between unique instances of a test. This can happen
    when a test includes a variable reference and different variable
    values are used by different definitions. The optional negate
    attribute signifies that the result of an individual test should be
    negated during analysis. For example, consider a test that evaluates
    to TRUE if a specific patch is installed. By negating this test, it
    now evaluates to TRUE if the patch is NOT installed. The required
    result attribute holds the result of the evaluation. Please refer to
    the description of the ResultEnumeration for details about the
    different result values.
    """

    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    test_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:tst:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    variable_instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    result: Optional[ResultEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DirectiveType:
    """An individual directive element determines whether or not a specific type of
    result is included in the results document.

    The required reported attribute controls this by providing a true or
    false for the specific directive. The optional content attribute
    controls how much information about the specific result is provided.
    For example, thin content would only be the id of the definition and
    the result, while a full content set would be the definition id with
    the result along with results for all the individual tests and
    extended definitions.  Please refer to the oval-
    res:ContentEnumeration for details about the different content
    options.
    """

    reported: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: ContentEnumeration = field(
        default=ContentEnumeration.FULL,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ExtendDefinitionType:
    """The ExtendDefinitionType complex type identifies a specific definition that
    has been extended by the criteria.

    The optional applicability_check attribute provides a Boolean flag
    that when true indicates that the extend_definition is being used to
    determine whether the OVAL Definition applies to a given system. The
    required definition_ref attribute is the actual id of the extended
    definition. The required version attribute is the specific version
    of the OVAL Definition used during analysis. The optional
    variable_instance attribute is a unique id that differentiates each
    unique instance of a definition. Capabilities that use OVAL may
    reference the same definition multiple times and provide different
    variable values each time the definition is referenced. This will
    result in multiple instances of a definition being included in the
    OVAL Results document (definitions that do not use variables can
    only have one unique instance). The inclusion of this unique
    instance identifier allows the OVAL Results document to associate
    the correct objects and items for each combination of supplied
    values. The optional negate attribute signifies that the result of
    an extended definition should be negated during analysis. For
    example, consider a definition that evaluates TRUE if certain
    software is installed. By negating the definition, it now evaluates
    to TRUE if the software is NOT installed. The required result
    attribute holds the result of the evaluation. Please refer to the
    description of the ResultEnumeration for details about the different
    result values.
    """

    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:def:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    variable_instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    result: Optional[ResultEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TestedItemType:
    """The TestedItemType complex type holds a reference to a system characteristic
    item that matched the object specified in a test.

    Details of the item can be found in the oval_system_characteristics
    section of the OVAL Results document by using the required item_id.
    The optional message element holds an error message or some other
    message that the analysis engine wishes to pass along. The required
    result attribute holds the result of the evaluation of the
    individual item as it relates to the state specified by the test. If
    the test did not include a state reference then the result attribute
    will be set to 'not evaluated'. Please refer to the description of
    the ResultEnumeration for details about the different result values.
    """

    message: list[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    item_id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    result: Optional[ResultEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CriteriaType:
    """The CriteriaType complex type describes the high level container for all the
    tests and represents the meat of the definition.

    Each criteria can contain other criteria elements in a recursive
    structure allowing complex logical trees to be constructed. Each
    referenced test is represented by a criterion element. Please refer
    to the description of the CriterionType for more information about
    and individual criterion element. The optional extend_definition
    element allows existing definitions to be included in the criteria.
    Refer to the description of the ExtendDefinitionType for more
    information. The required operator attribute provides the logical
    operator that binds the different statements inside a criteria
    together. The optional negate attribute signifies that the result of
    an extended definition should be negated during analysis. For
    example, consider a definition that evaluates TRUE if a certain
    software is installed. By negating the definition, it now evaluates
    to TRUE if the software is NOT installed. The required result
    attribute holds the result of the evaluation of the criteria. Note
    that this would be after any negation operation has been applied.
    Please refer to the description of the ResultEnumeration for details
    about the different result values. The optional applicability_check
    attribute provides a Boolean flag that when true indicates that the
    criteria is being used to determine whether the OVAL Definition
    applies to a given system.
    """

    criteria: list["CriteriaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    criterion: list[CriterionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extend_definition: list[ExtendDefinitionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operator: Optional[OperatorEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    result: Optional[ResultEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DirectivesType:
    """The DirectivesType complex type presents a set of flags that describe what
    information has been included in the results document.

    There are six possible results (true, false, unknown, error, not
    evaluated, and not applicable) for the evaluation of an OVAL
    Definition. The directives state which of these results are being
    reported in the results document.
    """

    definition_true: Optional[DirectiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    definition_false: Optional[DirectiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    definition_unknown: Optional[DirectiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    definition_error: Optional[DirectiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    definition_not_evaluated: Optional[DirectiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    definition_not_applicable: Optional[DirectiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class TestType:
    """The TestType complex type provides a reference to every item that matched
    the object section of the original test as well as providing an overall test
    result based on those items.

    The optional message element holds an error message or some other
    string that the analysis engine wishes to pass along. The optional
    tested_variable elements hold the value of each variable used by the
    test during evaluation. This includes the values used in both OVAL
    Objects and OVAL States. If a variable represents a collection of
    values, then multiple tested_variable elements would exist with the
    same variable_id attribute. Please refer to the description of oval-
    res:TestedVariableType for more information. The required test_id
    attribute identifies the test and must conform to the format
    specified by the oval:TestIDPattern simple type. The required
    version attribute is the specific version of the OVAL Test used
    during analysis. The optional variable_instance attribute
    differentiates between unique instances of a test. This can happen
    when a test includes a variable reference and different values for
    that variable are used by different definitions. The
    check_existence, check, and state_operator attributes reflect the
    values that were specified on the test as it was evaluated. These
    evaluation control attributes are copied into the OVAL Results file
    to enable post processing of results documents.  More information on
    each of these attributes is provided with the definition of the
    oval-def:TestType. The required result attribute holds the result of
    the evaluation after all referenced items have been examined and the
    evaluation control attributes have been applied. Please refer to the
    description of the oval-res:ResultEnumeration for details about the
    different result values.  In general, the overall result of an OVAL
    Test is determined by combining the results of each matching item
    based first on the check_existence attribute, then the check
    attribute, and finally the state_operator attribute. The following
    section provides a more detailed description of  how the result for
    an OVAL Test is determined when using an OVAL System Characteristics
    document. An OVAL System Characteristics document can contain an
    optional collected_objects section. When the collected_objects
    section is present the following rules specify how the overall
    result for an OVAL Test is determined: When an oval-
    sc:collected_objects/oval-sc:object with an id that matches the OVAL
    Object id that is referenced by the OVAL Test is not found, the
    result for the OVAL Test must be "unknown". When the flag attribute
    of the corresponding oval-sc:collected_objects/oval-sc:object is
    "error", the result of the OVAL Test must be "error". When the flag
    attribute of the corresponding oval-sc:collected_objects/oval-
    sc:object is "not collected", the result of the OVAL Test must be
    "unknown".  When the flag attribute of the corresponding oval-
    sc:collected_objects/oval-sc:object is "not applicable", the result
    of the OVAL Test must be "not applicable".  When the flag attribute
    of the corresponding oval-sc:collected_objects/oval-sc:object is
    "does not exist", the result of the OVAL Test is determined by
    examining the check_existence attribute's value and if the
    check_existence attribute is "none_exist" or "any_exist" the OVAL
    Test should evaluate to "true", for all other values of the
    check_existence attribute the OVAL Test should evaluate to "false".
    The check and state_operator attributes do not need to be considered
    in this condition. When the flag attribute of the corresponding
    oval-sc:collected_objects/oval-sc:object is "complete", the result
    of the OVAL Test is determined by first evaluating the
    check_existence attribute specified by the OVAL Test and then
    evaluating the check and state_operator attributes. The check
    attribute only needs to be considered if the result of evaluating
    the check_existence attribute is "true". When the flag attribute of
    the corresponding oval-sc:collected_objects/oval-sc:object is
    "incomplete", the result of the OVAL Test must be "unknown" with the
    following exceptions: 1) When the check_existence attribute of the
    OVAL Test is set to "none_exist" and the collected object has 1 or
    more item references with a status of "exists", a result of "false"
    must be reported;  2) When the check_existence attribute of the OVAL
    Test is set to "only_one_exists", the collected object has more than
    1 item reference with a status of "exists", a result of "false" must
    be reported;  3) If after evaluating the check_existence attribute a
    non "true" result has not been determined, the check attribute must
    be considered as follows: 3a) If the check attribute evaluation
    results in "false", then the OVAL Test result must be "false"; 3b)
    If the check attribute is set to "at_least_one_satisfies" and its
    evaluation results in "true", the OVAL Test result must be "true".
    When the collected_objects section is not present in the OVAL System
    Characteristics document, the evaluation engine must search the
    system characteristics for all Items that match the OVAL Object
    referenced by the OVAL Test. The set of matching OVAL Items is then
    evaluated first based on the check_existence attribute, then the
    check attribute, and finally the state_operator attribute.
    """

    message: list[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tested_item: list[TestedItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tested_variable: list[TestedVariableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    test_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:tst:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    variable_instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    check_existence: ExistenceEnumeration = field(
        default=ExistenceEnumeration.AT_LEAST_ONE_EXISTS,
        metadata={
            "type": "Attribute",
        },
    )
    check: Optional[CheckEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: OperatorEnumeration = field(
        default=OperatorEnumeration.AND,
        metadata={
            "type": "Attribute",
        },
    )
    result: Optional[ResultEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ClassDirectivesType(DirectivesType):
    """The ClassDirectivesType complex type presents a set of flags that describe
    what information has been included in the results document for a specific OVAL
    Definition class.

    See the definition of the oval-res:DirectivesType for more
    information. The required class attribute allows a set of directives
    to be specified for each supported OVAL Definition class (See the
    definition of the oval:ClassEnumeration for more information about
    the supported classes). A set of class specific directives overrides
    the default directives for the specified definition class. A given
    class may be specified once.
    """

    class_value: Optional[ClassEnumeration] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DefaultDirectivesType(DirectivesType):
    """The DefaultDirectivesType complex type presents the default set of flags
    that describe what information has been included in the results document.

    See the definition of the oval-res:DirectivesType for more
    information. The optional include_source_definitions attribute
    indicates whether or not the source OVAL Definitions document has
    been included in the results document.  A value of false indicates
    that the source OVAL Definitions has not been included. By default
    the source document is included.
    """

    include_source_definitions: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DefinitionType:
    """The DefinitionType complex type holds the result of the evaluation of an
    OVAL Definition.

    The message element holds an error message or some other string that the analysis engine wishes to pass along. In addition, the optional criteria element provides the results of the individual pieces of the criteria. Please refer to the description of the CriteriaType for more information.
    The required definition_id attribute is the OVAL id of the definition.
    The required version attribute is the specific version of the OVAL Definition used during analysis.
    The optional variable_instance attribute is a unique id that differentiates each unique instance of a definition. Capabilities that use OVAL may reference the same definition multiple times and provide different variable values each time the definition is referenced. This will result in multiple instances of a definition being included in the OVAL Results document (definitions that do not use variables can only have one unique instance). The inclusion of this unique instance identifier allows the OVAL Results document to associate the correct objects and items for each combination of supplied values.
    The optional class attribute ...
    The required result attribute holds the result of the evaluation. Please refer to the description of the ResultEnumeration for details about the different result values.
    """

    message: list[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    criteria: Optional[CriteriaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    definition_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:def:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    variable_instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[ClassEnumeration] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    result: Optional[ResultEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TestsType:
    """The TestsType complex type is a container for one or more test elements.

    Each test element holds the result of the evaluation of an OVAL
    Test. Please refer to the description of TestType for more
    information about an individual test element.
    """

    test: list[TestType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class DefinitionsType:
    """The DefinitionsType complex type is a container for one or more definition
    elements.

    Each definition element holds the result of the evaluation of an
    OVAL Definition. Please refer to the description of DefinitionType
    for more information about an individual definition element.
    """

    definition: list[DefinitionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class SystemType:
    """The SystemType complex type holds the evaluation results of the definitions
    and tests, as well as a copy of the OVAL System Characteristics used to perform
    the evaluation.

    The definitions section holds the results of the definitions and the
    tests section holds the results of the tests. The
    oval_system_characteristics section is a copy of the System
    Characteristics document used to perform the evaluation of the OVAL
    Definitions.
    """

    definitions: Optional[DefinitionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tests: Optional[TestsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    oval_system_characteristics: Optional[OvalSystemCharacteristics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oval:v6:system-characteristics",
            "required": True,
        },
    )


@dataclass
class ResultsType:
    """The ResultsType complex type is a container for one or more system elements.

    Each system element defines the results associated with an
    individual system. Please refer to the description of SystemType for
    more information about an individual system element.
    """

    system: list[SystemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class OvalResults:
    """The oval_results element is the root of an OVAL Results Document.

    Its purpose is to bind together the four major sections of a results document - generator, directives, oval_definitions, and results - which are the children of the root element. It must contain exactly one generator section, one directives section, and one results section.

    :ivar generator: The required generator section provides information
        about when the results document was compiled and under what
        version.
    :ivar directives: The required directives section presents flags
        describing what information has been included in the results
        document. This element represents the default set of directives.
        These directives apply to all classes of definitions for which
        there is not a class specific set of directives.
    :ivar class_directives: The optional class_directives section
        presents flags describing what information has been included in
        the results document for a specific OVAL Definition class. The
        directives for a particlar class override the default
        directives. Using OVAL Results class_directives, an OVAL Results
        document dealing with vulnerabilities might by default include
        only minimal information and then include full details for all
        vulnerability definitions that evaluated to true.
    :ivar oval_definitions: The oval_definitions section is optional and
        dependent on the include_source_definitions attribute of the
        directives element. Its purpose is to provide an exact copy of
        the definitions evaluated for the results document.
    :ivar results: The required results section holds all the results of
        the evaluated definitions.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_results"
        namespace = "urn:oval:v6:results"

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    directives: Optional[DefaultDirectivesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    class_directives: list[ClassDirectivesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        },
    )
    oval_definitions: Optional[OvalDefinitions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oval:v6:definitions",
        },
    )
    results: Optional[ResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
