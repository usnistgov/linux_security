"""Generic Pydantic validation script.

This module contains a function that can be called by running as __main__ in
the various Pydantic classes used throughout the project.

Calling syntax (run from lscp dir): `python[3] -m classes.rule --help`
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Type

import yaml
from pydantic import BaseModel


def validate(object: Type[BaseModel]) -> None:
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
                path_name = Path(file).name
                with open(file, "r") as rule_file:
                    yaml_load = yaml.safe_load(rule_file)
                    try:
                        obj = object.model_validate(yaml_load)
                    except ValueError as e:
                        print(e, file=sys.stderr)
                        print(f"{path_name} failed")
                        continue
                    print(f"{path_name} passed")

                print(
                    yaml.safe_dump(
                        obj.model_dump(exclude_none=True, by_alias=True),
                        sort_keys=False,
                    ),
                    file=sys.stderr,
                )
        else:
            parser.error("More than one rule must be provided.")
