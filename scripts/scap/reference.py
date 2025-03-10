from dataclasses import dataclass

from scap.reference_type_1 import ReferenceType1

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Reference(ReferenceType1):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
