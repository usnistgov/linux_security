import yaml
import argparse
from typing import List
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader


def platform_pretty_print(platform: str) -> str:
    match platform:
        case "ubuntu_2204":
            return "Ubuntu 22.04 LTS"
        case "ubuntu_2404":
            return "Ubuntu 24.04 LTS"
        case "ubuntu_2004":
            return "Ubuntu 20.04 LTS"
        case "rhel_8":
            return "Red Hat Enterprise Linux 8"
        case "rhel_9":
            return "Red Hat Enterprise Linux 9"
        case "rhel_10":
            return "Red Hat Enterprise Linux 10"
        case _:
            return "Generic"


@dataclass
class RuleInfo:
    rule_id: str
    tags: List[str]
    title: str
    description: str
    nist_80053_controls: List[str]
    check: str
    expected_result: str
    fix: str


def main() -> None:
    parser = argparse.ArgumentParser(description="Compliance-sh Generator")
    parser.add_argument(
        "-P",
        "--platform",
        required=True,
        choices=[
            "ubuntu_2204",
            "ubuntu_2404",
            "ubuntu_2004",
            "rhel_8",
            "rhel_9",
            "rhel_10",
        ],
        type=str,
        nargs=1,
        help="Specifies the platform to compile the script for",
    )
    parser.add_argument(
        "rules", type=str, nargs="+", help="The list of rule files to use"
    )
    args = parser.parse_args()

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("compliance.sh.jinja")

    rule_info_lst: List[RuleInfo] = []

    for files in args.rules:
        with open(files, "r") as f:
            rule = yaml.safe_load(f.read())

        platform_lst = [
            platform
            for platform in rule["platforms"]
            if platform["name"] == args.platform[0]
        ]
        if len(platform_lst) == 0:
            print(
                f'The following rule did not have "{args.platform[0]}" as a platform: {rule["id"]}'
            )
            continue

        platform_info = platform_lst[0]

        rule_info = RuleInfo(
            rule_id=rule["id"],
            tags=rule["tags"],
            title=rule["title"],
            description=rule["discussion"],
            nist_80053_controls=rule["references"]["nist"]["800-53r5"],
            check=platform_info["enforcement_info"]["check"]["shell"],
            expected_result=platform_info["enforcement_info"]["check"][
                "expected_output"
            ],
            fix=platform_info["enforcement_info"]["fix"]["shell"],
        )
        rule_info_lst.append(rule_info)

    out = (
        template.render(
            platform=platform_pretty_print(args.platform[0]), rules=rule_info_lst
        ).strip()
        + "\n"
    )

    with open("output/compliance.sh", "w+", newline="\n") as f:
        f.write(out)


if __name__ == "__main__":
    main()
