from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

@dataclass
class ComponentType:
    def evaluate_component(self,data):
        print("Base component evaluation should not occur.")