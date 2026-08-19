"""Classes responsible for mSCP mapping

In the mSCP project, the "Rule" class contains the information necessary for
the template engines to format everything appropriately. As such, when YAML
files get read, they get read as the class for the template engine. This
project isn't doing that. Instead, the YAML is put into its matching
Pydantic class: a class that generally matches the YAML one for one, outside of
minor tweaks to formatting.

To allow ourselves the opportunity to copy the templates into the mSCP project,
the templates should use the same sorts of variables mSCP has access to. As
such, these classes exist to map Pydantic rule files to template variables.
"""

from pathlib import Path
from typing import List

from utils.rules import get_enforcement_block

from .baseline import Baseline, Section
from .rule import Rule


class TemplateRules(Rule):
    result_value: str | int | bool | None = None
    exit_code: int | None = None
    section: str | None
    os_name: str
    os_type: str
    os_version: str | float
    check: str | None = None
    fix: str | None = None
    severity: str | None = None
    source_file: Path | None = None


class TemplateSection(Section):
    rules: List[TemplateRules]  # type: ignore


class TemplateBaseline(Baseline):
    profile: List[TemplateSection]  # type: ignore


def baseline_to_template(baseline: Baseline) -> TemplateBaseline:
    list_of_new_sections: List[TemplateSection] = []
    for section in baseline.profile:
        new_rules: List[TemplateRules] = []
        for rule in section.rules:
            result_value = None
            exit_code = None
            new_section = section.section
            new_check = None
            new_fix = None
            enforcement = get_enforcement_block(rule, baseline.platform)
            if enforcement:
                if enforcement.check and enforcement.check.result:
                    new_check = enforcement.check.shell
                    if enforcement.check.result.exit_code is not None:
                        exit_code = enforcement.check.result.exit_code
                    else:
                        dmp = enforcement.check.result.model_dump()
                        values = list(dmp.values())
                        result_value = [value for value in values if value is not None][
                            0
                        ]
                if enforcement.fix:
                    new_fix = enforcement.fix.shell

            new_rules.append(
                TemplateRules(
                    result_value=result_value,
                    exit_code=exit_code,
                    section=new_section,
                    os_name=baseline.platform.os,
                    os_type=baseline.platform.os,
                    os_version=baseline.platform.version,
                    check=new_check,
                    fix=new_fix,
                    id=rule.rule_id,
                    title=rule.title,
                    discussion=rule.discussion,
                    references=rule.references,
                    platforms=rule.platforms,
                )
            )

        list_of_new_sections.append(
            TemplateSection(section=section.section, rules=new_rules)
        )
    return TemplateBaseline(
        profile=list_of_new_sections,
        title=baseline.title,
        description=baseline.description,
        authors=baseline.authors,
        parent_values=baseline.parent_values,
        platform=baseline.platform,
    )
