from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class SubstitutionTextType:
    """
    A type that is used to represent text from a variable that may be inserted into
    a text string within this model.
    """

    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        },
    )
