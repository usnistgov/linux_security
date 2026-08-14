from pathlib import Path
from typing import List

import yaml
from classes import Rule, SupportedPlatform
from classes.rule import EnforcementInfo, EnforcementType

from .dir_utils import get_data_path


def get_enforcement_block(rule: Rule, platform: SupportedPlatform) -> EnforcementInfo:
    high_level_block = rule.enforcement_info
    current_platform_lst = [
        p_rule for p_rule in rule.platforms if p_rule.name == platform
    ]
    if len(current_platform_lst) == 0:
        raise ValueError(f"Rule {rule.id} does not support platform {platform.name}")

    current_enforcement = current_platform_lst[0].enforcement_info

    if current_enforcement.enforcement_type == EnforcementType.inherit:
        return high_level_block
    elif current_enforcement.enforcement_type == EnforcementType.full:
        return current_enforcement
    elif current_enforcement.enforcement_type == EnforcementType.vars:
        high_level_block.vars = current_enforcement.vars
        return high_level_block
    else:
        raise ValueError('Enforcement type for current platform is null or "blank" ')


def get_rule_from_string(rule_name: str | None = None) -> List[Rule]:
    glob_search = "*.yaml"
    rules: List[Rule] = []
    if rule_name:
        glob_search = f"*{rule_name}.yaml"

    rule_files = get_data_path("rules")
    rule_path = Path(rule_files)

    search_results = list(rule_path.rglob(glob_search))
    if len(search_results) == 0:
        raise NameError("Could not find rule name in data rules paths", name=rule_name)

    for found_yaml in search_results:
        with open(found_yaml, "r") as file:
            yaml_file = yaml.safe_load(file)
            rules.append(Rule.model_validate(yaml_file))

    return rules
