from dataclasses import dataclass

from scap.spkidata_type import SpkidataType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
