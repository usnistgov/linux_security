from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.entity_state_windows_view_type import EntityStateWindowsViewType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Textfilecontent54State(StateType):
    """
    The textfilecontent54_state element contains entities that are used to check
    the file path and name, as well as the text block in question and the value of
    the subexpressions.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename entity represents the name of a file.
    :ivar pattern: The pattern entity represents a regular expression
        that is used to define a block of text.
    :ivar instance: The instance entity calls out a specific match of
        the pattern. This can only be a positive integer.
    :ivar text: The text entity represents the block of text that
        matched the specified pattern.
    :ivar subexpression: The subexpression entity represents a value to
        test against the subexpression in the specified pattern. If
        multiple subexpressions are specified in the pattern, this value
        is tested against all of them. For example, if the pattern
        abc(.*)mno(.*)xyp was supplied, and the state specifies a
        subexpression value of enabled, then the test would check that
        both (or at least one, none, etc. depending on the entity_check
        attribute) of the subexpressions have a value of enabled.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    def generate_check(self, data):
        print(f"TextFileContent54 State! {self.id}")

    class Meta:
        name = "textfilecontent54_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pattern: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    instance: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    text: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    subexpression: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
