from dataclasses import dataclass, field
from typing import Optional

from scap.criterion_type import CriterionType
from scap.extend_definition_type import ExtendDefinitionType
from scap.operator_enumeration_1 import OperatorEnumeration1

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class CriteriaType:
    """The CriteriaType complex type describes a container for a set of sub
    criteria, criteria, criterion, or extend_definition elements allowing complex
    logical trees to be constructed.

    Each referenced test is represented by a criterion element. Please
    refer to the description of the CriterionType for more information
    about and individual criterion element. The optional
    extend_definition element allows existing definitions to be included
    in the criteria. Refer to the description of the
    ExtendDefinitionType for more information. The required operator
    attribute provides the logical operator that binds the different
    statements inside a criteria together. The optional negate attribute
    signifies that the result of the criteria as a whole should be
    negated during analysis. For example, consider a criteria that
    evaluates to TRUE if certain software is installed. By negating this
    test, it now evaluates to TRUE if the software is NOT installed. The
    optional comment attribute provides a short description of the
    criteria. The optional applicability_check attribute provides a
    Boolean flag that when true indicates that the criteria is being
    used to determine whether the OVAL Definition applies to a given
    system.
    """

    def generate_check(self, data):
        print(f"Recursively generating the check for criteria {self.comment}")
        print(f"Operator {self.operator}")
        # Get the operands (criterion)
        criterii = []
        criterions = self.criterion
        for criterion in criterions:
            criterii.append(criterion.generate_check(data))
        #print(f"Criterions: {criterions}")
        # Get the operands (criteria)
        criterias = self.criteria
        for crit in criterias:
            criterii.append(crit.generate_check(data))
        # Get the external resolvers (extended definitions)
        externals = self.extend_definition
        for extended in externals:
            criterii.append(extended.generate_check(data))
        print(f"The criterii: {criterii}")

    criteria: list["CriteriaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    criterion: list[CriterionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    extend_definition: list[ExtendDefinitionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operator: OperatorEnumeration1 = field(
        default=OperatorEnumeration1.AND,
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
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )
