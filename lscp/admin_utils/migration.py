"""Migrate from previous development rule formats to the current.

This module assists with the process of migrating rules from older formats into
newer formats. This script is unlikely to see more updating, as this project's
rules are now following mSCP syntax, but this script was used to convert to
mSCP and is preserved for documentation purposes.

Calling syntax (run from lscp dir): `python[3] -m admin_utils.migration --help`
"""

import argparse
from pathlib import Path
from typing import Dict

import yaml
from classes.rule import (
    Benchmark,
    CheckInfo,
    CheckResult,
    EnforcementInfo,
    FixInfo,
    Platform,
    References,
    Rule,
    Version,
)


def handle_enforcement(enforcement_block: dict) -> EnforcementInfo:
    if (
        "enforcement_type" in enforcement_block.keys()
        and enforcement_block["enforcement_type"] != "full"
    ):
        raise ValueError("This function will only handle complete blocks")

    check_shell = enforcement_block["check"]["shell"]
    exit_code: int | None = None
    string_result: str | None = None
    integer_result: int | None = None
    boolean_result: bool | None = None
    check_block = enforcement_block["check"]
    if "status_code" in check_block.keys():
        exit_code = check_block["status_code"]
    else:
        standard_out = (
            check_block["standard_output"]
            if "standard_output" in check_block.keys()
            else (
                check_block["standard_out"]
                if "standard_out" in check_block.keys()
                else check_block["expected_output"]
            )
        )
        if type(standard_out) == int:
            integer_result = standard_out
        elif type(standard_out) == str:
            string_result = standard_out
        elif type(standard_out) == bool:
            boolean_result = standard_out

    fix_shell = ""
    have_fix = "fix" in enforcement_block.keys()
    if have_fix:
        fix_shell = enforcement_block["fix"]["shell"]
    return EnforcementInfo(
        check=CheckInfo(
            shell=check_shell,
            result=CheckResult(
                string=string_result,
                integer=integer_result,
                boolean=boolean_result,
                exit_code=exit_code,
            ),
        ),
        fix=FixInfo(shell=fix_shell) if have_fix else None,
    )


def handle_version(
    platform: dict, enforcement_info: EnforcementInfo | None = None
) -> Dict[str, Version]:
    _, version = tuple(platform["name"].split("_"))
    if version == "2204":
        version = 22.04
    elif version == "2404":
        version = 24.04
    elif version == "2004":
        version = 20.04

    new_enforcement: EnforcementInfo | None = None
    if enforcement_info is None:
        try:
            new_enforcement = handle_enforcement(platform["enforcement_info"])
        except ValueError:
            pass
    return {
        str(version): Version(
            benchmarks=[
                Benchmark.model_validate(entry) for entry in platform["benchmarks"]
            ],
            enforcement_info=new_enforcement,
        )
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rule Migrator")
    parser.add_argument("rules", nargs="+")
    args = parser.parse_args()

    for rule in args.rules:
        with open(rule, "r") as f:
            data = yaml.safe_load(f)

            new_references = References.model_validate(data["references"])
            cce_data = {}
            nist800_data = new_references.nist["800-53r5"]
            new_disa_stig = {}
            for key, value in new_references.disa["disa_stig"].items():
                new_key = key.replace("04", "")
                cce_data[new_key] = ["CCE-XXXXX-X"]
                new_disa_stig[new_key] = value
            new_references.disa["disa_stig"] = new_disa_stig
            new_references.nist = {"cce": cce_data, "800-53r5": nist800_data}

            high_enforcement: EnforcementInfo | None = None
            if "enforcement_info" in data.keys():
                try:
                    high_enforcement = handle_enforcement(data["enforcement_info"])
                except ValueError:
                    pass

            version_dict: Dict[str, Version] = {}
            for platform in data["platforms"]:
                version_dict.update(handle_version(platform, high_enforcement))

            new_platform = Platform(
                enforcement_info=high_enforcement, versions=version_dict
            )

            new_rule = Rule(
                id=data["id"],
                title=data["title"],
                discussion=data["discussion"],
                references=new_references,
                platforms={"ubuntu": new_platform},
                tags=data["tags"],
            )

            file_name = Path(rule).name

            with open(f"../build/rules/{file_name}", "w+") as f:
                yaml.safe_dump(
                    new_rule.model_dump(exclude_none=True, by_alias=True),
                    f,
                    sort_keys=False,
                )
