from dataclasses import dataclass

from scap.retrieval_method_type import RetrievalMethodType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RetrievalMethod(RetrievalMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
