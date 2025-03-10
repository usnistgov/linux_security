from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_string_type import EntityObjectStringType
from scap.file_behaviors_1 import FileBehaviors1
from scap.object_type_2 import ObjectType2
from scap.set import Set

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class TextfilecontentObject(ObjectType2):
    """The textfilecontent_object element is used by a text file content test to
    define the specific line(s) of a file(s) to be evaluated.

    The textfilecontent_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema.

    :ivar set:
    :ivar behaviors:
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar line: The line element represents a line in the file and is
        represented using a regular expression. A single subexpression
        can be called out using parentheses. The value of this
        subexpression can then be checked using a textfilecontent_state.
        Note that when using regular expressions, OVAL supports a common
        subset of the regular expression character classes, operations,
        expressions and other lexical tokens defined within Perl 5's
        regular expression specification. For more information on the
        supported regular expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html.
    """

    class Meta:
        name = "textfilecontent_object"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    behaviors: Optional[FileBehaviors1] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    line: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
