from enum import Enum

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


class ResultType(Enum):
    """The ResultType simple type defines acceptable result values for
    questionnaires and test_actions.

    || P   | F | E | U | NT | NA ||
    ---------------||-----------------------------||------------------||------------------------------------------
    || 1+ | 0   | 0   | 0   | 0   | 0+ || Pass
    || 0+ | 1+ | 0+ | 0+ | 0+ | 0+ || Fail
    AND     || 0+ | 0   | 1+ | 0+ | 0+ | 0+ || Error
    || 0+ | 0   | 0   | 1+ | 0+ | 0+ || Unknown
    || 0+ | 0   | 0   | 0   | 1+ | 0+ || Not Tested
    || 0   | 0   | 0   | 0   | 0   | 1+ || Not Applicable
    || 0   | 0   | 0   | 0   | 0   | 0   || Not Tested
    ---------------||-----------------------------||------------------||------------------------------------------
    || 1+ | 0+ | 0+ | 0+ | 0+ | 0+ || Pass
    || 0   | 1+ | 0   | 0   | 0   | 0+ || Fail
    OR      || 0   | 0+ | 1+ | 0+ | 0+ | 0+ || Error
    || 0   | 0+ | 0   | 1+ | 0+ | 0+ || Unknown
    || 0   | 0+ | 0   | 0   | 1+ | 0+ || Not Tested
    || 0   | 0   | 0   | 0   | 0   | 1+ || Not Applicable
    || 0   | 0   | 0   | 0   | 0   | 0   || Not Tested

    :cvar UNKNOWN: An UNKNOWN value indicates that the result of a test
        cannot be determined.
    :cvar ERROR: An ERROR value indicates that an error occured while
        processing the check. Among other causes, this can indicate an
        unexpected response.
    :cvar NOT_TESTED: A NOT_TESTED value indicates that the check has
        not been tested yet.
    :cvar NOT_APPLICABLE: A NOT_APPLICABLE value indicates that the
        check is not relevant and can be skipped.
    :cvar PASS: A PASS value indicates that the check passed its test.
    :cvar FAIL: A FAIL value indicates that the check did not pass its
        test.
    """

    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
    NOT_TESTED = "NOT_TESTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    PASS = "PASS"
    FAIL = "FAIL"
