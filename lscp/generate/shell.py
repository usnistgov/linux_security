from os.path import join
from typing import Literal

from classes.baseline import Baseline
from classes.templates import baseline_to_template
from jinja2 import Environment, FileSystemLoader
from utils.directories import get_build_path, get_data_path

from .generate import BaseGenerator


class ShellGenerator(BaseGenerator):
    @property
    def generation_type(self) -> Literal["shell", "pdf", "html"]:
        return "shell"

    def generate(self, baseline: Baseline, output_dir: str | None = None) -> None:
        env = Environment(loader=FileSystemLoader(get_data_path("templates", "shell")))
        template = env.get_template("compliance.sh.jinja")

        baseline_id = baseline.title.split(" ")[-1]

        render_out = (
            template.render(
                baseline=baseline_to_template(baseline),
                baseline_name=baseline.title.split(" ")[-1],
                rule_count=len(
                    [
                        rule.rule_id
                        for section in baseline.profile
                        for rule in section.rules
                    ]
                ),
            ).strip()
            + "\n"
        )

        new_output_dir = (
            output_dir
            if output_dir
            else get_build_path(
                f"{baseline_id}_{baseline.platform.os}_{baseline.platform.version}"
            )
        )

        with open(join(new_output_dir, "compliance.sh"), "w+", newline="\n") as f:
            f.write(render_out)
