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

    # TODO: Use this for type-specific attributes (e.g attributes we ONLY see with TFC54)
    # TODO: Anything that we can get away with processing generically (e.g it's a string or a var ref, do it)
    def evaluate_specific_attribute(self, attribute, data):
        print(f"TFC54 Specific: {attribute}")

    # This is a lot nicer looking
    # TODO: need to figure out a way to denote attribute typing so they resolve specifics better
    def evaluate_object(self, data):
        prettyname = self.pretty_name()
        print(f"TFC54 Object, PrettyName: {prettyname}: {self}")
        command = ""
        if self.set:
            print("TFC54: Evaluating Set...")
            command = self.set.evaluate_set(data)
        else:
            if self.pattern:
                command += self.evaluate_attribute(self.pattern,data)
            if self.filepath:
                command += self.evaluate_attribute(self.filepath,data)
            if self.filename:
                command += self.evaluate_attribute(self.filename,data)
            if self.path:
                command += self.evaluate_attribute(self.path,data)
            if self.instance:
                command += self.evaluate_attribute(self.instance,data)
            if self.filter:
                command += self.evaluate_attribute(self.path,data)
            # TODO: Now that we have the requisites, we can assemble the object evaluation code
            # TODO: This should be:
            # READ (FILEPATH|FILENAME+PATH) -> FILTER CONTENTS (PATTERN) -> SUBSET (INSTANCE) 
            # -> FILTER SET (FILTER) -> OUTPUT SET (COMMAND)
        return command

#    def evaluate_object_old(self, data):
        print(f"TextFileContent54 Object! {self}")
        # In theory, there shouldn't be any direct name collisions with this format, and it's easier to read than a hash
        # All children of this object should be different since there's no reason for a variable to regenerate it's own obj... right? 
        # TODO: Probably worth checking if collisions are a problem (maybe keep a set of all names generated, and fail if a collision happens)
        # TODO: This really should be a regex...
        # TODO: The majority of this that can be realistically migrated to the superclass should be moved there, for genericism's sake
        prettyname = self.pretty_name()
        print(f"PrettyName: {prettyname}")
        print(self)
        # Now here is where we need to generate the actual code for the object check
        # Since we're searching files for text, we can use grep + find
        # We will have either a "filepath", which is a direct file
        # Or we will have a filename and a path, which means we need to match both multiple dirs and multiple files
        # Then we will need to search the file for the pattern field
        # And finally, we'll need to filter the output by the instance value, which is usually a range
        #
        # REMEMBER, HTML conversions such as &gt; vs > can and WILL break your regex!
        #
        filter = ""
        command = ""
        # This is NOT a complete implementation. 
        # I am going to vent here. The OVAL spec SUCKS! Confusing, inconsistent, so many variants in the schema it makes your head spin... why?!     
        if self.set:
            print("TextFileContent54: Set Detected")
            command = self.set.evaluate_set(data)
        else:
            # Since all of these are mutually exclusive, we're going to need to individually parse them into command segments, then combine
            # Them depending on which ones are present and which ones aren't
            file_selector = ""
            file_pattern = ""
            text_selector = ""
            text_pattern = ""
            if self.pattern:
                # This is another field that can have external variables which we will need to resolve
                if self.pattern.var_ref:
                    text_pattern = data["variables"][self.pattern.var_ref].evaluate_variable(data)
                else:
                    text_pattern = self.pattern.value
                # TODO: Test if this works with full matches and not just subgroups. So much oneline weirdness with perl..
                # Right now, I know this format works to print out just the matching group and nothing else, which is what we want
                # cat test.conf | perl -0777 -ple 'print if s/^[\s]*\[pam](?:[^\n\[]*\n+)+?[\s]*offline_credentials_expiration[\s]*=[\s]*(\d+)\s*(?:#.*)?$//'
                # But I do not know if this would work for multiple matching groups (presumably not), or a single match
                text_selector = f"perl -ple 'print $1 if /{text_pattern}/'"
            else:
                print("TextFileContent54 ERROR: No Pattern in Object!")
                sys.exit(-1)
            # TODO: The fact that most if not all of these attributes support external variable definitions is headache-inducing
            # Currently, we are duplicating a lot of code to ensure that all of these are processed, which is both horrible to
            # Look at and horrible to read/maintain/make changes to. Ideally, this should be genericized somehow, maybe with a 
            # evaluate_variable() function in the superclass or something. Because this will need to happen for every single attribute

            # We need to, for each object type:
            # Determine which attributes need to be evaluated to produce the data, and which are decorators
            # Evaluate these attributes, produce bash variables with hardcoded values for them, or produce bash code which will produce their values upon runtime
            # Assemble these attributes (or bash code equivalencies) into more bash code which will generate and filter the dataset this object represents
            # Return the code to do this to the test class

            # Can we do something like: iterate over attributes, evaluate, produce code
            # Then produce the final output code based off this?

            if self.filepath:
                if self.filepath.operation is OperationEnumeration.PATTERN_MATCH:
                    # Now we need to check if the pattern is locally defined, or externally defined in a variable
                    if self.filepath.var_ref:
                        # Now we need to grab the variable's value(s) from the reference
                        # Let's have generate check return a list of the variable results
                        evaluated = data["variables"][self.filepath.var_ref].evaluate_variable(data)
                        # Since this can have multiple values, we could use a (X|Y|Z) format?
                        file_pattern = "|".join(value for value in evaluated)
                        # TODO: we need to use the value in var_check (e.g all) to make sure that the filepath matches are contained
                        # In the variable values set. So far, in TextFileContent Filepath matching with vars, it appears to only be "at least one"
                    else:
                        # If there's no var_ref, we can safely just assume it's in the value for this block
                        file_pattern = self.filepath.value
                    file_selector = f"find / -regextype posix-extended -regex ${prettyname}FILEPATTERN -exec ${prettyname}TEXTSELECTOR" + "{} \\; 2> /dev/null"
                elif self.filepath.operation is None or self.filepath.operation is OperationEnumeration.EQUALS:
                    # Was reading the "useless use of cat" recently :) 
                    file_pattern = self.filepath.value
                    file_selector = f"< ${prettyname}FILEPATTERN ${prettyname}TEXTSELECTOR"
            elif self.filename and self.path:
                filepath_value = ""
                filename_value = ""
                if self.path.var_ref:
                    # TODO: Looks like var_check means that we may need to grab a subset of items for this! So for at least one, get all?
                    # And then maybe for like one, get only one. Since these variables might be runtime evaluated, we probably need to 
                    # Do the filtering of the variable set in the bash script, and not preprocessing it. Worth evaluating later
                    #print("path var ref")
                    filepath_value = data["variables"][self.path.var_ref].evaluate_variable(data)
                elif self.path.value:
                    filepath_value = self.path.value
                else:
                    print("TextFileContent54: ERROR, no path value but block defined")
                if self.filename.var_ref:
                    #print("filename var ref")
                    filename_value = data["variables"][self.filename.var_ref].evaluate_variable(data)
                elif self.filename.value:
                    filename_value = self.filename.value
                else:
                    print("TextFileContent54: ERROR, no filename value but block defined")
                print(filepath_value)
                print(filename_value)
                file_pattern = filepath_value + filename_value
                file_selector = f"find / -regextype posix-extended -regex ${prettyname}FILEPATTERN -exec ${prettyname}TEXTSELECTOR" + "{} \\; 2> /dev/null"
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
            command += f"""
            {prettyname}FILEPATTERN={file_pattern}
            {prettyname}TEXTSELECTOR={text_selector}
            {prettyname}FILESELECTOR=$({file_selector})
            {prettyname}DATASET=$(${prettyname}FILESELECTOR{filter})
            """
        return command