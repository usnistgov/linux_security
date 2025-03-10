from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ScoreType:
    """
    Type for a score value in an &lt;xccdf:TestResult&gt;.

    :ivar value:
    :ivar system: A URI indicating the scoring model used to create this
        score.
    :ivar maximum: The maximum possible score value that could have been
        achieved under the named scoring system.
    """

    class Meta:
        name = "scoreType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
