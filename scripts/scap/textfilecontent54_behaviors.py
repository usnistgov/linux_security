from dataclasses import dataclass, field

from scap.file_behaviors_1 import FileBehaviors1

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Textfilecontent54Behaviors(FileBehaviors1):
    """The Textfilecontent54Behaviors complex type defines a number of behaviors
    that allow a more detailed definition of the textfilecontent54_object being
    specified.

    Note that using these behaviors may result in some unique results.
    For example, a double negative type condition might be created where
    an object entity says include everything except a specific item, but
    a behavior is used that might then add that item back in. It is
    important to note that the 'max_depth' and 'recurse_direction'
    attributes of the 'behaviors' element do not apply to the 'filepath'
    element, only to the 'path' and 'filename' elements.  This is
    because the 'filepath' element represents an absolute path to a
    particular file and it is not possible to recurse over a file. The
    Textfilecontent54Behaviors extend the ind-def:FileBehaviors and
    therefore include the behaviors defined by that type.

    :ivar ignore_case: 'ignore_case' indicates whether case should be
        considered when matching system values against the regular
        expression provided by the pattern entity. This behavior is
        intended to align with the Perl regular expression 'i' modifier:
        if true, case will be ignored.  If false, case will not be
        ignored. The default is false.
    :ivar multiline: 'multiline' enables multiple line semantics in the
        regular expression provided by the pattern entity. This behavior
        is intended to align with the Perl regular expression 'm'
        modifier: if true, the '^' and '$' metacharacters will match
        both at the beginning/end of a string, and immediately
        after/before newline characters.  If false, they will match only
        at the beginning/end of a string.  The default is true.
    :ivar singleline: 'singleline' enables single line semantics in the
        regular expression provided by the pattern entity. This behavior
        is intended to align with the Perl regular expression 's'
        modifier: if true, the '.' metacharacter will match newlines. If
        false, it will not.  The default is false.
    """

    ignore_case: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    multiline: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    singleline: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
