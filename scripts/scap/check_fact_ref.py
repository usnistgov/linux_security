from dataclasses import dataclass

from scap.check_fact_ref_type import CheckFactRefType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class CheckFactRef(CheckFactRefType):
    class Meta:
        name = "check-fact-ref"
        namespace = "http://cpe.mitre.org/language/2.0"
