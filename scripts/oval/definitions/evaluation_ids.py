from dataclasses import dataclass, field

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/ovaldi/evalids"


@dataclass
class EvalutationDefinitionIds:
    """The evaluation-definition-ids element is the root the Document.

    Its purpose is to bind together the a set of definition elements.

    :ivar definition: Each definition represents the id of a definition
        to be evaluated.
    """

    class Meta:
        name = "evalutation-definition-ids"
        namespace = "http://oval.mitre.org/XMLSchema/ovaldi/evalids"

    definition: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:def:[1-9][0-9]*",
        },
    )
