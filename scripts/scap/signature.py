from dataclasses import dataclass

from scap.signature_type_1 import SignatureType1

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Signature(SignatureType1):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
