from typing import Any
import argparse
import yaml
import json
import sys

def validate(object: Any):
    parser = argparse.ArgumentParser(description="Class Validator")
    parser.add_argument("--schema", action="store_true", help="print JSON schema")
    parser.add_argument("rules", nargs="*")
    args = parser.parse_args()

    if args.schema:
        model_schema = object.model_json_schema()
        print(json.dumps(model_schema, indent=4))
    else:
        if args.rules:
            for file in args.rules:
                with open(file, "r") as rule_file:
                    yaml_load = yaml.safe_load(rule_file)
                    try:
                        object.model_validate(yaml_load)
                    except ValueError as e:
                        print(e, file=sys.stderr)
                        print(f"{yaml_load["id"]} failed")
                        continue
                    print(f"{yaml_load["id"]} passed")
        else:
            parser.error("More than one rule must be provided.")
