from typing import List

from classes.baseline import BaselinePlatform, Section
from classes.rule import EnforcementInfo, Rule

SECTION_REFERENCES = {
    "audit": "Auditing",
    "auth": "Authentication",
    "os": "Operating System",
    "pwpolicy": "Password Policies",
    "ssh": "Secure Shell",
    "services": "Services",
    "networking": "Networking",
}


def get_enforcement_block(
    rule: Rule, platform: BaselinePlatform
) -> EnforcementInfo | None:
    if platform.os not in rule.platforms.keys():
        raise ValueError(
            f"Rule {rule.rule_id} does not support the supplied platform, {platform.os}"
        )
    if str(platform.version) not in rule.platforms[platform.os].versions.keys():
        raise ValueError(
            f"Rule {rule.rule_id} does not support the supplied platform, {platform.os}"
        )

    rule_platform = rule.platforms[platform.os]
    rule_platform_version = rule_platform.versions[str(platform.version)]

    enforcement_block = rule_platform.enforcement_info
    if rule_platform_version.enforcement_info:
        enforcement_block = rule_platform_version.enforcement_info

    return enforcement_block


def compute_sections(rules: List[Rule]) -> List[Section]:
    section_lst: List[Section] = []

    for rule in rules:
        section_id = rule.rule_id.split("_")[0]

        section_name = SECTION_REFERENCES.get(section_id, "Uncategorized")

        filtered_section_lst = [
            section for section in section_lst if section.section == section_name
        ]
        if len(filtered_section_lst) == 0:
            section_lst.append(Section(section=section_name, rules=[rule]))
        else:
            existing_section = filtered_section_lst[0]
            existing_section.rules.append(rule)

    return sorted(section_lst, key=lambda section: section.section)
