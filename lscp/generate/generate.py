from abc import ABC, abstractmethod
from typing import List, Literal, Type

from classes import Baseline, Rule


class BaseGenerator(ABC):
    @property
    @abstractmethod
    def generation_type(self) -> Literal["shell", "pdf", "html"]:
        pass

    @abstractmethod
    def generate(
        self, baseline: Baseline, rules: List[Rule], output_dir: str | None = None
    ) -> None:
        pass


class GeneratorEngine:
    def __init__(self) -> None:
        self._generators: List[Type[BaseGenerator]] = []

    def register_generator(self, cls: Type[BaseGenerator]) -> None:
        if cls not in self._generators:
            self._generators.append(cls)

    def generate(
        self,
        generation_type: List[str],
        baseline: Baseline,
        rules: List[Rule],
        output_dir: str | None = None,
    ) -> None:
        for gen_type in generation_type:
            generator_lst = [
                generator()
                for generator in self._generators
                if generator().generation_type == gen_type
            ]
            if len(generator_lst) == 0:
                raise ValueError(f"No formatter found for {gen_type}")

            for generator in generator_lst:
                generator.generate(baseline, rules, output_dir=output_dir)
