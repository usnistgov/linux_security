from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/scap/source/1.2"


class ScapVersionType(Enum):
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"
    VALUE_1_2 = "1.2"
    VALUE_1_3 = "1.3"
