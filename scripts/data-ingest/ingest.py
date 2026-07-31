"""Primary loader for ingest modules

This file loads ingestors and runs their specified functions. All modules use
the RuleIngest base class and can be modified from there.
"""

from ingestors.stigs import STIGIngestor
from ingest_types import RuleIngestEngine, IngestInput
from ingest_types.rule_types import yaml_rule_representer, Rule
import os
from pathlib import Path
from typing import List
import yaml
from dataclasses import dataclass


@dataclass
class InputFileType:
    type: str
    files: List[IngestInput]


if __name__ == "__main__":
    yaml.add_representer(Rule, yaml_rule_representer, yaml.SafeDumper)

    engine = RuleIngestEngine(development=True)
    engine.register_parser(STIGIngestor)

    files: List[InputFileType] = []
    input_dirs = [
        name
        for name in os.listdir("input")
        if os.path.isdir(os.path.join("input", name))
    ]
    for dir in input_dirs:
        file_type = InputFileType(dir, [])
        input_files = os.listdir(os.path.join("input", dir))
        for file in input_files:
            file_name = Path(file).stem
            with open(os.path.join("input", dir, file), "r") as f:
                file_type.files.append(IngestInput(file_name, f.read()))
        files.append(file_type)

    rules: list[Rule] = []
    for categories in files:
        rules += engine.process_input(categories.type, categories.files)

    # print(rules)
    for rule in rules:
        yaml_dump = yaml.safe_dump(rule, sort_keys=False)
        with open(f"rules/{rule.rule_id}.yaml", "w+") as f:
            f.write(yaml_dump)
