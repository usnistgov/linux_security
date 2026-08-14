from os.path import join
from typing import List, Literal

from classes import Baseline, Rule
from jinja2 import Environment, FileSystemLoader
from utils.dir_utils import get_build_output, get_data_path
from utils.rules import get_enforcement_block

from .generate import BaseGenerator


class ShellGenerator(BaseGenerator):
    @property
    def generation_type(self) -> Literal["shell", "pdf", "html"]:
        return "shell"

    def generate(
        self, baseline: Baseline, rules: List[Rule], output_dir: str | None = None
    ) -> None:
        env = Environment(loader=FileSystemLoader(get_data_path("templates", "shell")))
        template = env.get_template("compliance.sh.jinja")

        platform = baseline.platform
        rule_lst: List[Rule] = []

        for rule in rules:
            enforcement_block = get_enforcement_block(rule, platform)
            new_rule = rule.model_copy()
            new_rule.enforcement_info = enforcement_block
            rule_lst.append(new_rule)

        render_out = (
            template.render(platform=platform.value, rules=rule_lst).strip() + "\n"
        )

        new_output_dir = output_dir if output_dir else get_build_output()

        with open(join(new_output_dir, "compliance.sh"), "w+", newline="\n") as f:
            f.write(render_out)
