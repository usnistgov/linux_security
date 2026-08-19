"""Classes pertaining to compliance rules.

All these classes will ingest and generate rules that are compatible with the
macOS Security Compliance Project, with both projects using the same standard
where possible.
"""

from enum import Enum
from typing import Any, Dict, List, Literal

from pydantic import (
    BaseModel,
    Field,
    ModelWrapValidatorHandler,
    field_serializer,
    model_serializer,
    model_validator,
)


class References(BaseModel):
    """Reference information.

    This class contains references utilized by rules to associate their
    information with other benchmarks or assessment platforms. Syntax may vary
    depending on the rule, so be warned.

    Attributes:
        nist: References for NIST specifications and the CCE.
        disa: References for DISA STIGs and associated IDs.
    """

    nist: dict[Literal["cce", "800-53r5", "800-171r3"], Any]
    disa: dict[Literal["cci", "srg", "disa_stig"], Any]


class CheckResult(BaseModel):
    """Expected result from checking compliance.

    When scripting, all but "exit_code" will be looking at /dev/stdout output
    to determine what the result is. If designing a rule, and need to check
    something not on /dev/stdout, you must pipe it to /dev/stdout accordingly.
    exit_code will not look at output but instead the reported exit code from
    the final command executed. Only one of exit code or result type may be
    specified.

    Attributes:
        string: Expected result of /dev/stdout type cast to a string.
        integer: Expected result of /dev/stdout type cast to an integer.
        boolean: Expected result of /dev/stdout type cast to a True/False
            value.
        exit_code: Reported exit code from the command specified..
    """

    string: str | None = None
    integer: int | None = None
    boolean: bool | None = None
    exit_code: int | None = None


class CheckInfo(BaseModel):
    """Information on how to check compliance on a system.

    If shell is present, result must be as well. additional_info can exist
    at any time, but if shell is not present, it must exist.

    Attributes:
        shell: BASH command to check compliance.
        result: Result of the BASH command to identify findings.
        additional_info: Notes regarding compliance checking.
    """

    shell: str | None = None
    result: CheckResult | None = None
    additional_info: str | None = None


class FixInfo(BaseModel):
    """Information on how to fix a system.

    Shell does not have to be populated with a command, but either shell or
    additional info must be present.

    Attributes:
        shell: BASH command to remediate the issue.
        additional_info: Notes regarding remediation.
    """

    shell: str | None = None
    additional_info: str | None = None


class EnforcementInfo(BaseModel):
    """Information on how to check or fix a system.

    If an enforcement info class is present, a check or a fix should be present
    as well.

    Attributes:
        check: Information on how to check for compliance.
        fix: Information on how to remediate compliance issues.
    """

    check: CheckInfo | None = None
    fix: FixInfo | None = None


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Benchmark(BaseModel):
    """Version-specific information regarding benchmark applicability.

    This class contains information regarding a benchmark associated with the
    containing version.

    Attributes:
        name: The name of the benchmark.
        severity: The severity ranking from low MEDIUM high. Mostly used for STIGs.
    """

    name: str
    severity: Severity | None = None

    @field_serializer("severity")
    def _fix_severity_output(self, severity: Severity):
        return severity.value


class Version(BaseModel):
    """Version-specific information used for the application of rules.

    This class is used to represent data applicable to each individual version
    associated with the platform.

    Attributes:
        benchmarks: A list of benchmarks associated wit the specific platform.
        enforcement_info: Enforcement block, containing check/fix information.
            Version-specific blocks will override platform-specific blocks.
    """

    benchmarks: List[Benchmark]
    enforcement_info: EnforcementInfo | None = None


class Platform(BaseModel):
    """Platform-specific information regarding rules.

    This class is used to represent exact specifics of how each rule should
    be implemented across various platforms. It stores information about how to
    check for compliance regarding a particular rule, and steps on how to
    remediate the compliance issue. The platform name is referenced with this
    data, likely as a key in a dictionary.

    Attributes:
        enforcement_info: A high-level block representing a globally-applicable
            check/fix across all versions of a particular platform.
        versions: A representation of each version associated with a platform,
            at least as documented by the rule.
    """

    enforcement_info: EnforcementInfo | None = None
    versions: Dict[str, Version]

    @model_validator(mode="wrap")
    @classmethod
    def _fix_version(
        cls, value: Any, handler: ModelWrapValidatorHandler["Platform"]
    ) -> "Platform":
        if isinstance(value, dict) and "versions" not in value.keys():
            copy = value.copy()
            enforcement_info = copy.pop("enforcement_info", None)

            return handler({"enforcement_info": enforcement_info, "versions": copy})
        return handler(value)

    @model_serializer(mode="wrap")
    def _fix_version_output(self, handler) -> Dict[str, Any]:
        data = handler(self)

        enforcement_info = (
            data["enforcement_info"] if "enforcement_info" in data.keys() else None
        )
        versions = data["versions"]

        result = {}
        if enforcement_info:
            result["enforcement_info"] = enforcement_info
        result.update(versions)

        return result


class Rule(BaseModel):
    """A compliance rule.

    This class is a one-to-one representation of the YAML file used to
    represent rules, and references other subclasses where needed. Loading
    data in with the class is done through Pydantic's model_validate function.

    Attributes:
        rule_id: Unique identifier for the rule (matches the YAML file stem).
        title: Human-readable title shown in the guidance.
        discussion: Long-form description of the rule and why it exists.
        references: NIST / DISA references to identify the rule as it relates
            to other organizational standards.
        platforms: A representation of the platform-specific information, such
            as how to check for compliance on a particular platform.
        tags: A list of identifiers that can be used to categorize the rule.
    """

    rule_id: str = Field(alias="id", serialization_alias="id")
    title: str
    discussion: str
    references: References
    platforms: Dict[str, Platform]
    tags: List[str] = []

    def __eq__(self, object) -> bool:
        if not isinstance(object, Rule):
            raise NotImplementedError
        else:
            return self.rule_id == object.rule_id

    def __str__(self) -> str:
        return self.rule_id


if __name__ == "__main__":
    from admin_utils.mobile_validator import validate

    validate(Rule)
