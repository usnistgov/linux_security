from enum import Enum
from typing import Any, List, Literal, Self

from pydantic import BaseModel, field_serializer, field_validator, model_validator
from utils.mobile_validator import validate

from .platforms import SupportedPlatform


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
    vars: dict[str, str] | None = None

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
    name: SupportedPlatform
    benchmarks: List[Benchmark]
    enforcement_info: EnforcementInfo

    @field_validator("name", mode="before")
    @classmethod
    def validate_platform(cls, platform: str):
        return SupportedPlatform[platform]

    @field_serializer("name")
    def serialize_platform(self, platform: SupportedPlatform):
        return platform.name


class Rule(BaseModel):
    id: str
    title: str
    discussion: str
    references: References
    enforcement_info: EnforcementInfo
    platforms: List[Platform]
    tags: List[str] = []

    def __eq__(self, object) -> bool:
        if not isinstance(object, Rule):
            raise NotImplementedError
        else:
            return self.id == object.id


if __name__ == "__main__":
    validate(Rule)
