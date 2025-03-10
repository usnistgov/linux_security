from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class ResultEnumType(Enum):
    """
    Allowed result indicators for a test.

    :cvar PASS: The target system or system component satisfied all the
        conditions of the &lt;xccdf:Rule&gt;.
    :cvar FAIL: The target system or system component did not satisfy
        all the conditions of the &lt;xccdf:Rule&gt;.
    :cvar ERROR: The checking engine could not complete the evaluation;
        therefore the status of the target’s compliance with the
        &lt;xccdf:Rule&gt; is not certain. This could happen, for
        example, if a testing tool was run with insufficient privileges
        and could not gather all of the necessary information.
    :cvar UNKNOWN: The testing tool encountered some problem and the
        result is unknown. For example, a result of ‘unknown’ might be
        given if the testing tool was unable to interpret the output of
        the checking engine (the output has no meaning to the testing
        tool).
    :cvar NOTAPPLICABLE: The &lt;xccdf:Rule&gt; was not applicable to
        the target of the test. For example, the &lt;xccdf:Rule&gt;
        might have been specific to a different version of the target
        OS, or it might have been a test against a platform feature that
        was not installed.
    :cvar NOTCHECKED: The &lt;xccdf:Rule&gt; was not evaluated by the
        checking engine. This status is designed for &lt;xccdf:Rule&gt;
        elements that have no check. It may also correspond to a status
        returned by a checking engine if the checking engine does not
        support the indicated check code.
    :cvar NOTSELECTED: The &lt;xccdf:Rule&gt; was not selected in the
        &lt;xccdf:Benchmark&gt;.
    :cvar INFORMATIONAL: The &lt;xccdf:Rule&gt; was checked, but the
        output from the checking engine is simply information for
        auditors or administrators; it is not a compliance category.
        This status value is designed for &lt;xccdf:Rule&gt; elements
        whose main purpose is to extract information from the target
        rather than test the target.
    :cvar FIXED: The &lt;xccdf:Rule&gt; had failed, but was then fixed
        (possibly by a tool that can automatically apply remediation, or
        possibly by the human auditor).
    """

    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    UNKNOWN = "unknown"
    NOTAPPLICABLE = "notapplicable"
    NOTCHECKED = "notchecked"
    NOTSELECTED = "notselected"
    INFORMATIONAL = "informational"
    FIXED = "fixed"
