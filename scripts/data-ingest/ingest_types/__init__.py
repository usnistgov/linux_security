"""Python dataclasses used for ingesting data

These classes are mostly used for formatting a "rule" YAML, while also providing some
helper functions to make parsing easier. This module also has the base function for
ingesting.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Literal, Type
from .rule_types import Rule


@dataclass
class IngestInput:
    name: str
    contents: str


class RuleIngestor(ABC):

    @abstractmethod
    def supported_file(self, file_type: str) -> bool:

        pass

    @abstractmethod
    def parse(
        self, contents: List[IngestInput], development: bool = False
    ) -> List[Rule]:

        pass


class RuleIngestEngine:
    def __init__(self, development: bool = False) -> None:
        self._format_classes: List[Type[RuleIngestor]] = []
        self.development = development

    def register_parser(self, cls: Type[RuleIngestor]) -> None:
        if cls not in self._format_classes:
            self._format_classes.append(cls)

    def process_input(self, input_type: str, input: List[IngestInput]) -> List[Rule]:
        for formatter in self._format_classes:
            formatter_cls = formatter()
            if formatter_cls.supported_file(input_type):
                return formatter_cls.parse(input, development=self.development)
        raise ValueError("No formatter found for file type")
