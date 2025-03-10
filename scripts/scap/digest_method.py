from dataclasses import dataclass

from scap.digest_method_type import DigestMethodType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DigestMethod(DigestMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
