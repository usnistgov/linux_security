from dataclasses import dataclass

from scap.test_result_type import TestResultType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TestResult(TestResultType):
    """The &lt;xccdf:TestResult&gt; element encapsulates the results of a single
    application of an &lt;xccdf:Benchmark&gt; to a single target platform.

    The &lt;xccdf:TestResult&gt; element normally appears as the child
    of the &lt;xccdf:Benchmark&gt; element, although it may also appear
    as the top-level element of an XCCDF results document. XCCDF is not
    intended to be a database format for detailed results; the
    &lt;xccdf:TestResult&gt; element offers a way to store the results
    of individual tests in modest detail, with the ability to reference
    lower-level testing data.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
