"""Classes pertaining to compliance baselines.

Like with rules, these baselines are fully compatible with the macOS
Security Compliance Project, and both should be able to resolve each other.
"""

from typing import Any, List

from pydantic import BaseModel, field_serializer, field_validator
from utils.data_search import get_rule_from_string

from .rule import Rule


class Section(BaseModel):
    """Information about a particular section and its associated rules.

    This class contains information about sections, or blocks of rules
    commonly associated with each other. Sections can be outlined as needed
    to better categorize rules, with each section being named in the report.

    Attributes:
        section: The name of the section.
        rules: The list of rules. These should be stored as the IDs of the
            rules, and each rule will be loaded when validating the Pydantic
            class.
    """

    section: str
    rules: List[Rule]

    @field_validator("rules", mode="before")
    @classmethod
    def _define_rules(cls, obj: Any):
        if isinstance(obj, list) and all(isinstance(item, str) for item in obj):
            rule_lst: List[Rule] = []
            for rule_str in obj:
                rule_lst += get_rule_from_string(rule_str)
            return rule_lst
        else:
            return obj

    @field_serializer("rules")
    def _output_rules(self, rules: List[Rule]):
        return [rule.rule_id for rule in rules]


class Author(BaseModel):
    """Author(s) for the specified baseline.

    This class contains information regarding the authors of the baseline. Some
    author data is taken from the program and its authors, but additional
    authors are credited according to who contributed to the construction of
    the rules and baselines.

    Attributes:
        name: The author's name.
        organization: The organization their contributions were completed under.
    """

    name: str
    organization: str


class BaselinePlatform(BaseModel):
    """Outline of the Operating System supported by the baseline.

    This class represents the Operating System and Version targeted in the
    compliance. Generally speaking, the version provided should cover all the
    rules associated with the baseline as to ensure consistency. Despite
    similarities that can commonly occur between versions, each version must
    be tested to ensure reliability, hence why the version is hardcoded and
    attached for every baseline.

    Attributes:
        os: The internal operating system name: "ubuntu" or "redhat".
        version: The OS version, represented in numerical form. For example,
            22.04 or 8. Numerical form is required for compatibility with mSCP.
    """

    os: str
    version: str | float


class Baseline(BaseModel):
    """A series of compliance rules.

    This class represents baselines, which store a series of rules to define
    required compliance rules for a particular system. Most often these rules
    will be tied to a benchmark of some capacity, but they have the flexibility
    to support different configurations. Whatever is needed for a particular
    network or system!

    Attributes:
        title: Human-readable title given to the entire baseline.
        description: Long-form description of what the baseline accomplishes.
        authors: The list of authors associated with designing the baseline.
        parent_values: Currently unused, used for compatibility with mSCP.
        platform: The platform the benchmark validates for.
        profile: A list of sections containing compliance rules.
    """

    title: str
    description: str | None = None
    authors: List[Author] | None = None
    parent_values: str = "recommended"
    platform: BaselinePlatform
    profile: List[Section]


if __name__ == "__main__":
    from admin_utils.mobile_validator import validate

    validate(Baseline)
