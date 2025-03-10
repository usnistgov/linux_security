from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


class UseCaseType(Enum):
    CONFIGURATION = "CONFIGURATION"
    VULNERABILITY = "VULNERABILITY"
    INVENTORY = "INVENTORY"
    OTHER = "OTHER"
