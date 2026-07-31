"""Rule-specific dataclasses

Here are dataclasses specifically tied to the rule YAML and its formatting.
"""

from typing import Literal, List, Any
from dataclasses import dataclass
import re

REGEX_TITLE_STRIP = r"Ubuntu \d\d\.\d\d LTS"


@dataclass
class EnforcementInfo:
    type: Literal["check", "fix"]
    shell: str
    expected_output: str | int


@dataclass
class Benchmark:
    name: str
    severity: str


@dataclass
class Platform:
    name: str
    benchmarks: List[Benchmark]
    enforcement: List[EnforcementInfo]


@dataclass
class Rule:
    rule_id: str
    title: str
    discussion: str
    references: dict[str, Any]
    platforms: List[Platform]
    tags: List[str]

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Rule):
            return NotImplemented

        orig_title = re.sub(REGEX_TITLE_STRIP, "", self.title)
        obj_title = re.sub(REGEX_TITLE_STRIP, "", value.title)
        return orig_title == obj_title


def yaml_rule_representer(dumper, data: Rule):
    platforms_dict: List[dict] = []
    for platform in data.platforms:
        platform_dict = {
            "name": platform.name,
            "benchmarks": [],
            "enforcement_info": {},
        }

        for benchmark in platform.benchmarks:
            platform_dict["benchmarks"].append(
                {"name": benchmark.name, "severity": benchmark.severity}
            )

        for enforcement in platform.enforcement:
            platform_dict["enforcement_info"][enforcement.type] = {
                "shell": enforcement.shell
            }

            if enforcement.type == "check":
                platform_dict["enforcement_info"][enforcement.type][
                    "expected_output"
                ] = enforcement.expected_output

        platforms_dict.append(platform_dict)

    return dumper.represent_dict(
        {
            "id": data.rule_id,
            "title": data.title,
            "discussion": data.discussion,
            "references": data.references,
            "platforms": platforms_dict,
            "tags": data.tags,
        }
    )
