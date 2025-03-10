from dataclasses import dataclass

from scap.ociltype import Ociltype

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Ocil(Ociltype):
    """The ocil element is the root XML element of an OCIL document.

    It contains information about one or more questionnaires. It may
    also contain results elements to store prior responses.
    """

    class Meta:
        name = "ocil"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
