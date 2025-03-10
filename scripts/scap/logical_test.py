from dataclasses import dataclass

from scap.logical_test_type import LogicalTestType

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class LogicalTest(LogicalTestType):
    class Meta:
        name = "logical-test"
        namespace = "http://cpe.mitre.org/language/2.0"
