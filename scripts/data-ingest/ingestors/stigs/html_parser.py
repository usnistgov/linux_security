"""Helper module for the parsing of HTML

This module is responsible for reading the raw HTML and grouping everything into
objects the rest of the program can understand.
"""

from dataclasses import dataclass
from bs4 import Tag
from typing import List


@dataclass
class STIG_Header:
    benchmark_name: str
    benchmark_id: str
    release_info: str
    version: int
    group_id: str
    severity: str  # TODO make dataclass
    rule_id: str
    rule_version: str
    # classification: str # Unused?
    # asset_posture: str # Unused?


@dataclass
class STIG_RuleInfo:
    srg_id: str
    title: str
    fix_text: str
    discussion: str
    ccis_unformatted: str
    check_text: str
    check_stig_ref: str
    weight: float
    documentable: bool


@dataclass
class STIGHTML(STIG_Header, STIG_RuleInfo):
    pass


def parse_header_block(header: Tag) -> STIG_Header:
    header_data = header.find_all("div", class_="data")
    if len(header_data) != 10:
        raise ValueError("Header length does not match")

    clean_data: List[str] = []
    for header_info in header_data:
        # All the data is always formatted this way, so it can be done in a cheap way.
        value = header_info.contents[3]
        clean_data.append(value.get_text())

    return STIG_Header(
        benchmark_name=clean_data[0],
        benchmark_id=clean_data[1],
        release_info=clean_data[2],
        version=int(clean_data[3]),
        group_id=clean_data[4],
        severity=clean_data[5],
        rule_id=clean_data[6],
        rule_version=clean_data[7],
    )


def parse_info_block(rule_block: Tag) -> STIG_RuleInfo:
    if len(rule_block.contents) != 18:
        raise ValueError("Info length does not match")

    return STIG_RuleInfo(
        srg_id=rule_block.contents[1].get_text(),
        title=rule_block.contents[3].get_text(),
        fix_text=rule_block.contents[5].get_text(),
        discussion=rule_block.contents[7].get_text(),
        ccis_unformatted=rule_block.contents[9].get_text(),
        check_text=rule_block.contents[11].get_text(),
        check_stig_ref=rule_block.contents[13].get_text(),
        weight=float(rule_block.contents[15].get_text()),
        documentable=True if rule_block.contents[17].get_text() != "false" else False,
    )
