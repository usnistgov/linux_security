#
# YAML Rule Producer Script V2
#
# This script automatically creates and populates yaml files with the requisite data from OpenSCAP reports.
# Create check filename based off of OpenSCAP rule name + category, check if exists, if not, create yaml file in proper folder.
# Add new rule to the rules directory, if the ID exists in the Excel sheet and it has a defined filename.
# Find relevant rule by ID in the CIS or STIG OpenSCAP HTML pages (Pages have a naming convention, this could be a future fix)
# Extract the Rule name, use this for title
# Extract the Rationale, use this for the discussion 
# Extract CCE from References section if existant
# Extract CCIs, 800-53's, SRGs, DISA-STIG, from References section
# Extract severity from Severity section
# Populate tags for 800-53 based off of 800-53 baselines file from mac repo
# Create spaces for OS
# Fill in OS-specific fixes if they exist for shell 

#TODO: Automatically incorporate all checks we can via the datastream XML files provided by OpenSCAP
# There is a huge database of check XML files provided via OVAL format which the DS XML files reference
# Unfortunately for me, they all use their own custom XML format, and there is roughly 500MB of them for all of the OS's we care about
# Some food for thought ideas:
# There is a reasonable chance that a lot of these checks are structurally similar, e.g software checks, file regex checks
# If we could figure out how to make templates for these, or regenerate the XML, it would make life a lot easier.
# Ideally, we do not want to use all the XML, since it's so big
# A reasonable solution may be to parse the oval_unlinked for each OS, as this is only 5MB for Ubuntu 20.04
# Additionally, this has all the info we need and appears to be modularized. 
# In theory, we can positively say that if an XCCDF is defined for that OS's CIS/STIG, it *should* have a check for it.
# It looks like the ssg-ubuntu2004-xccdf checks both the ocil and the oval, so should we do the same? Maybe start with oval

# Relative psuedocode steps
# Given XCCDF ID, e.g xccdf_org.ssgproject.content_rule_account_disable_post_pw_expiration
# Locate the Rule XML block in ssg-OStitleOSVersion-xccdf.xml (should be precached as a dictionary), with the tag:
# <xccdf-1.2:Rule id="xccdf_org.ssgproject.content_rule_account_disable_post_pw_expiration">
# Locate the child block for OVAL:
# <xccdf-1.2:check system="http://oval.mitre.org/XMLSchema/oval-definitions-5"> 
# Locate the sub-block for the specific check ref:
# <xccdf-1.2:check-content-ref href="ssg-ubuntu2004-oval.xml" name="oval:ssg-account_disable_post_pw_expiration:def:1" />
# Index a data structure (probably a dict) for this file's contents, find the block looking like the following:
# <oval-def:definition id="oval:ssg-account_disable_post_pw_expiration:def:1" version="2" class="compliance">
# Look for the child block matching <oval-def:criteria, like below:
# <oval-def:criteria comment="the value INACTIVE parameter should be set appropriately in /etc/default/useradd" operator="AND">
# Find the sub-block with the ID for the test, like below:
# <oval-def:criterion test_ref="oval:ssg-test_etc_default_useradd_inactive:tst:1" />
# TODO: Since there can be multiple criterion, we will need to trace all of these and generate for all of them
# TODO: These are sequential, if we could calculate how many criterion each rule has, we can avoid lookups and just iterate linearly
# Find the block matching this ID which is a textfilecontent54_test type (or maybe another type?):
# <ind:textfilecontent54_test id="oval:ssg-test_etc_default_useradd_inactive:tst:1" version="1" check="all" comment="the value INACTIVE parameter should be set appropriately in /etc/default/useradd" state_operator="AND">
# Find the sub-block in this which has the tag <ind:obj, and grab the object_ref from it:
# <ind:object object_ref="oval:ssg-object_etc_default_useradd_inactive:obj:1" />
# Finding the block with this as the ID gets us a textfilecontent54_object, which contains everything we need to autogenerate the check:
# <ind:textfilecontent54_object id="oval:ssg-object_etc_default_useradd_inactive:obj:1" version="1">
# <ind:filepath>/etc/default/useradd</ind:filepath>
# <ind:pattern operation="pattern match">^\s*INACTIVE\s*=\s*(\d+)\s*$</ind:pattern>
# <ind:instance datatype="int">1</ind:instance>
# </ind:textfilecontent54_object>
# In this case, we make some processing code for the various operations, with modularized shell code for each
# Then we simply insert the values, and profit :)
# Obviously we will need to check and test, but as long as the implementation of this is good, in theory the SSG guys have already tested all these controls, just with their own code
# TODO: XML objects use references, we will need to do a lot of jumping around
# TODO: Defined operations appear to be the following:
# - File Operation (ind:filepath/ind:filename), appears to be accessing of files and directories
#    - Glob/Wildcard match files in a directory
# - Pattern Operation (ind:pattern), appears to be pattern based filtering on a target
#    - Pattern Match to Regex string (grep -e?)
# - Instance Operations (ind:instance), appears to be operations performed on the test pipeline
#    - Greater than or Equal to integer (-eq?)
# - Unix Behavior Operations (unix:), appears to be a category for general OS commands
#    - Recurse Directories (find -exec?), labeled unix:behaviors
#    - Operate on sysctl objects (sysctl?), labeled unix:sysctl_object
#       - Appears to have the members sysctl
# - Linux Behavior Operations (linux:), appears to be a category for Linux-specific concepts (e.g systemd units)
#    - Systemd Manipulation (systemctl?), labeled linux:systemdunitdependency_object
#    - Package Management Info (dpkg), labeled linux:dpkginfo

# TODO: Double check and improve tagging, some of it seems not fully correct
# TODO: Implement ODV in the yaml output

#!/usr/bin/env python3
import openpyxl
import traceback
import os
import glob
import argparse
import sys
import re
import yaml
import time
from timeit import timeit
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer
import lxml
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
#from oval.definitions.gov.nist.checklists.xccdf import *
#from oval.definitions.org.mitre.oval.xmlschema import *
#from oval.definitions.org.w3.pkg_2000.pkg_09.xmldsig import *
#from oval.definitions.org.mitre.oval import *
#from oval.definitions.gov.nist.scap.schema.scap.source import *
#from oval.definitions.gov.nist.checklists.xccdf import *
from scap import *
#from scap.csrc.nist.gov.schema.scap.pkg_1.pkg_3 import *
#from scap.scap.nist.gov.schema.xccdf.pkg_1.pkg_2.xccdf_1_2 import *
#from scap.raw.githubusercontent.com.ovalproject.language.pkg_5.pkg_11.pkg_2.schemas import *
from lxml import etree
# TODO: This entire dumper section can definitely be cleaned up

# Thanks to Reorx Xiao for this code that helps nicely format the yaml dumps!
# Was changing this to CDumper but barely got much performance benefit, need to find an easier bottleneck to solve for
class IndentDumper(yaml.Dumper):
    def increase_indent(self, sequence=True, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

# Compile the provided regex
# Then match it with the target string, and return the first match
# Just a simple helper function
def regex_and_return_first_match(compiledre,targetstring):
    match = compiledre.search(targetstring)
    if match is not None:
        return match.group(0)
    else:
        return None
    
# Check if the provided value already exists in the list
# If not, append the value to the list
# Otherwise, do nothing
def unique_append_lists(list1,list2):
    for value in list2:
        unique_append(list1, value)

# Check if the provided value already exists in the list
# If not, append the value to the list
# Otherwise, do nothing
def unique_append(list,value):
    if list is None:
        list = []
    if value not in list:
        list.append(value)
    # TODO: There are so many wasted cycles on re-sorting here, either do inline sort or one sort at the end
    # Sorting here is super wasteful since we could totally do it at the end, or inline
    # But for now, it doesn't matter
    sort_nicely(list)

# Shamelessly borrowing this function from Bob Gendler :)
# Sort the given list in the way that humans expect.
# Accepts a single list parameter which will be sorted
def sort_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

class multiline(str): pass

def multiline_presenter(dumper, data):
    # This is to make empty checks and fixes look like
    # |
    #  $OS_VALUE
    # Rather than
    # - $OS_VALUE
    return dumper.represent_scalar('tag:yaml.org,2002:str', data + "\n", style='|')

# Adopted from this stackoverflow:
# https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data/8641732#8641732
def str_presenter(dumper, data):
    # This is the fix to get rid of block chomping, e.g |- instead of |
    if len(data.splitlines()) > 1 or '\n' in data:  
        # Try and fix trailing spaces here
        #fixed_data = data + "\n"
        text_list = [line.rstrip() for line in data.splitlines()]
        fixed_data = "\n".join(text_list) + "\n"
        # Victory at last! Turns out pyyaml hates \t, this fixed all the weird double quoting issues
        return dumper.represent_scalar('tag:yaml.org,2002:str', fixed_data.replace("\t","   "), style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

def represent_none(self, _):
    return self.represent_sequence('tag:yaml.org,2002:seq', ["N/A"])

yaml.representer.Representer.add_representer(type(None), represent_none)

def represent_list(self, data):
    if len(data) < 1:
        return self.represent_sequence('tag:yaml.org,2002:seq', ["N/A"])
    return self.represent_sequence('tag:yaml.org,2002:seq', data)

yaml.representer.Representer.add_representer(list, represent_list)

yaml.representer.Representer.add_representer(multiline, str_presenter)

yaml.representer.Representer.add_representer(str, str_presenter)

def evaluate_behavior(behavior, ssg_os_controls, layer=0):
    print(f"{"-- " * layer}Behavior")        

def evaluate_variable(var, ssg_os_controls, layer=0):
    print(f"{"-- " * layer}Var")

def evaluate_state(state, ssg_os_controls, layer=0):
    statereftype = state.prefix + ":" + state.name
    print(f"{"-- " * layer}State {state["state_ref"]} {statereftype}")
    # Now we need to find the actual state
    stateobj = ssg_os_controls.find(attrs={"id":state["state_ref"]})
    stateobjtype = stateobj.prefix + ":" + stateobj.name
    print(f"{"-- " * layer}State Obj {stateobj["id"]} {stateobjtype}")

def evaluate_object(object, ssg_os_controls, layer=0):
    objtype = object.prefix + ":" + object.name
    print(f"{"-- " * layer}Object {object["object_ref"]} {objtype}")
    # Now we need to find the actual object object (lol)
    objobj = ssg_os_controls.find(attrs={"id":object["object_ref"]})
    objobjtype = objobj.prefix + ":" + objobj.name
    print(f"{"-- " * layer}Object Obj {objobj["id"]} {objobjtype}")

    # TODO: Would be great to make this into a functional language evaluator (Bison/ANTLR) or an XML transformer (xsl)
    # So much duplication of code...
    
    # We will not support the old textfilecontent version, for now
    if objobj.name == "textfilecontent54_object":
        # We have a textfilecontent object, which is defined in independent-definitions-schema.xsd
        # This is what generates the "set" of data we expect to get from this file
        # It appears to do greedy perl matching, we should use -P for sure
        pattern = objobj.find("pattern")
        # This is how much of that set to return, e.g if equal to 1, return first, if greater than or equal to 1, return all
        instance = objobj.find("instance")
        # We are guaranteed one of two choices, either a full filepath, or a path and a filename
        print(pattern)
        print(instance)
        print(objobj)
        if objobj.find("filepath"):
            filepath = objobj.find("filepath")
            # Since we only need to search a filepath, we can just use grep
            aggregator_command=f"grep -P '{pattern.get_text()}' {filepath.get_text()})"
        else:
            # We should have a path + filename
            filename = objobj.find("filename")
            path = objobj.find("path")
            # Since we need to search a path for filenames, we should probably use find
            # We also have to support recursion and recurse directions, along with max depth, if not pattern
            if path.operation and path.operation == "pattern match":
                # We have options for two layers of pattern matching here
                if filename.operation and filename.operation == "pattern match":
                    aggregator_command=f"find / -regex '{path.get_text() + "/" + filename.get_text()}' -exec grep -P '{pattern.get_text()}'" + r" \{} +"
                else:
                    # Need to test if this works the way I think it does
                    aggregator_command=f"find / -regex '{path.get_text() + "/" + filename.get_text()}' -exec grep -P '{pattern.get_text()}'" + r" \{} +"
            elif not path.operation or (path.operation and path.operation == "equals"):
                # Now for recurse + depth + maybe file pattern matching
                # Technically the spec says we have to support upwards recursion (why?)
                # Since find does not support this, and as far as I can tell none of the XML files feature it, we will not support this.
                behavior = objobj.find("behaviors")
                extraargs = ""
                if behavior:
                    behaviors = behavior.attrs
                    if "max_depth" in behaviors.keys():
                        extraargs += f" -maxdepth {behaviors["max_depth"]} "
                    if "recurse" in behaviors.keys():
                        recursetype = behaviors["recurse"]
                        if recursetype == "symlinks and directories":
                            # Find follows dirs by default, so just add symlinks
                            # We don't need to do anything if the type is directories, since that's default behavior too
                            extraargs += " -L "
                        elif recursetype == "symlinks":
                            # This is an interesting variant from the OVAL standard and is difficult to implement. 
                            # Since it is not natively supported by find, I am choosing to throw an error if this condition is ever encountered
                            # Rather than generate a broken check.
                            print("FATAL ERROR: XML Parsing encountered a recursion type of symlinks only, which is not currently implemented.")
                            os.exit(-1)
                    if "recurse_direction" in behaviors.keys():
                        # By default this is down, but we aren't implementing upwards recursion, so we will inform the user and throw an error
                        # For some reason this also has a "none" value, we will also not be implementing that.
                        if behaviors["recurse_direction"] in ["upward","none"]:
                            print("FATAL ERROR: XML Parsing encountered a recursion direction of down or none, which are not currently implemented.")
                            os.exit(-1)
                    if "recurse_file_system" in behaviors.keys():
                        # The spec here is not clear, but it seems like "all" represents all file systems it encounters, e.g spare media mounted to /run, etc
                        # "local" and "defined" seem mostly synonymous, in that "local" means to stick to the current file system, e.g if your path is /, do not check other fs
                        # "defined" appears to also mean to stick to the file system defined, e.g if your path is /, do not check /run/media or other fs
                        # In find, recursing other file systems is the default, so we only need to do something for restrictions on this
                        if behaviors["recurse_file_system"] in ["local","defined"]:
                            extraargs += " -mount "
                aggregator_command=f"find {extraargs} / -regex '{path.get_text() + "/" + filename.get_text()}' -exec grep -P '{pattern.get_text()}'" + r" \{} +"
            else:
                print("FATAL ERROR: XML Parsing encountered an unexpected operation type.")
                os.exit(-1)
        processor = None
        if instance and "operation" in instance.attrs.keys():
            # Now we need to filter the set through the instance, which can basically subset n...m from our generated set
            # For instance, if instance is 1 and the operation is equals, we go from 1..1 and get the first match
            # Now if we have greater than or equal and 1, we go from 1...m and get every match in the set
            operation = instance["operation"]
            instancevalue = instance.get_text()
            if operation == "equals":
                # This prints exactly that line
                processor = f"sed -n {instancevalue}p"
            elif operation == "greater than or equal":
                # This prints all remaining lines, starting at the value
                processor = f"tail -n {instancevalue}"
            else:
                # This is unimplemented, so throw an error
                print("FATAL ERROR: XML Parsing encountered an instance operation that is not == or >=, which means it is unimplemented.")
                sys.exit(-1)
        # Since I really would not like to make code with variables named 1234ABD=$()
        # Let's start with lazy naming, and just remove symbols from the ID and cap it at 16 chars
        variable_name=re.sub(r'[^a-zA-Z]', '', objobj["id"]).replace("ovalssgobject","")
        # The object should produce a bash command that stores to a variable, which we can then compare to the state in our test
        final_command=f"{variable_name}=$({aggregator_command} {str("| " + processor) if processor else ""})"
        print(f"Created a bash command variable: {final_command}")
                



def evaluate_test(test, ssg_os_controls, layer=0):
    print(f"{"-- " * layer}Test {test["id"]} {test.prefix + ":" + test.name}")
    object=test.find(object_ref=True)
    if object:
        object = evaluate_object(object,ssg_os_controls,layer+1)
    states=test.find_all(state_ref=True)
    for state in states:
        states = evaluate_state(state,ssg_os_controls,layer+1)
    # Now, if we were doing a proper implementation, we'd evaluate here
    # However, instead we want to generate some bash code that matches these states + object requirements 
    # Unfortunately, we are going to need to do 26 different if statements here
    # I guess we could make 26 classes instead? Maybe at some point

def evaluate_criterion(criterion, ssg_os_controls, layer=0):
    # This should create a BASH inline variable, called something creative if at all possible
    print(f"{"-- " * layer}Criterion {criterion["test_ref"]}")
    test=ssg_os_controls.find(attrs={"id":criterion["test_ref"]})
    if test:
        evaluate_test(test,ssg_os_controls,layer+1)
        print(f"{"-- " * (layer + 1)}Test {test.name} {test["id"]}")
        #object=ssg_os_controls.find(attrs={"id":test.findChildren(name=True,string=False)[0]["object_ref"]})
        #if object:
        #    print(f"{"-- " * (layer + 2)}Object {object.name} {object["id"]}")
        #    # Here's where we do the granular handling of operations
        #    children = object.findChildren(name=True,string=False)
        #    if object.name == "textfilecontent54_object":
        #        # There can be all sorts of stuff such as behaviors,filepath,pattern,instance in here
        #        # This is basically like writing a compiler...
        #        for child in children:
        #            print(f"{"-- " * (layer + 3)}Attribute {child.name} {child.get_text()}")
        #    else:
        #        for child in children:
        #            print(f"{"-- " * (layer + 3)}Attribute x{child.name} {child.get_text()}")

def evaluate_criteria(criteria, ssg_os_controls, layer=0):
    print(f"{"-- " * layer}Criteria operator is {criteria["operator"]}")
    # This is where we will want to assemble the equivalency statements 
    segments = []
    for child in criteria.children:
        #print(f"{child} name {child.name}")
        if child.name == "extend_definition":
            print(f"{"-- " * layer}Recursing extend_def..")
            segments.append(evaluate_definition(ssg_os_controls.find("oval-def:definition",attrs={"id":child["definition_ref"]}), ssg_os_controls, layer=layer+1))
            print(f"{"-- " * layer}Finished recursion layer...")
        elif child.name == "criterion":
            print(f"{"-- " * layer}Found criterion!")
            segments.append(evaluate_criterion(child, ssg_os_controls, layer=layer+1))
            print(f"{"-- " * layer}Finished evaluating criterion..")
        elif child.name == "criteria":
            print(f"{"-- " * layer}Recursing criteria..")
            segments.append(evaluate_criteria(child, ssg_os_controls, layer=layer+1))
            print(f"{"-- " * layer}Finished criteria recursion...")
    
def evaluate_definition(definition, ssg_os_controls, layer=0):
    if definition.criteria:
        print(f"{"-- " * layer}Found criteria in definition {definition["id"]}! Evaluating...")
        return evaluate_criteria(definition.find("oval-def:criteria"), ssg_os_controls, layer=layer+1)

def generate_state(state, vars, depth=0):
    print(f"{"--" * depth}State {state.id}")

def generate_object(object, vars, depth=0):
    print(f"{"--" * depth}Obj {object.generate_check()}")
    # This is where we're going to need to call class functions, and where it probably makes sense to add a "parse" function to the root

def generate_test(test_ref, tests, states, objects, vars, depth=0):
    test = tests[test_ref]
    print(f"{"--" * depth}Test {test.id}")
    # Get object which should exist
    objectref = test.object_value.object_ref
    generate_object(objects[objectref], vars, depth+1)
    # Get states if they exist
    staterefs = test.state
    for stateref in staterefs:
        generate_state(states[stateref.state_ref], vars, depth+1)

def generate_criteria(criteria, tests, states, objects, vars, depth=0):
    print(f"{"--" * depth}Criteria: {criteria.comment}")
    # Check the relevant operator
    operator = criteria.operator
    print(f"{"--" * depth}Operator {operator}")
    # Get the operands (criterion)
    criterions = criteria.criterion
    for criterion in criterions:
        generate_test(criterion.test_ref, tests, states, objects, vars, depth+1)
    #print(f"Criterions: {criterions}")
    # Get the operands (criteria)
    criterias = criteria.criteria
    for crit in criterias:
        generate_criteria(crit, tests, states, objects, vars, depth+1)
    
    
# TODO: This will be in DESPERATE need of optimization
# We went from roughly 20-30 rules a second to 1 at best! But that makes sense, we have to search a giant XML file...
# We may have to consider preloading and creating an optimized file?
def generate_check(check, defs, tests, states, objects, vars):
    ovalref = check.find("xccdf-1.2:check-content-ref")["name"]
    # Grab Dictionary Object from Ref ID
    definition = defs[ovalref]

    # print(f"\n\n {definition} \n\n")
    # Evaluate criteria and criterion 
    # We have a tree of CriteriaType nodes
    criteriaroot = definition.criteria
    print(f"\n\n Criteria Root: {criteriaroot}")
    # Then we need to DFS down the criteria chain, and grab all criterion on each level. 
    # Recursion? 
    criteriachain = definition.generate_check(data={"tests":tests,"definitions":defs,"states":states,"objects":objects,"vars":vars})
    #print(f"Got ovaldef: {ovaldef}")
    #evaluate_definition(ovaldef, ssg_os_controls)
    # Criteria appears to be structured like so:
    # There is a criteria block, with an operator, generally AND or OR
    # Inside of this, there can be multiple more criteria blocks, which are evaluated as well
    # Inside of each criteria block, there are one of three things: a subcriteria, a criterion, or an extend_definition, which links to more criteria
    # This is reminding me of BPF/functional programming...
    # Our evaluation order should probably be: 
    # Expand subcriteria first
    # Then criterion
    # Then extended_definitions?
    #ovaltref = ovaldef.find("oval-def:criterion")["test_ref"]
    #print(f"Got ovaltref: {ovaltref}")
    #testref = ssg_os_controls.find(attrs={"id":ovaltref})
    #print(f"Got testref: {testref}")
    #objref = testref.find(text=False)["object_ref"]
    #print(f"Got objref: {objref}")
    #endref = ssg_os_controls.find(attrs={"id":objref})
    #print(f"Check found! {endref}")

def main():

    # Get the root directory of the git repo we should be inside of
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Create arguments parser
    parser = argparse.ArgumentParser(description='Use an XLSX file of desired rules from CIS and STIG to create and populate the equivalent yaml files')
    parser.add_argument("--spreadsheet", default=None, help="A full file path to an Excel spreadsheet containing desired rules and names for STIGs and CIS")
    parser.add_argument("--mappings", default="/resources", help="The local directory in this repo to search for relevant OS mapping guides and XML files, in the form of ssg-OS-guide-cis and ssg-OS-guide-stig")
    parser.add_argument("--outputdir", default="/testrules", help="The directory this script will create populated rule files in. It will overwrite same-name rules in this directory")
    parser.add_argument("--overwrite", default=False, help="This value allows you to recreate existing yaml files in the input directory. USE WITH CAUTION!")
    try:
        # Parse our arguments 
        results = parser.parse_args()
        print("Using the spreadsheet at this path: " + results.spreadsheet)
        print("Loading SSG guide files from this directory: " + str(results.mappings))
        print(f"Using {results.outputdir} as the output directory for newly generated yaml files")
    except IOError as msg:
        # TODO: This really should be cleaner error handling
        parser.error(str(msg))

    # Attempt to load the working XLSX spreadsheet which we've specified the path to in args
    # Load the workbook
    try:
        workbook = openpyxl.load_workbook(results.spreadsheet)
    except FileNotFoundError as err:
        # TODO: Does this cover other exceptions besides just the file not existing?
        # TODO: Make this error handling better and more verbose for end users
        print("Error loading the spreadsheet. Exiting...")
        sys.exit(-1)

    # Select the active sheet
    sheet = workbook.active

    # Load OpenSCAP files in mappings directory
    # The filename pattern is ssg-(osname)(osmajorversion)-guide-(stig or cis)-(variants).html
    # We can infer the relevant OS info for the yaml file from this
    # Thanks Bob for writing the yaml os versions to be raw nums, the same as the SSG format :)
    # The main reason I'm using a dictionary here is just so that I can associate each HTML's content with the OS name and guide type,
    # Rather than having to do some beautifulsoup magic to pull it out or something like that.
    # Not the most efficient way of doing it.. maybe a future TODO!
    ssg_controls_dictionary = {}
    # This is a second dict that purely stores text, for the sake of speed up efficiency.
    # The get_text() call otherwise has to be called all 444 times, this way we only do it once per read of each SSG
    ssg_rawtext_dictionary = {}

    ssg_rules_dictionary = {}

    # We need to make dicts for each separate list of tests, states, etc, so that we can quickly parse based off of that
    ssg_defs_dict = {}
    ssg_tests_dict = {}
    ssg_objects_dict = {}
    ssg_states_dict = {}
    ssg_vars_dict = {}

    # Defining resources path
    resources_path = root_dir + "/resources/xml/"

    # Starting a timer to see how long it takes to generate all these rules (could definitely be made more efficient)
    start_time = time.time()

    # Create a global compiled regex cache to increase performance
    regex_cache=[
        re.compile(r"[a-z]+"),
        re.compile(r"\d+"),
        re.compile(r"level\d{1}"),
        re.compile(r"(server|workstation){1}"),
        re.compile(r"(stig_gui|stig){1}"),
        re.compile(r"CCE\-\d{5}\-\d{1}"),
        re.compile(r"SRG\-OS\-\d{6}\-GPOS\-\d{5}"),
        re.compile(r"^[A-Z]{2}\-\d{1,2}(?:\.\d{1,2})?(?:\(\w{1,3}\))?$"),
        re.compile(r"CCI\-\d{6}"),
        re.compile(r"[A-Z]{4}\-\d{1,2}\-\d{6}")  
    ]

    for ssg_control_file in glob.iglob(f"{resources_path}/*.xml"):
        # Determine all OS variants in play, by listing all files and doing prefix comparisons
        # Essentially, we need to look through the files, find every rhel8, rhel9, ubuntu2204, etc guide
        # Then, we need to pick out the one we'd like to use, and load that one into the dictionary.
        # The question becomes, how do we decide which one to use? 
        # For STIG, there are only two variants, STIG and STIG_GUI. STIG_GUI primarily removes controls relating to the X windowing system.
        # For CIS, there are a few variants, Level 1 and Level 2, of both workstation and server. 
        # For now, we'll make the decision to follow the mac security way of doing it.
        # We will add every rule we can, and tag them according to the following:
        # - If the rule exists in STIG_GUI or a CIS Workstation, we will tag it client (consider changing this to workstation?).
        # - If the rule exists in STIG or a CIS Server, we will tag it server.
        # - If a rule exists in any of the STIGs, we will tag it stig.
        # - If the rule exists in CIS Level 1, we will tag it cis_lvl1
        # - If the rule exists in CIS Level 2, we will tag it cis_lvl2.
        # - If the rule exists in any of the CIS, we will tag it cis.
        
        # We probably need to preprocess and link every single element of this, thanks to all the IDREFs not autolinking...

        #XSDATA commands
        # xsdata generate ..\resources\xml\sources\ --recursive --package oval.definitions -ss single-package --debug\
        # test
        ssg_file_path = os.path.join(resources_path,ssg_control_file)
        try:
            with open(ssg_file_path, 'r', encoding='utf-8') as file:
                basename = os.path.basename(ssg_file_path).split("-")[1]
                os_name = basename #basename.split("-")[1]
                print(f"Saving into SSG dictionary with the key {basename}") 

            
                # Test loading a definition here
                parser = XmlParser(handler=LxmlEventHandler)
                tree = lxml.etree.parse(ssg_file_path)
                root = tree.getroot()
                # There has got to be a better way to do this... having to load the rule, then go find the def, then go find the checks, then go find the variables.. yeesh!d
                # This data structure is so bad... it autocreated a specific list for each type, rather than a generic!
                # Why even use the source schemas at all... I may have to go back and redo this 
                # I don't even think it's XSDATA's fault... just that the OVAL schema is such a cluster..
                states = tree.find(".//oval-def:states",namespaces=root.nsmap)
                ssg_states_dict[basename] = {}
                for state in states.getchildren():
                    parsed = parser.parse(state)
                    ssg_states_dict[basename][parsed.id] = parsed

                objects = tree.find(".//oval-def:objects",namespaces=root.nsmap)
                ssg_objects_dict[basename] = {}
                for object in objects.getchildren():
                    parsed = parser.parse(object)
                    ssg_objects_dict[basename][parsed.id] = parsed

                tests = tree.find(".//oval-def:tests",namespaces=root.nsmap)
                ssg_tests_dict[basename] = {}
                for test in tests.getchildren():
                    parsed = parser.parse(test)
                    ssg_tests_dict[basename][parsed.id] = parsed

                variables = tree.find(".//oval-def:variables",namespaces=root.nsmap)
                ssg_vars_dict[basename] = {}
                for variable in variables.getchildren():
                    parsed = parser.parse(variable)
                    ssg_vars_dict[basename][parsed.id] = parsed
                 
                definitions = tree.find(".//oval-def:definitions",namespaces=root.nsmap)
                ssg_defs_dict[basename] = {}
                for definition in definitions.getchildren():
                    parsed = parser.parse(definition)
                    ssg_defs_dict[basename][parsed.id] = parsed    
                print(f"Successfully populated definitions, objects, tests, states, and variable dictionaries for {basename}.")
                
                ssg_controls_dictionary[basename] = BeautifulSoup(file.read(), "lxml-xml")
                ssg_rawtext_dictionary[basename] = ssg_controls_dictionary[basename].get_text()
                ssg_benchmarks_dict = {}
                for benchmark in ssg_controls_dictionary[basename].find_all("xccdf-1.2:Profile"):
                    tags = []
                    cis_level = regex_and_return_first_match(regex_cache[2],benchmark["id"])
                    cis_type = regex_and_return_first_match(regex_cache[3],benchmark["id"])
                    stig_type = regex_and_return_first_match(regex_cache[4],benchmark["id"])
                    # TODO: Consider tagging "standard" rules?
                    if cis_level:
                        if cis_level == "level1":
                            unique_append(tags,"cis_lvl1")
                        elif cis_level == "level2":
                            unique_append(tags, "cis_lvl2")
                        else:
                            print("WARNING: THIS STATEMENT SHOULD NOT BE REACHED WITH ACCURATE PARSING.")
                    if cis_type:
                        if cis_type == "server":
                            unique_append(tags,"server")
                        elif cis_type == "workstation":
                            unique_append(tags,"client")
                    # TODO: This might need to be refactored, there doesn't seem to be a STIG_GUI in the datastreams
                    if stig_type:
                        unique_append(tags,"stig")
                        if stig_type == "stig":
                            unique_append(tags,"server")
                        elif stig_type == "stig_gui":
                            unique_append(tags, "client")
                    values =  benchmark.find_all("xccdf-1.2:refine-value")
                    ssg_benchmarks_dict[benchmark["id"]] = {
                        # We are matching selected as true because groups are listed as rules as well, but they all appear to be unselected
                        "rules":[rule["idref"] for rule in benchmark.find_all("xccdf-1.2:select",attrs={"selected":"true"})],
                        # These are going to be substitution values in checks and fixes that are specific to a guide (STIG, CIS, etc)
                        # In Bob's repo, these are called ODVs, so I am borrowing that concept for our yaml schema 
                        "odv_ids":[value["idref"] for value in values],
                        "odv_values":[value["selector"] for value in values],
                        "tags":tags
                    }
                # Let's run a find_all on this, and then place all the finds into a dictionary, correlated by their ID
                for control in ssg_controls_dictionary[basename].find_all("xccdf-1.2:Rule"):
                    if control["id"] not in ssg_rules_dictionary.keys():
                        ssg_rules_dictionary[control["id"]] = {"rules":[],"os_name":[]}
                    ssg_rules_dictionary[control["id"]]["rules"].append(control)
                    ssg_rules_dictionary[control["id"]]["os_name"].append(os_name)
                #print(ssg_labeledcontrols_dictionary[basename])
                print(f"Successfully found and loaded SSG XML file: {ssg_file_path}")
        except Exception as e:
            # TODO: More advanced error reporting
            print(f"Unable to load SSG XML file: {ssg_file_path} {e.with_traceback} {e.args} {(type(e))}")

    end_time1 = time.time()
    print(f"Time taken to load all datastreams: {end_time1-start_time}")

    # Change to rules dir to begin creating test rules
    os.chdir(root_dir)

    # Load NIST 800-53 yaml
    with open(root_dir + "/includes/800-53_baselines.yaml",'r') as file:
        nist_yaml = yaml.safe_load(file)

    # Iterate through each row in our spreadsheet
    valid_rules=0
    # Count successful populations
    populated_rules = 0
    # Skip the first row as this is the column titles
    for row in sheet.iter_rows(min_row=2,values_only=True):
        # Look for rows with a valid name set AND a valid CIS or STIG rule
        if row[0] and (row[2] or row[4]):
            # In our sheet, column 1 is the full file name, column 2 is the type (os, audit, etc), and column 3 and 5 are the relevant CIS and STIG IDs. 
            filepath=Path(os.getcwd() + "/rules/" + row[1] + "/" + row[0])
            # Create the os, audit, pwpolicy, etc dirs if they don't already exist in output dir
            os.makedirs(os.path.dirname(Path(os.getcwd() + "/" + results.outputdir + "/" + row[1] + "/" + row[0])), exist_ok=True)
            
            if not filepath.is_file() or results.overwrite:
                # This sets the control ID to be the CIS one, if no CIS one, set to STIG, since one must exist
                # (In our schema, both columns contain SSG-type rules, so defaulting to CIS is fine if both exist)
                control_id = row[2] if row[2] else row[4]


                # TODO: Probably should check if it exists or not in our rules dict
                # One of the big benefits of DataStream over HTML is we can just straight up autofill this
                # TODO: It would be really nice to create a "generic" XML file that contains all the values that are the same for every datastream
                # For now, I guess we can grab every variant's value, compare, if any are unique, make it OS_VALUE, otherwise, make global the value
                if control_id in [None, " "] or control_id not in ssg_rules_dictionary.keys():
                    continue
                benchtags = []
                for id, benchmark in ssg_benchmarks_dict.items():
                    if control_id in benchmark["rules"]:
                        unique_append_lists(benchtags,benchmark["tags"])
                first_rule = ssg_rules_dictionary[control_id]["rules"][0]
                yaml_dict=dict(
                id = row[0].split(".")[0],
                title = str(first_rule.title.get_text()),
                discussion = str(first_rule.rationale.get_text()),
                check = multiline("$OS_VALUE"),
                result = {"integer":1},
                fix = multiline("$OS_VALUE"),
                references={
                    "cce":["$OS_VALUE"],
                    "cci":[],
                    "800-53r4":[],
                    "srg":[],
                    "disa_stig":["$OS_VALUE"],
                    "cis":{
                        "benchmark":["$OS_VALUE"]
                    },
                },
                tags = benchtags,
                severity = str(first_rule["severity"]),
                os_specifics = {},
                )
                start1 = time.time()
                for rule, os_type in zip(ssg_rules_dictionary[control_id]["rules"],ssg_rules_dictionary[control_id]["os_name"]):
                    # TODO: This is probably redundant
                    if rule:
                        # Define the os specifics category here, since we don't care if it doesn't have the control :)
                        os_title = regex_and_return_first_match(regex_cache[0],os_type)
                        os_version = regex_and_return_first_match(regex_cache[1],os_type)
                        if os_title not in yaml_dict["os_specifics"].keys():
                            yaml_dict["os_specifics"][os_title] = {}
                        if os_version not in yaml_dict["os_specifics"][os_title].keys():
                            yaml_dict["os_specifics"][os_title][os_version] = {}
                        yaml_dict["os_specifics"][os_title][os_version] = {"references":{"cce":[],"disa_stig":[]},"check":None,"fix":None}
                        yaml_references = yaml_dict["references"]
                        yaml_os_specificrefs = yaml_dict["os_specifics"][os_title][os_version]["references"]                        
                        # Now for the fun part! Grabbing the various CCIs, STIGs, and 800-53's from identifiers
                        identifiers = rule.find_all("xccdf-1.2:reference")
                        for identifier in identifiers:
                            #idstr += str(identifier.string) + " "
                            if identifier["href"] == "https://public.cyber.mil/stigs/cci/":
                                #This is a CCI, add this to the global refs
                                unique_append(yaml_references["cci"], str(identifier.get_text()))
                            if identifier["href"] ==  "http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf":
                                # This is an 800-53, so check against severity grading + add to global refs
                                nistmatch = str(identifier.string)
                                unique_append(yaml_references["800-53r4"], nistmatch)
                                if nistmatch in nist_yaml["low"]:
                                    unique_append(yaml_dict["tags"],"800-53r5_low")
                                if nistmatch in nist_yaml["moderate"]:
                                    unique_append(yaml_dict["tags"],"800-53r5_moderate")
                                if nistmatch in nist_yaml["high"]:
                                    unique_append(yaml_dict["tags"],"800-53r5_high")
                            if identifier["href"] ==  "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cgeneral-purpose-os":
                                # This is an SRG, so add to global refs
                                unique_append(yaml_references["srg"],str(identifier.get_text()))
                            if identifier["href"] ==  "https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cunix-linux":
                                # This is a STIG, so add it to os_specifics
                                unique_append(yaml_os_specificrefs["disa_stig"],str(identifier.get_text()))
                        cce = rule.find("xccdf-1.2:ident")
                        if cce:
                            unique_append(yaml_os_specificrefs["cce"],str(cce.get_text()))
                        fix = rule.find("xccdf-1.2:fix",attrs={"system":"urn:xccdf:fix:script:sh"})
                        if fix:
                            remediation = "[source,bash]\n---\n" + str(fix.get_text()) + "\n---"
                            yaml_dict["os_specifics"][os_title][os_version]["fix"] = multiline(remediation)
                        # Now for the new and exciting part, autogenerating bash code using the check definitions in the xml :)
                        # We'll make the decision to go primarily with the oval checks
                        check = rule.find("xccdf-1.2:check",attrs={"system":"http://oval.mitre.org/XMLSchema/oval-definitions-5"})
                        if check:
                            # This is gonna be slow... definitely future optimization candidate
                            # There seems to be recursive definitions... Guess we have to write a function for this...
                            generate_check(check,ssg_defs_dict[os_type],ssg_tests_dict[os_type],ssg_states_dict[os_type],ssg_objects_dict[os_type],ssg_vars_dict[os_type])
                        #print(yaml_dict)
                try:
                    with open(Path(os.getcwd() + "/" + results.outputdir + "/" + row[1] + "/" + row[0]), 'w') as file:
                        yaml.dump(yaml_dict, file, default_style=False, sort_keys=False, allow_unicode=True, Dumper=IndentDumper)
                    print(f"Successfully populated and wrote {row[0]}!")
                except Exception as error:
                    print(f"Error: Unable to produce the file {row[0]}! The specific error is {error}.")
                    print(traceback.format_exc())
                    sys.exit(-1)
                populated_rules += 1
                end1 = time.time()
                exect = end1 - start1
                print(f"Total time taken for {control_id} is {exect}.")
            else:
                print(f"{row[0]} already exists.")
            valid_rules += 1
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Rule Populator Execution time: {execution_time} seconds.")
    print(f"Successfully populated {populated_rules} rules.")
    # At old RPS (~2.55) as of 1/30/25, this means that this script can populate all 444 rules in 174 seconds, or a little under 3 minutes.
    # At new RPS (~6.6) as of 1/31/25, this means that we can produce all 444 rules in only 67 seconds, or a little over 1 minute! HUGE improvements
    # We've made it to a new RPS of (35.5) (yes, you read that right), meaning this can produce all 444 rules in 12 seconds. 
    # This is probably the reasonable limit of performance optimizations, at least until the amount of SSGs being processed increases significantly.
    print(f"Calculated RPS (rule populations per second) is {populated_rules / execution_time}.")
    print(f"Successfully processed {valid_rules} rules.")

main()