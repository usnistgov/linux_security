from dataclasses import dataclass, field
from typing import Optional

from scap.object_ref_type import ObjectRefType
from scap.state_ref_type import StateRefType
from scap.test_type import TestType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Textfilecontent54Test(TestType):
    """The textfilecontent54_test element is used to check the contents of a text
    file (aka a configuration file) by looking at individual blocks of text.

    It extends the standard TestType as defined in the oval-definitions-
    schema and one should refer to the TestType description for more
    information. The required object element references a
    textfilecontent54_object and the optional state element specifies
    the metadata to check.
    """
    
    def generate_check(self, data):
        print(f"TextFileContent54 Test! {self.id}")
        # Evaluate the object and state refs, pass to them
        #print(self)
        # Evaluate object
        object = data["objects"][self.object_value.object_ref].generate_check(data)
        #print(f"TextFileTest Object: {object}")
        # Evaluate state(s)
        states = []
        for state in self.state:
            states.append(data["states"][state.state_ref].generate_check(data))
        print(f"TextFileTest States: {states}")

    class Meta:
        name = "textfilecontent54_test"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    object_value: Optional[ObjectRefType] = field(
        default=None,
        metadata={
            "name": "object",
            "type": "Element",
            
            "required": True,
        },
    )
    state: list[StateRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
