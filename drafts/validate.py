from typing import List, Any, Self, Literal
from enum import Enum
import yaml
import argparse
import sys

from pydantic import BaseModel, model_validator


class References(BaseModel):
    nist: dict[Literal["800-53r5", "800-171r3", "cce"], Any]
    disa: dict[Literal["cci", "srg", "disa_stig"], Any]


class EnforcementType(str, Enum):
    full = "full"
    vars = "vars"
    inherit = "inherit"
    blank = "blank"


class CheckInfo(BaseModel):
    shell: str
    standard_output: str | None = None
    status_code: int | None = None

    @model_validator(mode="after")
    def only_one_output(self) -> Self:
        if self.standard_output is not None == self.status_code is not None:
            raise ValueError(
                "Only standard output or command output should be specified, and not both."
            )
        return self


class FixInfo(BaseModel):
    shell: str


class EnforcementInfo(BaseModel):
    enforcement_type: EnforcementType
    check: CheckInfo | None = None
    fix: FixInfo | None = None
    vars: dict[str, Any] | None = None

    @model_validator(mode="after")
    def enforce_check(self) -> Self:
        if (
            self.enforcement_type != EnforcementType.inherit
            and self.enforcement_type != EnforcementType.vars
            and self.check is None
        ):
            raise ValueError("A check must be present if not inheriting.")
        return self

    @model_validator(mode="after")
    def ensure_vars(self) -> Self:
        if self.enforcement_type == EnforcementType.vars and (
            self.vars is None or len(self.vars) == 0
        ):
            raise ValueError(
                "The variables list must be present if using the 'vars' enforcement type."
            )
        return self


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Benchmark(BaseModel):
    name: str
    severity: Severity | None = None


class Platform(BaseModel):
    name: str
    benchmarks: List[Benchmark]
    enforcement_info: EnforcementInfo


class Rule(BaseModel):
    id: str
    title: str
    discussion: str
    references: References
    enforcement_info: EnforcementInfo
    platforms: List[Platform]
    tags: List[str] = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rule Validator")
    parser.add_argument("rules", nargs="+")
    args = parser.parse_args()

    for file in args.rules:
        with open(file, "r") as rule_file:
            yaml_load = yaml.safe_load(rule_file)
            try:
                Rule.model_validate(yaml_load)
            except ValueError as e:
                print(e, file=sys.stderr)
                print(f"{yaml_load["id"]} failed")
                continue
            print(f"{yaml_load["id"]} passed")
