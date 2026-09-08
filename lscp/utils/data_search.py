from pathlib import Path
from typing import List

import yaml
from classes.rule import Rule
from utils.directories import get_custom_path, get_data_path


def get_rule_from_string(rule_name: str | None = None) -> List[Rule]:
    glob_search = "*.yaml"
    rules: List[Rule] = []
    if rule_name:
        glob_search = f"*{rule_name}.yaml"

    rule_files = get_data_path("rules")
    rule_path = Path(rule_files)

    custom_files = get_custom_path("rules")
    custom_path = Path(custom_files)

    search_results = list(rule_path.rglob(glob_search))

    if len(search_results) == 0 or rule_name is None:
        search_results += list(custom_path.rglob(glob_search))

    if len(search_results) == 0:
        raise NameError("Could not find rule name in data rules paths", name=rule_name)

    for found_yaml in search_results:
        with open(found_yaml, "r") as file:
            yaml_file = yaml.safe_load(file)
            rules.append(Rule.model_validate(yaml_file))
    return rules
