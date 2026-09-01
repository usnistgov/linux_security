import argparse
from typing import List

import yaml
from classes.baseline import Baseline, BaselinePlatform, Section
from classes.rule import Rule
from generate import GeneratorEngine
from generate.shell import ShellGenerator
from utils.data_search import get_rule_from_string
from utils.directories import get_custom_path
from utils.rules import compute_sections

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Linux Security Compliance Project (LSCP) Manager"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    guidance = subparsers.add_parser("guidance")
    guidance.add_argument(
        "baseline",
        help="baseline YAML file used to create the guidance documents",
    )
    guidance.add_argument(
        "-A",
        "--all",
        action="store_true",
        default=False,
        help="generate documentation and all support files for the rules in the specified baseline",
    )
    guidance.add_argument(
        "-s",
        "--script",
        action="store_true",
        default=False,
        help="generate the compliance script for the rules in the specified baseline",
    )
    guidance.add_argument(
        "--no-docs",
        default=False,
        dest="no_docs",
        action="store_true",
        help="skip generating the PDF and HTML documents",
    )

    baseline = subparsers.add_parser("baseline")
    baseline.add_argument(
        "keywords",
        nargs="*",
        help="keyword to be used to collect associated rules",
    )
    baseline.add_argument(
        "-l",
        "--list_tags",
        default=False,
        action="store_true",
        help="list the available keywords that can be used to generate a baseline YAML file",
    )

    args = parser.parse_args()

    if args.command == "guidance":
        rules: List[Rule] = []
        baseline_data: Baseline
        with open(args.baseline, "r") as file:
            baseline_yaml = yaml.safe_load(file)
            baseline_data = Baseline.model_validate(baseline_yaml)

        # generate_files = ["pdf", "html"]
        generate_files = []
        if args.all:
            generate_files.append("shell")
        else:
            if args.no_docs:
                generate_files = []
            if args.script:
                generate_files.append("shell")

        engine = GeneratorEngine()
        engine.register_generator(ShellGenerator)
        engine.generate(generate_files, baseline_data)

    elif args.command == "baseline":
        all_rules: List[Rule]
        if args.list_tags or len(args.keywords) == 1:
            all_rules = get_rule_from_string()
        else:
            parser.error("Keywords must contain a value, or -l should be passed.")

        if args.list_tags:
            tags: List[str] = [tag for rule in all_rules for tag in rule.tags]
            tags = list(set(tags))
            print("Available Tags:\n")
            for tag in tags:
                print(tag)
        else:
            new_rules = [
                rule for rule in all_rules for tag in rule.tags if tag in args.keywords
            ]

            default_platform = BaselinePlatform(os="ubuntu", version=22.04)

            new_baseline = Baseline(
                title=f"{default_platform.os} {default_platform.version}: Security Configuration - {args.keywords[0]}",
                parent_values="recommended",
                platform=default_platform,
                profile=compute_sections(new_rules),
            )

            output_path = get_custom_path(
                "baselines",
                f"{args.keywords[0]}_{default_platform.os}_{default_platform.version}.yaml",
            )
            with open(output_path, "w+") as file:
                file.write(
                    yaml.safe_dump(
                        new_baseline.model_dump(exclude_none=True, by_alias=True),
                        sort_keys=False,
                    )
                )

    else:
        parser.print_help()
