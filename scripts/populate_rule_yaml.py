#
# YAML Rule Producer Script
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

# TODO: In the long term future, the ssg-ubuntu2004-xccdf.xml contains all the same text as the HTML. In theory, it should be easier (and more reliable to parse), as it contains both STIGs and CIS.
# Definitely something that may be worth pursuing down the road, since parsing the HTML is more of a stopgap and I only went down that road since I was unaware of the XML files until now.

#!/usr/bin/env python3
import openpyxl
import traceback
import os
import glob
import argparse
import sys
import re
# See comment above line 323 on why I wanted to switch from pyyaml
# TODO: ruamel.yaml has switched away from mimicking pyyaml syntax, meaning 0.18 and above break this code.
# It would be nice to make the code work with 0.18, but since I wrote it all for pyyaml and am last-min changing, no time now
import yaml
#import ruamel.yaml as yaml
import time
from timeit import timeit
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer

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
    # This is a third dict for experimental performance optimization, which aims to speed up te search calls for each rule
    ssg_labeledcontrols_dictionary = {}

    # Defining resources path
    resources_path = root_dir + "/resources"

    # Starting a timer to see how long it takes to generate all these rules (could definitely be made more efficient)
    # One big improvement, initializing BeautifulSoup for each site only once, and then storing it in the dict
    start_time = time.time()

    for ssg_control_file in glob.iglob(f"{resources_path}/*.html"):
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
        # In theory, this could result in dictionary collisions if we did normal prefix comparisons.
        # To resolve this, we will use the second split and the last split, concatenated together. 
        # Let's try preloading all the relevant sections into a giant dictionary, since right now our Soup calls are up to 0.04secs
        # We may need to look at lots more SSG html files at once, and make more rules, so speed is key!
        ssg_file_path = os.path.join(resources_path,ssg_control_file)
        try:
            with open(ssg_file_path, 'r', encoding='utf-8') as file:
                basename = os.path.basename(ssg_file_path)
                print(f"Saving into SSG dictionary with the key {basename}") 
                ssg_controls_dictionary[basename] = BeautifulSoup(file.read(),"lxml")
                ssg_rawtext_dictionary[basename] = ssg_controls_dictionary[basename].get_text()
                # Let's run a find_all on this, and then place all the finds into a dictionary, titled by their ID
                ssg_labeledcontrols_dictionary[basename] = {}
                for control in ssg_controls_dictionary[basename].find_all("tr",attrs={"data-tt-id":True},class_="guide-tree-leaf"):
                    ssg_labeledcontrols_dictionary[basename][control["data-tt-id"]] = control
                #print(ssg_labeledcontrols_dictionary[basename])
                print(f"Successfully found and loaded SSG HTML file: {ssg_file_path}")
        except Exception:
            # TODO: More advanced error reporting
            print(f"Unable to load SSG HTML file: {ssg_file_path}")


    # Change to rules dir to begin creating test rules
    os.chdir(root_dir)

    # Load NIST 800-53 yaml
    with open(root_dir + "/includes/800-53_baselines.yaml",'r') as file:
        nist_yaml = yaml.safe_load(file)

    # Iterate through each row in our spreadsheet
    valid_rules=0
    # Count successful populations
    populated_rules = 0
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
    # Skip the first row as this is the column titles
    for row in sheet.iter_rows(min_row=2,values_only=True):
        # Look for rows with a valid name set AND a valid CIS or STIG rule
        if row[0] and (row[2] or row[4]):
            # In our sheet, column 1 is the full file name, column 2 is the type (os, audit, etc), and column 3 and 5 are the relevant CIS and STIG IDs. 
            filepath=Path(os.getcwd() + "/rules/" + row[1] + "/" + row[0])
            # Create the os, audit, pwpolicy, etc dirs if they don't already exist in output dir
            os.makedirs(os.path.dirname(Path(os.getcwd() + "/" + results.outputdir + "/" + row[1] + "/" + row[0])), exist_ok=True)
            yaml_dict=dict(
                id = "",
                title = "",
                discussion = "",
                check = multiline("$OS_VALUE"),
                result = {"integer":1},
                fix = multiline("$OS_VALUE"),
                references={
                    "cce":["$OS_VALUE"],
                    "cci":[],
                    "800-53r5":[],
                    "srg":[],
                    "disa_stig":["$OS_VALUE"],
                    "cis":{
                        "benchmark":["$OS_VALUE"]
                    },
                },
                tags = [],
                severity = "",
                os_specifics = {},
            )
            if not filepath.is_file() or results.overwrite:
                #if not filepath.is_file():
                #    print(f"{row[0]} does not exist.")
                #elif results.overwrite:
                #    print(f"{row[0]} does exist, but overwrite enabled. Recreating...")
                # Grab the data from the HTML file dictionary for each, and propogate it into the yaml file we need to create
                # TODO: at some point down the road might be nice to not have to search the entire file each time, maybe preload it into a data structure
                # This sets the control ID to be the CIS one, if no CIS one, set to STIG, since one must exist
                # (In our schema, both columns contain SSG-type rules, so defaulting to CIS is fine if both exist)
                control_id = row[2] if row[2] else row[4]
                #start1 = time.time()
                for name, ssg_html in ssg_controls_dictionary.items():
                    # Try and find the tr item in each based off the ID we want.
                    soup = ssg_html
                    # TODO: This is all repetitive data grabbing that probably doesn't need to happen. 
                    # TODO: In theory, all the files should have the same CCI's etc as well. 
                    # Test doing this for efficiency, since we eat 0.03-0.05 per each failed SSG search
                    # In contrast, successful searches are within 0.002-0.003, so order of magnitude faster
                    # if text in string checks are very fast, so if we can precache the text then search it, this should remove a lot of wasted time
                    # Time efficiency for the inside check is e-05 efficiency, so HUGE benefit! 
                    #start = time.time()
                    if control_id in ssg_labeledcontrols_dictionary[name].keys():
                        control = ssg_labeledcontrols_dictionary[name][control_id]
                        #control = soup.find("tr", {"data-tt-id":control_id})
                    else:
                        control = None
                    #end = time.time()
                    #exect = end - start
                    # It seems like relative execution time for this is 0.001-0.01 per SSG, and with 9-10 SSGs, this gets you a max of 0.1 and a min of 0.01
                    # On average, I'm seeing about 0.05 here, from a total execution time of about 0.15 per rule. For now, let's focus on that remaining 0.10 and not here
                    #print(f"Soup Execution time for {control_id} in {name}: {exect} seconds. Match: {(control is not None)}")
                    if control:
                        # Define the os specifics category here, since we don't care if it doesn't have the control :)
                        os_blob = name.split("-")[1]
                        os_title = regex_and_return_first_match(regex_cache[0],os_blob)
                        os_version = regex_and_return_first_match(regex_cache[1],os_blob)
                        cis_level = regex_and_return_first_match(regex_cache[2],name)
                        cis_type = regex_and_return_first_match(regex_cache[3],name)
                        stig_type = regex_and_return_first_match(regex_cache[4],name)
                        if os_title not in yaml_dict["os_specifics"].keys():
                            yaml_dict["os_specifics"][os_title] = {}
                        if os_version not in yaml_dict["os_specifics"][os_title].keys():
                            yaml_dict["os_specifics"][os_title][os_version] = {}
                        yaml_dict["os_specifics"][os_title][os_version] = {"references":{"cce":[],"disa_stig":[]},"check":None,"fix":None}
                        yaml_dict["id"] = row[0].split(".")[0]
                        # TODO: In theory, all of these values should be the same for every rule. If they are not, we may want to do something about this
                        #print(f"{control_id} is defined in SSG {name}.")
                        # Now we need to extract relevant information from it.
                        # Let's start with the title, as the id is already defined
                        title = control.find("h4")
                        if title:
                            yaml_dict["title"] = title.get_text().split("\n")[1].strip()
                            #print(f"Control Title is {title.get_text().split("\n")[1].strip()}")
                        #Now let's grab the discussion (labeled as rationale)
                        discussion = control.find(class_="rationale")
                        if discussion:
                            # TODO: Do we actually need these multiline tags?
                            yaml_dict["discussion"] = multiline(discussion.get_text(strip=False))
                            #print(f"Control Discussion field is {discussion.get_text(strip=True)}")
                        # And the severity
                        severity = control.find(class_="severity")
                        if severity:
                            yaml_dict["severity"] = severity.get_text(strip=True)
                            #print(f"Control Severity field is {severity.get_text(strip=True)}")
                        # Let's add tags based on the kind of SSG this is
                        # TODO: This maybe could/should be done with the content, rather than the title, as the title can be changed
                        if cis_level:
                            if cis_level == "level1":
                                unique_append(yaml_dict["tags"],"cis_lvl1")
                            elif cis_level == "level2":
                                unique_append(yaml_dict["tags"], "cis_lvl2")
                            else:
                                print("WARNING: THIS STATEMENT SHOULD NOT BE REACHED WITH ACCURATE PARSING.")
                        if cis_type:
                            if cis_type == "server":
                                unique_append(yaml_dict["tags"],"server")
                            elif cis_type == "workstation":
                                unique_append(yaml_dict["tags"],"client")
                        if stig_type:
                            unique_append(yaml_dict["tags"],"stig")
                            if stig_type == "stig":
                                unique_append(yaml_dict["tags"],"server")
                            elif stig_type == "stig_gui":
                                unique_append(yaml_dict["tags"], "client")
                        # Now for the fun part! Grabbing the various CCIs, STIGs, and 800-53's from identifiers
                        identifiers = control.find(class_="identifiers")
                        if identifiers:
                            # We'll need to process this, split out the right ones, and place them into the file
                            # You might be wondering why I'm using re.compile rather than just the letter a.
                            # This is because in SSG files, specifically RHEL ones, the CCE field is an "addr" tag, not an "a" tag.
                            # But guess what letter both start with? :)
                            for identifier in identifiers.find_all(re.compile("^a")):
                                # Let's get the actual text, without the tags and such
                                # Technically, if we wanted to be really sure that each match was right, we could check the HREFs of the a tags instea
                                # Since every single CCI should go to the CCI site, 800-53r5 to NIST, et cetera
                                # But I've taken a look at the current dataset and am making the execute decision that this isn't necessary at this time.
                                # TODO: Maybe a future idea?
                                raw_identifier = identifier.get_text(strip=True)
                                yaml_references = yaml_dict["references"]
                                yaml_os_specificrefs = yaml_dict["os_specifics"][os_title][os_version]["references"]
                                ccematch = regex_and_return_first_match(regex_cache[5], raw_identifier)
                                if ccematch:
                                    # We have a CCE match!
                                    # Since these are OS-specific, let's place them in the specific subsection for the OS this guide references from
                                    unique_append(yaml_os_specificrefs["cce"],ccematch)
                                    continue
                                srgmatch = regex_and_return_first_match(regex_cache[6], raw_identifier)
                                if srgmatch:
                                    # We have an SRG match!
                                    unique_append(yaml_references["srg"],srgmatch)
                                    continue
                                # Turns out there are a LOT of items that look weirdly similar to the 800-53s... such as DE.AE-2
                                nistmatch = regex_and_return_first_match(regex_cache[7], raw_identifier)
                                if nistmatch:
                                    # We have an 800-53 match!
                                    unique_append(yaml_references["800-53r5"],nistmatch)
                                    # For these, since we have 800-53r5 scorings as well, we'll want to calculate those here as well.
                                    if nistmatch in nist_yaml["low"]:
                                        unique_append(yaml_dict["tags"],"800-53r5_low")
                                    if nistmatch in nist_yaml["moderate"]:
                                        unique_append(yaml_dict["tags"],"800-53r5_moderate")
                                    if nistmatch in nist_yaml["high"]:
                                        unique_append(yaml_dict["tags"],"800-53r5_high")
                                    continue
                                ccimatch = regex_and_return_first_match(regex_cache[8], raw_identifier)
                                if ccimatch:
                                    # We have a CCI match!
                                    unique_append(yaml_references["cci"],ccimatch)
                                    continue
                                stigmatch = regex_and_return_first_match(regex_cache[9],raw_identifier)
                                if stigmatch:
                                    # We have a STIG match!
                                    # Since these are OS-specific, let's place them in the specific subsection for the OS this guide references from
                                    unique_append(yaml_os_specificrefs["disa_stig"],stigmatch)
                                    continue
                                #print(f"CCE Match: {compile_and_return_first_match(r"CCE\-\d{5}\-\d{1}", raw_identifier)}")
                                #print(f"SRG Match: {compile_and_return_first_match(r"SRG\-OS\-\d{6}\-GPOS\-\d{5}", raw_identifier)}")
                                #print(f"CCI Match: {compile_and_return_first_match(r"CCI\-\d{6}", raw_identifier)}")
                                #print(f"800-53r5 Match: {compile_and_return_first_match(r"[A-Z]{2}\-\d{1,2}\({0,1}\d{0,2}\){0,1}", raw_identifier)}")
                                #print(identifier.get_text())
                        shellbutton = control.find(string="Remediation Shell script ⇲")
                        if shellbutton:
                            # The array indexing at 1 is to remove the # prefixing the ID
                            # Need to add the code tag since there can be other tags in this div
                            remediation = "[source,bash]\n---\n" + control.find(id=shellbutton.parent["data-target"][1:]).code.get_text() + "\n---"
                            yaml_dict["os_specifics"][os_title][os_version]["fix"] = multiline(remediation)
                            #print(yaml_dict)
                try:
                    # This is the biggest slowdown I can find, taking sometimes 0.04 seconds to complete. 
                    with open(Path(os.getcwd() + "/" + results.outputdir + "/" + row[1] + "/" + row[0]), 'w') as file:
                    #with open(Path(os.getcwd() + "/" + results.outputdir + "/" + row[0]), 'w') as file:
                        # Apparently custom dumpers don't work with safe_dump. Not awesome
                        # Another really frustrating behavior is that pyyaml handles multi lines like below weird:
                        # A multiline string SHOULD look like this:
                        # key: |
                        #    value value value
                        #    value value value
                        # But pyyaml writes below, no matter what you do (see issue #411 on their github, unresolved since 2022)
                        # key: "value\\\
                        # \\ value \\ \n value \\ value"
                        # Nearly gotten it working using a custom parser further up, except for a frustrating issue! Instead of:
                        # |
                        # text 
                        # text
                        # We instead get 
                        # |-
                        # text 
                        # text
                        # Thanks to this amazing article https://joekiller.com/2023/10/21/yaml-pipe-dash-what/ I've learned block chomping!
                        yaml.dump(yaml_dict, file, default_style=False, sort_keys=False, allow_unicode=True, Dumper=IndentDumper)
                    print(f"Successfully populated and wrote {row[0]}!")
                except Exception as error:
                    print(f"Error: Unable to produce the file {row[0]}! The specific error is {error}.")
                    print(traceback.format_exc())
                    sys.exit(-1)
                populated_rules += 1
                #end1 = time.time()
                #exect = end1 - start1
                #print(f"Total time taken for {control_id} is {exect}.")
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