from dataclasses import dataclass

from scap.cpefact_ref_type import CpefactRefType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class FactRef(CpefactRefType):
    class Meta:
        name = "fact-ref"
        namespace = "http://cpe.mitre.org/language/2.0"
