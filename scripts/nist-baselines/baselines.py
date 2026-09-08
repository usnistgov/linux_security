import argparse
from pathlib import Path
from typing import List

import requests
import yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NIST Baselines")
    parser.add_argument("rules", nargs="+")
    args = parser.parse_args()

    stored_requests: dict[str, str] = {}

    for file in args.rules:
        with open(file, "r") as rule_file:
            data = yaml.safe_load(rule_file)
            applicable_results: List[str] = []

        controls: List[str] = data["references"]["nist"]["800-53r5"]
        new_controls_list: List[str] = []

        for control in controls:
            submit_str = ""
            control_split = control.split(" ")
            num_added = False
            for section in control_split:
                if "-" in section:
                    section_lst = section.split("-")
                    num = section_lst[1]
                    num_int = int(num)
                    submit_str += f"{section_lst[0]}-{num_int:02d}"
                elif "(" in section and ")" in section and not num_added:
                    num = section.replace("(", "").replace(")", "")
                    try:
                        num_int = int(num)
                    except ValueError:
                        continue
                    num_added = True
                    submit_str += f"({num_int:02d})"

            new_controls_list.append(submit_str)

            prior_requests = [
                value for key, value in stored_requests.items() if key == submit_str
            ]
            if len(prior_requests) > 0:
                applicable_results.append(prior_requests[0])
            else:
                req_data = requests.get(
                    f"https://controlfreak.risk-redux.io/controls/{submit_str}.json"
                ).json()
                if req_data["control"]["is_low"]:
                    applicable_results.append("low")
                    stored_requests[submit_str] = "low"
                elif req_data["control"]["is_moderate"]:
                    applicable_results.append("moderate")
                    stored_requests[submit_str] = "moderate"
                elif req_data["control"]["is_high"]:
                    applicable_results.append("high")
                    stored_requests[submit_str] = "high"
                else:
                    stored_requests[submit_str] = "NONE"
            print(
                "{:<15}{:<10}{:<50}".format(
                    submit_str, stored_requests[submit_str], data["id"]
                )
            )

        if "low" in applicable_results:
            data["tags"] = ["800-53r5_low", "800-53r5_moderate", "800-53r5_high"]
        elif "moderate" in applicable_results:
            data["tags"] = ["800-53r5_moderate", "800-53r5_high"]
        elif "high" in applicable_results:
            data["tags"] = ["800-53r5_high"]

        data["references"]["nist"]["800-53r5"] = new_controls_list

        file_name = Path(file).name
        with open(f"output/{file_name}", "w+") as f:
            yaml.safe_dump(data, f, sort_keys=False)
