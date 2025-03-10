from dataclasses import dataclass

from scap.x509_data_type import X509DataType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class X509Data(X509DataType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
