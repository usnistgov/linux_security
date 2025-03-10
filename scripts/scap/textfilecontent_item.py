from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_windows_view_type import EntityItemWindowsViewType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class TextfilecontentItem:
    """
    The textfilecontent_item looks at the contents of a text file (aka a
    configuration file) by looking at individual lines.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of the file
        (without the path) that is being represented.
    :ivar pattern: The pattern entity represents a regular expression
        that is used to define a block of text.  Subexpression notation
        (parenthesis) is used to call out a value(s) to test against.
        For example, the pattern abc(.*)xyz would look for a block of
        text in the file that starts with abc and ends with xyz, with
        the subexpression being all the characters that exist inbetween.
        Note that if the pattern can match more than one block of text
        starting at the same point, then it matches the longest.
        Subexpressions also match the longest possible substrings,
        subject to the constraint that the whole match be as long as
        possible, with subexpressions starting earlier in the pattern
        taking priority over ones starting later.
    :ivar instance: The instance entity calls out which match of the
        pattern is being represented by this item.  The first match is
        given an instance value of 1, the second match is given an
        instance value of 2, and so on.  The main purpose of this entity
        is too provide uniqueness for different textfilecontent_items
        that results from multiple matches of a given pattern against
        the same file.
    :ivar line: The line element represents a line in the file and is
        represented using a regular expression.
    :ivar text: The text entity represents the block of text that
        matched the specified pattern.
    :ivar subexpression: The subexpression entity represents the value
        of a subexpression in the specified pattern.  If multiple
        subexpressions are specified in the pattern, then multiple
        entities are presented.  Note that the textfilecontent_state in
        the definition schema only allows a single subexpression entity.
        This means that the test will check that all (or at least one,
        none, etc.) the subexpressions pass the same check.  This means
        that the order of multiple subexpression entities in the item
        does not matter.
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "textfilecontent_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    instance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    line: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    subexpression: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
