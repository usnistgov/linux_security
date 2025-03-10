from dataclasses import dataclass, field
from typing import Optional

from scap.artifact_refs_type import ArtifactRefsType
from scap.result_type import ResultType
from scap.test_action_ref_type import TestActionRefType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestActionConditionType:
    """The TestActionConditionType complex type specifies processing
    instructions - either produce a result or move on to another test. The
    TestActionConditionType is extended by all handlers ("when_...") in
    test_actions.

    :ivar result: This element indicates that a final value (i.e. PASS,
        FAIL, ERROR, UNKNOWN, NOT_TESTED, NOT_APPLICABLE) should be
        returned if the encapsulating handler is invoked.
    :ivar test_action_ref: This element indicates that a new test_action
        should be processed if the encapsulating handler is invoked.
    :ivar artifact_refs: The artifact_refs element contains all the
        artifacts that must be requested when a question, test_action,
        or questionnaire has been evaluated.
    """

    result: Optional[ResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    test_action_ref: Optional[TestActionRefType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    artifact_refs: Optional[ArtifactRefsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
