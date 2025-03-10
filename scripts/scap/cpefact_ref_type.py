from dataclasses import dataclass, field
from typing import Optional

from scap.fact_ref_type import FactRefType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


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
            "pattern": r"[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        },
    )
