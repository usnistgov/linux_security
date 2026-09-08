"""Verify all the supplied attributes are accounted for within the rules.

This module is useful for checking references. By supplying the search path, we
can go through every rule and check if a reference is present. If a reference
cannot be identified in any rule, it will return "NOT FOUND".

Calling syntax (run from lscp dir): `python[3] -m admin_utils.attribute_search --help`
"""

import argparse
import re

from classes.rule import Rule
from utils.data_search import get_rule_from_string


# This function is AI-generated
def get_nested(obj: Rule, path: str, default=[]):
    # Split path by dots, brackets, and quotes into distinct keys
    tokens = re.findall(r"[^\.\[\]\'\"]+", path)

    current = obj
    for token in tokens:
        # Try dictionary key lookup
        if isinstance(current, dict) and token in current:
            current = current[token]
        # Try object attribute lookup (Pydantic models, standard classes)
        elif hasattr(current, token):
            current = getattr(current, token)
        # Try list/tuple numeric index lookup
        elif isinstance(current, (list, tuple)) and token.isdigit():
            idx = int(token)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                return default
        else:
            return default
    return current


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rule Search")
    parser.add_argument("-t", dest="search_key", help="Key to search for. Format like Python, for example: references.disa['disa_stig']")
    parser.add_argument("value", nargs="+", help="Value to match for")
    args = parser.parse_args()

    all_rules = get_rule_from_string()

    for value in args.value:
        search_res = [
            rule for rule in all_rules if value in get_nested(rule, args.search_key)
        ]

        if len(search_res) > 0:
            print(f"{value} in {search_res[0].rule_id}")
        else:
            print(f"{value} NOT FOUND")
