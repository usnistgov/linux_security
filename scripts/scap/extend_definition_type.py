from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ExtendDefinitionType:
    """The ExtendDefinitionType complex type allows existing definitions to be
    extended by another definition.

    This works by evaluating the extended definition and then using the
    result within the logical context of the extending definition. The
    required definition_ref attribute is the actual id of the definition
    being extended. The optional negate attribute signifies that the
    result of an extended definition should be negated during analysis.
    For example, consider a definition that evaluates TRUE if
    certainsoftware is installed. By negating the definition, it now
    evaluates to TRUE if the software is NOT installed. The optional
    comment attribute provides a short description of the specified
    definition and should mirror the title metadata of the extended
    definition. The optional applicability_check attribute provides a
    Boolean flag that when true indicates that the extend_definition is
    being used to determine whether the OVAL Definition applies to a
    given system.
    """

    def generate_check(self, data):
        print("Extended definition evaluating!")
        data["definitions"][self.definition_ref].generate_check(data)

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
