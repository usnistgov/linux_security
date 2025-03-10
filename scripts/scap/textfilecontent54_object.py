from dataclasses import dataclass, field
from typing import Optional

from scap.entity_object_int_type import EntityObjectIntType
from scap.entity_object_string_type import EntityObjectStringType
from scap.filter import Filter
from scap.object_type_2 import ObjectType2
from scap.set import Set
from scap.textfilecontent54_behaviors import Textfilecontent54Behaviors

from typing import override

from scap.operation_enumeration import OperationEnumeration

import sys

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class Textfilecontent54Object(ObjectType2):
    """The textfilecontent54_object element is used by a textfilecontent_test to
    define the specific block(s) of text of a file(s) to be evaluated.

    The textfilecontent54_object will only collect regular files on UNIX
    systems and FILE_TYPE_DISK files on Windows systems. Each object
    extends the standard ObjectType as defined in the oval-definitions-
    schema and one should refer to the ObjectType description for more
    information. The common set element allows complex objects to be
    created using filters and set logic. Again, please refer to the
    description of the set element in the oval-definitions-schema. The
    set of files to be evaluated may be identified with either a
    complete filepath or a path and filename. Only one of these options
    may be selected. It is important to note that the 'max_depth' and
    'recurse_direction' attributes of the 'behaviors' element do not
    apply to the 'filepath' element, only to the 'path' and 'filename'
    elements.  This is because the 'filepath' element represents an
    absolute path to a particular file and it is not possible to recurse
    over a file.

    :ivar set:
    :ivar behaviors:
    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename entity specifies the name of a file.
    :ivar pattern: The pattern entity defines a chunk of text in a file
        and is represented using a regular expression. A subexpression
        (using parentheses) can call out a piece of the text block to
        test. For example, the pattern abc(.*)xyz would look for a block
        of text in the file that starts with abc and ends with xyz, with
        the subexpression being all the characters that exist in
        between. The value of the subexpression can then be tested using
        the subexpression entity of a textfilecontent54_state. Note that
        if the pattern, starting at the same point in the file, matches
        more than one block of text, then it matches the longest. For
        example, given a file with abcdefxyzxyzabc, then the pattern
        abc(.*)xyz would match the block abcdefxyzxyz. Subexpressions
        also match the longest possible substrings, subject to the
        constraint that the whole match be as long as possible, with
        subexpressions starting earlier in the pattern taking priority
        over ones starting later. Note that when using regular
        expressions, OVAL supports a common subset of the regular
        expression character classes, operations, expressions and other
        lexical tokens defined within Perl 5's regular expression
        specification. For more information on the supported regular
        expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html.
    :ivar instance: The instance entity calls out a specific match of
        the pattern. It can have both positive and negative values. If
        the value is positive, the index of the specific match of the
        pattern is counted from the beginning of the set of matches of
        that pattern. The first match is given an instance value of 1,
        the second match is given an instance value of 2, and so on. For
        positive values, the 'less than' and 'less than or equals'
        operations imply the the object is operating only on positive
        values. Frequently, this entity will be defined as 'greater than
        or equals' 1, which results in the object representing the set
        of all matches of the pattern. Negative values are used to
        simplify collection of pattern match occurrences counting
        backwards from the last match. To find the last match, use an
        instance of -1; the penultimate match is found using an instance
        value of -2, and so on. For negative values, the 'greater than'
        and 'greater than or equals' operations imply the object is
        operating only on negative values. For example, searching for
        instances greater than or equal to -2 would yield only the last
        two maches. Note that the main purpose of the instance item
        entity is to provide uniqueness for different
        textfilecontent_items that results from multiple matches of a
        given pattern against the same file, and they will always have
        positive values.
    :ivar filter:
    """

    class Meta:
        name = "textfilecontent54_object"
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
    behaviors: Optional[Textfilecontent54Behaviors] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filepath: Optional[EntityObjectStringType] = field(
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
    pattern: Optional[EntityObjectStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    instance: Optional[EntityObjectIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    
    def generate_check(self, data):
        print(f"TextFileContent54 Object! {self.id}")
        # Now here is where we need to generate the actual code for the object check
        # Since we're searching files for text, we can use grep + find
        # We will have either a "filepath", which is a direct file
        # Or we will have a filename and a path, which means we need to match both multiple dirs and multiple files
        # Then we will need to search the file for the pattern field
        # And finally, we'll need to filter the output by the instance value, which is usually a range
        #print(self)
        filter = ""
        # This is NOT a complete implementation. 
        # I am going to vent here. The OVAL spec SUCKS! Confusing, inconsistent, so many variants in the schema it makes your head spin... why?!
        if self.instance:
            print("TextFileContent54: Instance Detected")
            filter = " | "
            if self.instance.operation is OperationEnumeration.GREATER_THAN_OR_EQUAL:
                if self.instance.value > 0:
                    filter += f"tail -n +{self.instance.value}"
                else:
                    filter += f"tail -n {abs(self.instance.value)}"
            elif self.instance.operation is OperationEnumeration.EQUALS:
                if self.instance.value > 0:
                    filter += f"sed -n {self.instance.value}p"
                else:
                    filter += f"tail {self.instance.value} | head -1"
            else:
                # Throw, since unimplemented
                print(f"ERROR: Unimplemented Instance Operation {self.instance.operation}!")
                sys.exit(-1)        
        if self.filepath:
            print("TextFileContent54: Filepath Detected")
            if ((not self.filepath.operation) or self.filepath.operation in [OperationEnumeration.EQUALS]):
                command = f"grep -h \"{self.pattern.value}\" {self.filepath.value}"
            elif self.filepath.operation == OperationEnumeration.PATTERN_MATCH:
                command = f"find / -regextype posix-egrep -regex \"{self.filepath.value}\" -exec grep -P \"{self.pattern.value}\"" + "{} \\;"
            else:
                print(f"ERROR: Unable to process filepath!")
                sys.exit(-1)
        elif self.filename and self.path:
            print("TextFileContent54: Filename and Depth Detected")
            command = f"find / -regextype posix-egrep -regex \"{self.path.value + "/" + self.filename.value}\" -exec grep -P \"{self.pattern.value}\"" + "{} \\;"
        elif self.set:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTextFileContent54: Set Detected")
            command = self.set.generate_check(data)
        else:
            print(f"ERROR: Unimplemented Object State! No Instance, No Set!")
            sys.exit(-1)
        print(command + filter)
        return command + filter