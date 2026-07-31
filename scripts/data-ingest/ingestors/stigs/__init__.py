"""DISA STIG ingestor

This module works with specifically the HTML export result from the official DISA STIG
viewer (3.7.0).
"""

from typing import List
from dataclasses import asdict
import re
from random import shuffle

from bs4 import BeautifulSoup
from llm_hook import LLMConnection
from ingest_types import RuleIngestor, IngestInput
from ingest_types.rule_types import Rule, Benchmark, Platform, EnforcementInfo
from .prompts import (
    CHECK_CMD_PROMPT,
    FIX_CMD_PROMPT,
    GENERATE_ID_PROMPT,
    GENERATE_DESCRIPTION_PROMPT,
)
from .html_parser import parse_header_block, parse_info_block, STIGHTML


class STIGIngestor(RuleIngestor):
    def supported_file(self, file_type: str) -> bool:
        return file_type == "stig_html"

    def parse(
        self, contents: List[IngestInput], development: bool = False
    ) -> List[Rule]:
        stig_rules: List[Rule] = []
        for stig in contents:
            soup = BeautifulSoup(stig.contents, "html.parser")

            rule_blocks = soup.find_all("div", class_="rule")

            # The development flag randomly shuffles and collects 5 rules.
            # This makes it so testing doesn't take forever.
            if development:
                shuffle(rule_blocks)
                rule_blocks = rule_blocks[:5]
                # rule_blocks = [
                #     block
                #     for block in rule_blocks
                #     if "timesyncd" in block.decode_contents()
                # ]

            for rule in rule_blocks:
                header_html = rule.find("div", class_="header")
                rule_html = rule.find("div", class_="rule_info")
                if not header_html or not rule_html:
                    raise ValueError(
                        "These files are not the expected STIG HTML files."
                    )

                header = parse_header_block(header_html)
                rule_info = parse_info_block(rule_html)
                data = STIGHTML(**asdict(header), **asdict(rule_info))

                llm = LLMConnection()
                description_llm = llm.send_message(
                    GENERATE_DESCRIPTION_PROMPT, data.discussion
                )
                check_llm = llm.send_message(CHECK_CMD_PROMPT, data.check_text)
                fix_llm = llm.send_message(FIX_CMD_PROMPT, data.fix_text)
                id_llm = llm.send_message(
                    GENERATE_ID_PROMPT, f"{data.title}\n\n{data.discussion}"
                )

                possible_id = id_llm.response if id_llm.response else data.group_id
                new_description = (
                    description_llm.response
                    if description_llm.response
                    else data.discussion
                )

                if check_llm.response == None or fix_llm.response == None:
                    raise ValueError("The LLM failed to generate a response.")

                result_re = re.search(
                    "LLM_RESULT:( .*$)",
                    check_llm.response,
                    flags=re.MULTILINE | re.IGNORECASE,
                )
                if result_re == None:
                    raise ValueError("The LLM failed to include a specified result.")

                result = result_re.group(1).strip()

                try:
                    result = int(result)
                except ValueError:
                    pass

                check_cmd = re.sub(
                    "LLM_RESULT: .*$",
                    "",
                    check_llm.response,
                    flags=re.MULTILINE | re.IGNORECASE,
                ).strip()

                nist_cn = re.findall(
                    "NIST SP 800-53 Revision 5::(.*$)",
                    data.ccis_unformatted,
                    flags=re.MULTILINE,
                )
                ccis = re.findall("CCI-.*$", data.ccis_unformatted, flags=re.MULTILINE)

                references = {
                    "nist": {
                        "800-53r5": list(set(nist_cn)),
                    },
                    "disa": {
                        "cci": list(set(ccis)),
                        "srg": [data.srg_id],
                        "disa_stig": {stig.name: [data.rule_version]},
                    },
                }

                sample_rule = Rule(
                    rule_id=possible_id,
                    title=data.title,
                    discussion=new_description,
                    references=references,
                    platforms=[
                        Platform(
                            name=stig.name,
                            benchmarks=[Benchmark("disa_stig", data.severity)],
                            enforcement=[
                                EnforcementInfo("check", check_cmd, result),
                                EnforcementInfo("fix", fix_llm.response, ""),
                            ],
                        ),
                    ],
                    tags=["testing"],
                )

                found_existing_rule = False
                for existing_rule in stig_rules:
                    # Since we're using AI generated IDs, it's possible for it to overlap. If it does, give up and add the group ID to the end.
                    if sample_rule.rule_id == existing_rule.rule_id:
                        sample_rule.rule_id += data.group_id

                    if sample_rule == existing_rule:
                        found_existing_rule = True
                        existing_rule.references["disa"]["disa_stig"][stig.name] = [
                            data.rule_version
                        ]
                        if (
                            sample_rule.references["disa"]["srg"][0]
                            not in existing_rule.references["disa"]["srg"]
                        ):
                            existing_rule.references["disa"]["srg"].append(
                                sample_rule.references["disa"]["srg"]
                            )
                        existing_rule.platforms += sample_rule.platforms
                        break

                if not found_existing_rule:
                    stig_rules.append(sample_rule)

        return stig_rules
